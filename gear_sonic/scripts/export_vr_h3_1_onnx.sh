#!/usr/bin/env bash
set -euo pipefail

CALLER_PWD="${PWD}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

if [[ $# -gt 0 ]]; then
  CHECKPOINT="$1"
  if [[ "${CHECKPOINT}" != /* && ! -e "${REPO_ROOT}/${CHECKPOINT}" && -e "${CALLER_PWD}/${CHECKPOINT}" ]]; then
    CHECKPOINT="${CALLER_PWD}/${CHECKPOINT}"
  fi
else
  CHECKPOINT="data/model_step_100000.pt"
fi

ROBOT_MOTION_FILE="${ROBOT_MOTION_FILE:-data/my_robot_motions/robot}"
SMPL_MOTION_FILE="${SMPL_MOTION_FILE:-data/smpl_filtered}"

cd "${REPO_ROOT}"

python "${REPO_ROOT}/gear_sonic/eval_agent_trl.py" \
  +exp=manager/universal_token/all_modes/sonic_vr_h3_1 \
  checkpoint="${CHECKPOINT}" \
  num_envs=1 \
  headless=True \
  +export_onnx_only=true \
  ++manager_env.commands.motion.motion_lib_cfg.motion_file="${ROBOT_MOTION_FILE}" \
  ++manager_env.commands.motion.motion_lib_cfg.smpl_motion_file="${SMPL_MOTION_FILE}"
