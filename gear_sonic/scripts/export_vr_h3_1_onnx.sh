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
  CHECKPOINT="logs_rl/TRL_VR_H3_1_Track/manager/universal_token/all_modes/sonic_vr_h3_1_test-20260508_175136/model_step_100000.pt"
fi

PYTHON_BIN="${PYTHON_BIN:-python}"
ROBOT_MOTION_FILE="${ROBOT_MOTION_FILE:-data/motion_lib_bones_seed/vr_h3_1_filtered}"
SMPL_MOTION_FILE="${SMPL_MOTION_FILE:-dummy}"

cd "${REPO_ROOT}"

if [[ ! -f "${CHECKPOINT}" ]]; then
  echo "Missing checkpoint: ${CHECKPOINT}" >&2
  exit 1
fi

if [[ ! -d "${ROBOT_MOTION_FILE}" ]]; then
  echo "Missing H3 motion directory: ${ROBOT_MOTION_FILE}" >&2
  exit 1
fi

"${PYTHON_BIN}" "${REPO_ROOT}/gear_sonic/eval_agent_trl.py" \
  +exp=manager/universal_token/all_modes/sonic_vr_h3_1 \
  checkpoint="${CHECKPOINT}" \
  num_envs=1 \
  headless=True \
  +export_onnx_only=true \
  ++manager_env.commands.motion.motion_lib_cfg.motion_file="${ROBOT_MOTION_FILE}" \
  ++manager_env.commands.motion.motion_lib_cfg.smpl_motion_file="${SMPL_MOTION_FILE}"
