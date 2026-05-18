#!/usr/bin/env bash
set -euo pipefail

# Compare the released SONIC G1 checkpoint against the finetuned run from WandB
# emj8wxux using the same deterministic Isaac eval settings.

NUM_ENVS="${NUM_ENVS:-128}"
MAX_MOTIONS="${MAX_MOTIONS:-512}"
HEADLESS="${HEADLESS:-True}"
PYTHON_BIN="${PYTHON_BIN:-python}"

if [[ -z "${MOTION_FILE:-}" ]]; then
  if [[ -d data/motion_lib_bones_seed/robot_filtered ]]; then
    MOTION_FILE="data/motion_lib_bones_seed/robot_filtered"
  else
    MOTION_FILE="data/motion_lib_bones_seed/g1_filtered"
  fi
fi

if [[ -z "${SMPL_MOTION_FILE:-}" ]]; then
  if [[ -d data/motion_lib_bones_seed/1215_bones_seed_filtered ]]; then
    SMPL_MOTION_FILE="data/motion_lib_bones_seed/1215_bones_seed_filtered"
  elif [[ -d data/smpl_filtered ]]; then
    SMPL_MOTION_FILE="data/smpl_filtered"
  else
    SMPL_MOTION_FILE="sample_data/smpl_filtered"
  fi
fi

RELEASE_CKPT="${RELEASE_CKPT:-sonic_release/last.pt}"
FINETUNE_RUN_DIR="${FINETUNE_RUN_DIR:-logs_rl/TRL_G1_Track/manager/universal_token/all_modes/sonic_release_test-20260515_093340}"

CHECKPOINTS=(
  "$RELEASE_CKPT"
  "$FINETUNE_RUN_DIR/model_step_002000.pt"
  "$FINETUNE_RUN_DIR/model_step_004000.pt"
  "$FINETUNE_RUN_DIR/last.pt"
)

export WANDB_MODE="${WANDB_MODE:-disabled}"
export WANDB_DISABLED="${WANDB_DISABLED:-true}"
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

if ! "$PYTHON_BIN" -c 'import smpl_sim' >/dev/null 2>&1; then
  echo "Missing Python module: smpl_sim" >&2
  echo "The im_eval callback imports smpl_sim only when computing final metrics," >&2
  echo "so without it the eval can waste minutes and then crash at the end." >&2
  echo >&2
  echo "Install it in the same env used for eval_agent_trl.py, then rerun:" >&2
  echo "  /home/hantp/miniconda3/envs/env_isaaclab/bin/pip install git+https://github.com/ZhengyiLuo/SMPLSim.git" >&2
  echo >&2
  echo "Then make sure: $PYTHON_BIN -c 'import smpl_sim' succeeds." >&2
  exit 1
fi

if [[ "$SMPL_MOTION_FILE" == sample_data/* ]]; then
  echo "WARNING: using sample SMPL motions: $SMPL_MOTION_FILE" >&2
  echo "This is useful for smoke tests, but it is not a fair release-vs-finetune eval." >&2
  echo "Set SMPL_MOTION_FILE=/path/to/full/smpl_filtered for real metrics." >&2
fi

for ckpt in "${CHECKPOINTS[@]}"; do
  if [[ ! -f "$ckpt" ]]; then
    echo "Skipping missing checkpoint: $ckpt" >&2
    continue
  fi

  name="$(basename "$(dirname "$ckpt")")_$(basename "$ckpt" .pt)"
  echo
  echo "================================================================"
  echo "Evaluating: $ckpt"
  echo "Eval name : $name"
  echo "Motion    : $MOTION_FILE"
  echo "SMPL      : $SMPL_MOTION_FILE"
  echo "================================================================"

  "$PYTHON_BIN" gear_sonic/eval_agent_trl.py \
    +checkpoint="$ckpt" \
    +headless="$HEADLESS" \
    ++eval_callbacks=im_eval \
    ++run_eval_loop=False \
    ++num_envs="$NUM_ENVS" \
    ++eval_name="$name" \
    "+manager_env/terminations=tracking/eval" \
    "++manager_env.commands.motion.motion_lib_cfg.max_unique_motions=$MAX_MOTIONS" \
    "++manager_env.commands.motion.motion_lib_cfg.motion_file=$MOTION_FILE" \
    "++manager_env.commands.motion.motion_lib_cfg.smpl_motion_file=$SMPL_MOTION_FILE"
done
