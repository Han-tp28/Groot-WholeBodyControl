#!/usr/bin/env bash
set -euo pipefail

# VR_H3_1 training launcher following docs/source/user_guide.
# The experiment config keeps motion_file unset; this script provides the
# command-line motion overrides recommended by the guide.
#
# Useful overrides:
#   NUM_ENVS=16 HEADLESS=False   visual debug run
#   SMPL_MOTION_FILE=...         use matching SMPL data, or dummy
#   BASE_CKPT=...   resume/finetune from an existing checkpoint
#   NUM_PROCESSES=2 launch with accelerate multi-GPU

PYTHON_BIN="${PYTHON_BIN:-python}"
HEADLESS="${HEADLESS:-True}"

MOTION_FILE="${MOTION_FILE:-data/motion_lib_bones_seed/vr_h3_1_filtered}"
SMPL_MOTION_FILE="${SMPL_MOTION_FILE:-dummy}"
NUM_ENVS="${NUM_ENVS:-4096}"
NUM_STEPS_PER_ENV="${NUM_STEPS_PER_ENV:-24}"
MAX_ITERS="${MAX_ITERS:-100000}"
ACTOR_LR="${ACTOR_LR:-2e-5}"
WANDB_GROUP="${WANDB_GROUP:-vr_h3_1}"
USE_WANDB="${USE_WANDB:-true}"
TERRAIN_TYPE="${TERRAIN_TYPE:-trimesh}"
CAT_UPPER_BODY_POSES="${CAT_UPPER_BODY_POSES:-true}"
FREEZE_FRAME_AUG="${FREEZE_FRAME_AUG:-true}"
PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"
NUM_PROCESSES="${NUM_PROCESSES:-1}"
EXP_VAR="${EXP_VAR:-train}"

if [[ ! -d "$MOTION_FILE" ]]; then
  echo "Missing VR_H3_1 motion directory: $MOTION_FILE" >&2
  exit 1
fi

if [[ "$SMPL_MOTION_FILE" != "dummy" && ! -d "$SMPL_MOTION_FILE" ]]; then
  echo "Missing SMPL motion directory: $SMPL_MOTION_FILE" >&2
  exit 1
fi

args=(
  gear_sonic/train_agent_trl.py
  +exp=manager/universal_token/all_modes/sonic_vr_h3_1
  num_envs="$NUM_ENVS"
  headless="$HEADLESS"
  use_wandb="$USE_WANDB"
  exp_var="$EXP_VAR"
  ++algo.config.num_learning_iterations="$MAX_ITERS"
  ++algo.config.num_steps_per_env="$NUM_STEPS_PER_ENV"
  ++algo.config.actor_learning_rate="$ACTOR_LR"
  ++wandb.wandb_group="$WANDB_GROUP"
  ++manager_env.config.terrain_type="$TERRAIN_TYPE"
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
  args+=(+checkpoint="$BASE_CKPT")
fi

if [[ -n "${WANDB_ENTITY:-}" ]]; then
  args+=(++wandb.wandb_entity="$WANDB_ENTITY")
fi

echo "Training VR_H3_1"
echo "  checkpoint  : ${BASE_CKPT:-scratch}"
echo "  motion_file : $MOTION_FILE"
echo "  smpl_file   : $SMPL_MOTION_FILE"
echo "  exp_var     : $EXP_VAR"
echo "  num_envs    : $NUM_ENVS"
echo "  steps/env   : $NUM_STEPS_PER_ENV"
echo "  max_iters   : $MAX_ITERS"
echo "  actor_lr    : $ACTOR_LR"
echo

if [[ "$NUM_PROCESSES" -gt 1 ]]; then
  HYDRA_FULL_ERROR="${HYDRA_FULL_ERROR:-1}" \
  PYTORCH_CUDA_ALLOC_CONF="$PYTORCH_CUDA_ALLOC_CONF" \
  accelerate launch --multi_gpu --num_processes="$NUM_PROCESSES" "${args[@]}"
else
  HYDRA_FULL_ERROR="${HYDRA_FULL_ERROR:-1}" \
  PYTORCH_CUDA_ALLOC_CONF="$PYTORCH_CUDA_ALLOC_CONF" \
  "$PYTHON_BIN" "${args[@]}"
fi
