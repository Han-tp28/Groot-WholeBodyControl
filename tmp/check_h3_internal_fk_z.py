import joblib
import numpy as np
import torch
from easydict import EasyDict

from gear_sonic.utils.motion_lib.torch_humanoid_batch import Humanoid_Batch


MOTION = "data/my_robot_motions/robot_filtered/240529/neutral_deep_breath_001__A544.pkl"

cfg = EasyDict(
    {
        "asset": {
            "assetRoot": "gear_sonic/data/assets/robot_description/mjcf/",
            "assetFileName": "vr_h3_1_rl.xml",
            "urdfFileName": "",
        },
        "extend_config": [],
    }
)

data = joblib.load(MOTION)
key = next(iter(data))
entry = data[key]

pose = torch.from_numpy(np.asarray(entry["pose_aa"], dtype=np.float32))[None]
trans = torch.from_numpy(np.asarray(entry["root_trans_offset"], dtype=np.float32))[None]

fk = Humanoid_Batch(cfg)
res = fk.fk_batch(pose, trans, fps=int(entry["fps"]), target_fps=50, interpolate_data=False)
pos = res.global_translation.squeeze(0).detach().cpu().numpy()

print("motion", key, "frames", pos.shape[0], "bodies", pos.shape[1])
print("body names")
for i, name in enumerate(fk.body_names):
    print(f"{i:02d} {name}")

names = [
    "pelvis",
    "left_ankle_roll_link",
    "right_ankle_roll_link",
    "waist_roll_link",
    "head_yaw_link",
]
print("\nselected body z")
for name in names:
    if name not in fk.body_names:
        print(name, "missing")
        continue
    i = fk.body_names.index(name)
    z = pos[:, i, 2]
    print(f"{name:24s} idx={i:02d} first={z[0]:.6f} min={z.min():.6f} max={z.max():.6f} mean={z.mean():.6f}")

root_z = np.asarray(entry["root_trans_offset"])[:, 2]
print("\nroot_trans_offset z", root_z[0], root_z.min(), root_z.max(), root_z.mean())
all_min = pos[:, :, 2].min(axis=1)
print("all body min z first/min/max/mean", all_min[0], all_min.min(), all_min.max(), all_min.mean())

# IsaacLab selected H3 body_names from sonic_vr_h3_1.yaml
selected = [
    "pelvis", "left_hip_roll_link", "left_knee_pitch_link", "left_ankle_roll_link",
    "right_hip_roll_link", "right_knee_pitch_link", "right_ankle_roll_link",
    "waist_roll_link", "left_shoulder_roll_link", "left_elbow_pitch_link",
    "left_wrist_pitch_link", "right_shoulder_roll_link", "right_elbow_pitch_link",
    "right_wrist_pitch_link",
]
print("\nselected command body z first/mean")
for name in selected:
    i = fk.body_names.index(name)
    z = pos[:, i, 2]
    print(f"{name:24s} idx={i:02d} first={z[0]:.6f} mean={z.mean():.6f}")
