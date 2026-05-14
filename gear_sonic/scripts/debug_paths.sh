#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
echo "SCRIPT_DIR: ${SCRIPT_DIR}"
echo "REPO_ROOT: ${REPO_ROOT}"
echo "Current PWD: ${PWD}"
cd "${REPO_ROOT}"
echo "New PWD: ${PWD}"
ls -d gear_sonic/eval_agent_trl.py
