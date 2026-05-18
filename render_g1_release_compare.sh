#!/usr/bin/env bash
set -euo pipefail

# Render release vs finetuned G1 checkpoints with the same eval setup.
# Output videos go under /tmp/g1_release_compare_renders by default.

NUM_ENVS="${NUM_ENVS:-8}"
RENDER_DIR="${RENDER_DIR:-/tmp/g1_release_compare_renders}"

MOTION_FILE="${MOTION_FILE:-data/motion_lib_bones_seed/g1_filtered}"
SMPL_MOTION_FILE="${SMPL_MOTION_FILE:-sample_data/smpl_filtered}"

RELEASE_CKPT="${RELEASE_CKPT:-sonic_release/last.pt}"
FINETUNE_RUN_DIR="${FINETUNE_RUN_DIR:-logs_rl/TRL_G1_Track/manager/universal_token/all_modes/sonic_release_test-20260515_093340}"

CHECKPOINTS=(
  "$RELEASE_CKPT"
  "$FINETUNE_RUN_DIR/model_step_004000.pt"
  "$FINETUNE_RUN_DIR/last.pt"
)

export WANDB_MODE="${WANDB_MODE:-disabled}"
export WANDB_DISABLED="${WANDB_DISABLED:-true}"
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

for ckpt in "${CHECKPOINTS[@]}"; do
  if [[ ! -f "$ckpt" ]]; then
    echo "Skipping missing checkpoint: $ckpt" >&2
    continue
  fi

  name="$(basename "$(dirname "$ckpt")")_$(basename "$ckpt" .pt)"
  out_dir="$RENDER_DIR/$name"
  mkdir -p "$out_dir"

  echo
  echo "================================================================"
  echo "Rendering : $ckpt"
  echo "Output    : $out_dir"
  echo "Motion    : $MOTION_FILE"
  echo "SMPL      : $SMPL_MOTION_FILE"
  echo "================================================================"

  python gear_sonic/eval_agent_trl.py \
    +checkpoint="$ckpt" \
    +headless=True \
    ++eval_callbacks=im_eval \
    ++run_eval_loop=False \
    ++num_envs="$NUM_ENVS" \
    ++manager_env.config.render_results=True \
    "++manager_env.config.save_rendering_dir=$out_dir" \
    ++manager_env.config.env_spacing=10.0 \
    "+manager_env/terminations=tracking/eval" \
    "++manager_env.commands.motion.motion_lib_cfg.max_unique_motions=$NUM_ENVS" \
    "++manager_env.commands.motion.motion_lib_cfg.motion_file=$MOTION_FILE" \
    "++manager_env.commands.motion.motion_lib_cfg.smpl_motion_file=$SMPL_MOTION_FILE" \
    "~manager_env/recorders=empty" "+manager_env/recorders=render"
done
