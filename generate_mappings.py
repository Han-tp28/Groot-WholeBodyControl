IL_JOINTS = ['left_hip_pitch_joint', 'right_hip_pitch_joint', 'waist_yaw_joint', 'left_hip_roll_joint', 'right_hip_roll_joint', 'waist_roll_joint', 'left_hip_yaw_joint', 'right_hip_yaw_joint', 'left_shoulder_pitch_joint', 'right_shoulder_pitch_joint', 'left_knee_pitch_joint', 'right_knee_pitch_joint', 'left_shoulder_roll_joint', 'right_shoulder_roll_joint', 'left_ankle_pitch_joint', 'right_ankle_pitch_joint', 'left_shoulder_yaw_joint', 'right_shoulder_yaw_joint', 'left_ankle_roll_joint', 'right_ankle_roll_joint', 'left_elbow_pitch_joint', 'right_elbow_pitch_joint', 'left_wrist_yaw_joint', 'right_wrist_yaw_joint', 'left_wrist_roll_joint', 'right_wrist_roll_joint', 'left_wrist_pitch_joint', 'right_wrist_pitch_joint']

MJ_JOINTS = ['left_hip_pitch_joint', 'left_hip_roll_joint', 'left_hip_yaw_joint', 'left_knee_pitch_joint', 'left_ankle_pitch_joint', 'left_ankle_roll_joint', 'right_hip_pitch_joint', 'right_hip_roll_joint', 'right_hip_yaw_joint', 'right_knee_pitch_joint', 'right_ankle_pitch_joint', 'right_ankle_roll_joint', 'waist_yaw_joint', 'waist_roll_joint', 'left_shoulder_pitch_joint', 'left_shoulder_roll_joint', 'left_shoulder_yaw_joint', 'left_elbow_pitch_joint', 'left_wrist_yaw_joint', 'left_wrist_roll_joint', 'left_wrist_pitch_joint', 'right_shoulder_pitch_joint', 'right_shoulder_roll_joint', 'right_shoulder_yaw_joint', 'right_elbow_pitch_joint', 'right_wrist_yaw_joint', 'right_wrist_roll_joint', 'right_wrist_pitch_joint']

IL_BODIES = ['pelvis', 'left_hip_pitch_link', 'right_hip_pitch_link', 'waist_yaw_link', 'left_hip_roll_link', 'right_hip_roll_link', 'waist_roll_link', 'left_hip_yaw_link', 'right_hip_yaw_link', 'left_shoulder_pitch_link', 'right_shoulder_pitch_link', 'left_knee_pitch_link', 'right_knee_pitch_link', 'left_shoulder_roll_link', 'right_shoulder_roll_link', 'left_ankle_pitch_link', 'right_ankle_pitch_link', 'left_shoulder_yaw_link', 'right_shoulder_yaw_link', 'left_ankle_roll_link', 'right_ankle_roll_link', 'left_elbow_pitch_link', 'right_elbow_pitch_link', 'left_wrist_yaw_link', 'right_wrist_yaw_link', 'left_wrist_roll_link', 'right_wrist_roll_link', 'left_wrist_pitch_link', 'right_wrist_pitch_link']

MJ_BODIES = ['pelvis', 'left_hip_pitch_link', 'left_hip_roll_link', 'left_hip_yaw_link', 'left_knee_pitch_link', 'left_ankle_pitch_link', 'left_ankle_roll_link', 'right_hip_pitch_link', 'right_hip_roll_link', 'right_hip_yaw_link', 'right_knee_pitch_link', 'right_ankle_pitch_link', 'right_ankle_roll_link', 'waist_yaw_link', 'waist_roll_link', 'left_shoulder_pitch_link', 'left_shoulder_roll_link', 'left_shoulder_yaw_link', 'left_elbow_pitch_link', 'left_wrist_yaw_link', 'left_wrist_roll_link', 'left_wrist_pitch_link', 'right_shoulder_pitch_link', 'right_shoulder_roll_link', 'right_shoulder_yaw_link', 'right_elbow_pitch_link', 'right_wrist_yaw_link', 'right_wrist_roll_link', 'right_wrist_pitch_link', 'head_yaw_link', 'head_pitch_link']

il_to_mj_dof = [MJ_JOINTS.index(j) for j in IL_JOINTS]
mj_to_il_dof = [IL_JOINTS.index(j) for j in MJ_JOINTS]

il_to_mj_body = [MJ_BODIES.index(b) for b in IL_BODIES]
mj_to_il_body = [IL_BODIES.index(b) if b in IL_BODIES else IL_BODIES.index('waist_roll_link') for b in MJ_BODIES]

print("VR_H3_1_ISAACLAB_JOINTS =", IL_BODIES)
print("VR_H3_1_ISAACLAB_TO_MUJOCO_DOF =", il_to_mj_dof)
print("VR_H3_1_MUJOCO_TO_ISAACLAB_DOF =", mj_to_il_dof)
print("VR_H3_1_ISAACLAB_TO_MUJOCO_BODY =", il_to_mj_body)
print("VR_H3_1_MUJOCO_TO_ISAACLAB_BODY =", mj_to_il_body)
