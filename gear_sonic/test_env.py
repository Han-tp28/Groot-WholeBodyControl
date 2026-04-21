import os
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
os.environ["TORCH_USE_CUDA_DSA"] = "1"

import torch
import sys
from gear_sonic.train_agent_trl import create_manager_env
from gear_sonic.train_agent_trl import get_args
import hydra
from omegaconf import OmegaConf

def main():
    # Construct config manually or load it
    args = ["+exp=manager/universal_token/all_modes/sonic_vr_h3_1", "num_envs=2", "headless=True", "++manager_env.commands.motion.motion_lib_cfg.motion_file=data/my_robot_motions/robot_filtered"]
    
    # We will use subprocess to run the train script with CUDA_LAUNCH_BLOCKING=1 to get the exact traceback
    pass

if __name__ == "__main__":
    main()
