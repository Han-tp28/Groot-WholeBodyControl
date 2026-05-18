#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python}"
NUM_ENVS="${NUM_ENVS:-128}"
MAX_MOTIONS="${MAX_MOTIONS:-512}"
HEADLESS="${HEADLESS:-True}"

CHECKPOINT="${1:-${CHECKPOINT:-logs_rl/TRL_VR_H3_1_Track/manager/universal_token/all_modes/sonic_vr_h3_1_test-20260508_175136/model_step_100000.pt}}"
MOTION_FILE="${MOTION_FILE:-data/motion_lib_bones_seed/vr_h3_1_filtered}"
SMPL_MOTION_FILE="${SMPL_MOTION_FILE:-dummy}"
EVAL_NAME="${EVAL_NAME:-$(basename "$(dirname "$CHECKPOINT")")_$(basename "$CHECKPOINT" .pt)_core}"

if [[ ! -f "$CHECKPOINT" ]]; then
  echo "Missing checkpoint: $CHECKPOINT" >&2
  exit 1
fi

if [[ ! -d "$MOTION_FILE" ]]; then
  echo "Missing H3 motion directory: $MOTION_FILE" >&2
  exit 1
fi

if ! "$PYTHON_BIN" -c 'import smpl_sim' >/dev/null 2>&1; then
  echo "Missing Python module: smpl_sim" >&2
  echo "Install in env_isaaclab:" >&2
  echo "  /home/hantp/miniconda3/envs/env_isaaclab/bin/pip install git+https://github.com/ZhengyiLuo/SMPLSim.git" >&2
  exit 1
fi

echo "Evaluating VR_H3_1 core/g1-only"
echo "  checkpoint  : $CHECKPOINT"
echo "  motion_file : $MOTION_FILE"
echo "  smpl_file   : $SMPL_MOTION_FILE"
echo "  eval_name   : $EVAL_NAME"
echo

HYDRA_FULL_ERROR="${HYDRA_FULL_ERROR:-1}" "$PYTHON_BIN" gear_sonic/eval_agent_trl.py \
  +exp=manager/universal_token/all_modes/sonic_vr_h3_1 \
  checkpoint="$CHECKPOINT" \
  headless="$HEADLESS" \
  ++eval_callbacks=im_eval \
  ++run_eval_loop=False \
  ++num_envs="$NUM_ENVS" \
  ++eval_name="$EVAL_NAME" \
  "+manager_env/terminations=tracking/eval" \
  ++manager_env.commands.motion.encoder_sample_probs.g1=1.0 \
  ++manager_env.commands.motion.encoder_sample_probs.teleop=0.0 \
  ++manager_env.commands.motion.encoder_sample_probs.smpl=0.0 \
  ++manager_env.commands.motion.teleop_sample_prob_when_smpl=0.0 \
  ++manager_env.commands.motion.motion_lib_cfg.max_unique_motions="$MAX_MOTIONS" \
  ++manager_env.commands.motion.motion_lib_cfg.motion_file="$MOTION_FILE" \
  ++manager_env.commands.motion.motion_lib_cfg.smpl_motion_file="$SMPL_MOTION_FILE"
