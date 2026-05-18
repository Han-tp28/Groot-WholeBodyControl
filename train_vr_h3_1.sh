#!/usr/bin/env bash
set -euo pipefail

# Stable VR_H3_1 recipe:
#   core   : train/reference-track with g1 encoder only. This matches deploy/reference
#            behavior and is the safest default.
#   teleop : keep g1 + teleop encoders, no SMPL.
#   all    : g1 + teleop + SMPL. Use only with a real full SMPL dataset.

PYTHON_BIN="${PYTHON_BIN:-python}"
NUM_ENVS="${NUM_ENVS:-4096}"
HEADLESS="${HEADLESS:-True}"
STAGE="${STAGE:-core}"  # core | teleop | all

MOTION_FILE="${MOTION_FILE:-data/motion_lib_bones_seed/vr_h3_1_filtered}"
SAVE_FREQUENCY="${SAVE_FREQUENCY:-2000}"
WANDB_GROUP="${WANDB_GROUP:-vr_h3_1_g1_style}"
USE_WANDB="${USE_WANDB:-true}"
TERRAIN_TYPE="${TERRAIN_TYPE:-trimesh}"
CAT_UPPER_BODY_POSES="${CAT_UPPER_BODY_POSES:-true}"
FREEZE_FRAME_AUG="${FREEZE_FRAME_AUG:-true}"

DEFAULT_H3_100K="logs_rl/TRL_VR_H3_1_Track/manager/universal_token/all_modes/sonic_vr_h3_1_test-20260508_175136/model_step_100000.pt"
if [[ -z "${BASE_CKPT:-}" && -f "$DEFAULT_H3_100K" ]]; then
  BASE_CKPT="$DEFAULT_H3_100K"
fi

if [[ ! -d "$MOTION_FILE" ]]; then
  echo "Missing H3 motion directory: $MOTION_FILE" >&2
  exit 1
fi

case "$STAGE" in
  core)
    EXP_VAR="${EXP_VAR:-g1style_core_from_h3_100k}"
    MAX_ITERS="${MAX_ITERS:-30000}"
    ACTOR_LR="${ACTOR_LR:-1e-5}"
    SMPL_MOTION_FILE="${SMPL_MOTION_FILE:-dummy}"
    G1_PROB=1.0
    TELEOP_PROB=0.0
    SMPL_PROB=0.0
    TELEOP_WHEN_SMPL=0.0
    ;;
  teleop)
    EXP_VAR="${EXP_VAR:-g1style_teleop_from_core}"
    MAX_ITERS="${MAX_ITERS:-10000}"
    ACTOR_LR="${ACTOR_LR:-5e-6}"
    SMPL_MOTION_FILE="${SMPL_MOTION_FILE:-dummy}"
    G1_PROB=1.0
    TELEOP_PROB=1.0
    SMPL_PROB=0.0
    TELEOP_WHEN_SMPL=0.0
    ;;
  all)
    EXP_VAR="${EXP_VAR:-g1style_all_from_core}"
    MAX_ITERS="${MAX_ITERS:-10000}"
    ACTOR_LR="${ACTOR_LR:-5e-6}"
    SMPL_MOTION_FILE="${SMPL_MOTION_FILE:-data/smpl_filtered}"
    G1_PROB=1.0
    TELEOP_PROB=1.0
    SMPL_PROB=1.0
    TELEOP_WHEN_SMPL=0.5
    if [[ "$SMPL_MOTION_FILE" == "dummy" || ! -d "$SMPL_MOTION_FILE" ]]; then
      echo "STAGE=all needs a real SMPL dataset, got: $SMPL_MOTION_FILE" >&2
      echo "Use STAGE=core/teleop, or set SMPL_MOTION_FILE=/path/to/full/smpl_filtered." >&2
      exit 1
    fi
    ;;
  *)
    echo "Unknown STAGE=$STAGE. Use: core | teleop | all" >&2
    exit 1
    ;;
esac

args=(
  gear_sonic/train_agent_trl.py
  +exp=manager/universal_token/all_modes/sonic_vr_h3_1
  num_envs="$NUM_ENVS"
  headless="$HEADLESS"
  use_wandb="$USE_WANDB"
  exp_var="$EXP_VAR"
  ++algo.config.num_learning_iterations="$MAX_ITERS"
  ++algo.config.actor_learning_rate="$ACTOR_LR"
  ++callbacks.model_save.save_frequency="$SAVE_FREQUENCY"
  ++wandb.wandb_group="$WANDB_GROUP"
  ++manager_env.config.terrain_type="$TERRAIN_TYPE"
  ++manager_env.commands.motion.encoder_sample_probs.g1="$G1_PROB"
  ++manager_env.commands.motion.encoder_sample_probs.teleop="$TELEOP_PROB"
  ++manager_env.commands.motion.encoder_sample_probs.smpl="$SMPL_PROB"
  ++manager_env.commands.motion.teleop_sample_prob_when_smpl="$TELEOP_WHEN_SMPL"
  ++manager_env.commands.motion.cat_upper_body_poses="$CAT_UPPER_BODY_POSES"
  ++manager_env.commands.motion.freeze_frame_aug="$FREEZE_FRAME_AUG"
  ++manager_env.commands.motion.motion_lib_cfg.motion_file="$MOTION_FILE"
  ++manager_env.commands.motion.motion_lib_cfg.smpl_motion_file="$SMPL_MOTION_FILE"
)

if [[ -n "${BASE_CKPT:-}" && "$BASE_CKPT" != "none" && "$BASE_CKPT" != "null" ]]; then
  if [[ ! -f "$BASE_CKPT" ]]; then
    echo "Missing BASE_CKPT: $BASE_CKPT" >&2
    exit 1
  fi
  args+=(checkpoint="$BASE_CKPT")
fi

if [[ -n "${WANDB_ENTITY:-}" ]]; then
  args+=(++wandb.wandb_entity="$WANDB_ENTITY")
fi

echo "Training VR_H3_1"
echo "  stage       : $STAGE"
echo "  checkpoint  : ${BASE_CKPT:-scratch}"
echo "  motion_file : $MOTION_FILE"
echo "  smpl_file   : $SMPL_MOTION_FILE"
echo "  exp_var     : $EXP_VAR"
echo "  num_envs    : $NUM_ENVS"
echo "  max_iters   : $MAX_ITERS"
echo "  actor_lr    : $ACTOR_LR"
echo

HYDRA_FULL_ERROR="${HYDRA_FULL_ERROR:-1}" "$PYTHON_BIN" "${args[@]}"
