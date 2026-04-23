### Prerequisites and setup for Training 

GPU: NVIDIA GPU with CUDA 12.x (L40, A100, or H100 recommended)

OS: Ubuntu 22.04+

Python: 3.11 (required by Isaac Lab; sim/teleop/deploy scripts work on 3.10+)

Isaac Lab: 2.3+ (required for simulation environments)


### Quick start

```bash
# Install training dependencies (Isaac Lab must be installed separately — see docs)
pip install -e "gear_sonic/[training]"

# Download checkpoint + SMPL data from Hugging Face
pip install huggingface_hub
python download_from_hf.py --training


### Prepare Dataset
Download data source form  :
https://huggingface.co/datasets/bones-studio/seed

To convert G1 CSV to H3_1 CSV:
https://bitbucket.org/vinrobotics/gmr/src/main/



# Download Bones-SEED G1 CSVs from bones-studio.ai/seed, then convert and filter
python gear_sonic/data_process/convert_soma_csv_to_motion_lib.py \
    --input /path/to/bones_seed/g1/csv/ \
    --output data/motion_lib_bones_seed/robot --fps 30 --fps_source 120 --individual --num_workers 16
python gear_sonic/data_process/filter_and_copy_bones_data.py \
    --source data/motion_lib_bones_seed/robot --dest data/motion_lib_bones_seed/robot_filtered

# Finetune from released checkpoint (64+ GPUs recommended) Train multi GPU:
accelerate launch \
    --multi_gpu --num_processes=2 \
    gear_sonic/train_agent_trl.py \
    +exp=manager/universal_token/all_modes/sonic_vr_h3_1 \
    num_envs=4096 headless=True \
    ++manager_env.commands.motion.motion_lib_cfg.motion_file=data/my_robot_motions/robot_filtered \
    ++manager_env.commands.motion.motion_lib_cfg.smpl_motion_file=data/smpl_filtered
```




Train single GPU:
```bash
python gear_sonic/train_agent_trl.py \
    +exp=manager/universal_token/all_modes/sonic_vr_h3_1 \
    num_envs=4096 headless=True \
    ++manager_env.commands.motion.motion_lib_cfg.motion_file=data/my_robot_motions/robot_filtered \
    ++manager_env.commands.motion.motion_lib_cfg.smpl_motion_file=data/smpl_filtered
```

## What's Included

This release includes:

- **`gear_sonic_deploy`**: C++ inference stack for deploying SONIC policies on real hardware
- **`gear_sonic`**: Full SONIC training stack — PPO training, data processing pipeline, and configuration system for training on Bones-SEED and custom motion datasets

### Setup

> **Git LFS required.** This repo contains large binary assets (meshes, ONNX
> models). Without Git LFS, you will get small pointer files instead of actual
> data, causing silent failures. Install Git LFS first if you don't have it:
> `sudo apt install git-lfs && git lfs install`

```bash
git clone https://github.com/NVlabs/GR00T-WholeBodyControl.git
cd GR00T-WholeBodyControl
git lfs pull

# Verify your environment
python check_environment.py
```

