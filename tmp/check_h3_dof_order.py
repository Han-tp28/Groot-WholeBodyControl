import joblib
import numpy as np

MOTION = "data/my_robot_motions/robot_filtered/240529/neutral_deep_breath_001__A544.pkl"

VR_H3_1_ISAACLAB_JOINTS = [
    "pelvis", "left_hip_pitch_link", "right_hip_pitch_link", "waist_yaw_link",
    "left_hip_roll_link", "right_hip_roll_link", "waist_roll_link",
    "left_hip_yaw_link", "right_hip_yaw_link", "left_shoulder_pitch_link",
    "right_shoulder_pitch_link", "left_knee_pitch_link", "right_knee_pitch_link",
    "left_shoulder_roll_link", "right_shoulder_roll_link", "left_ankle_pitch_link",
    "right_ankle_pitch_link", "left_shoulder_yaw_link", "right_shoulder_yaw_link",
    "left_ankle_roll_link", "right_ankle_roll_link", "left_elbow_pitch_link",
    "right_elbow_pitch_link", "left_wrist_yaw_link", "right_wrist_yaw_link",
    "left_wrist_roll_link", "right_wrist_roll_link", "left_wrist_pitch_link",
    "right_wrist_pitch_link",
]
VR_H3_1_MUJOCO_TO_ISAACLAB_DOF = [
    0, 6, 12, 1, 7, 13, 2, 8, 14, 21, 3, 9, 15, 22,
    4, 10, 16, 23, 5, 11, 17, 24, 18, 25, 19, 26, 20, 27,
]

mj_dof_names = [
    "left_hip_pitch_joint",
    "left_hip_roll_joint",
    "left_hip_yaw_joint",
    "left_knee_pitch_joint",
    "left_ankle_pitch_joint",
    "left_ankle_roll_joint",
    "right_hip_pitch_joint",
    "right_hip_roll_joint",
    "right_hip_yaw_joint",
    "right_knee_pitch_joint",
    "right_ankle_pitch_joint",
    "right_ankle_roll_joint",
    "waist_yaw_joint",
    "waist_roll_joint",
    "left_shoulder_pitch_joint",
    "left_shoulder_roll_joint",
    "left_shoulder_yaw_joint",
    "left_elbow_pitch_joint",
    "left_wrist_yaw_joint",
    "left_wrist_roll_joint",
    "left_wrist_pitch_joint",
    "right_shoulder_pitch_joint",
    "right_shoulder_roll_joint",
    "right_shoulder_yaw_joint",
    "right_elbow_pitch_joint",
    "right_wrist_yaw_joint",
    "right_wrist_roll_joint",
    "right_wrist_pitch_joint",
]

isaac_dof_body_names = VR_H3_1_ISAACLAB_JOINTS[1:]
data = joblib.load(MOTION)
entry = data[next(iter(data))]
dof = np.asarray(entry["dof"])

print("dof shape", dof.shape)
print("\nfirst frame as MuJoCo order")
for i, (name, val) in enumerate(zip(mj_dof_names, dof[0])):
    print(f"{i:02d} {name:30s} {val: .6f}")

isaac = dof[0, VR_H3_1_MUJOCO_TO_ISAACLAB_DOF]
print("\nfirst frame after MUJOCO_TO_ISAACLAB_DOF")
for i, (body, val) in enumerate(zip(isaac_dof_body_names, isaac)):
    print(f"{i:02d} {body:30s} {val: .6f}")

print("\nrange by MuJoCo dof")
for i, name in enumerate(mj_dof_names):
    vals = dof[:, i]
    print(f"{i:02d} {name:30s} min={vals.min(): .4f} max={vals.max(): .4f} mean={vals.mean(): .4f}")
