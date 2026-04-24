from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
import isaaclab.sim as sim_utils

ASSET_DIR = "gear_sonic/data/assets"

ARMATURE_5020 = 0.003609725
ARMATURE_7520_14 = 0.010177520
ARMATURE_7520_22 = 0.025101925
ARMATURE_4010 = 0.00425

NATURAL_FREQ = 10 * 2.0 * 3.1415926535  # 10Hz
DAMPING_RATIO = 2.0

STIFFNESS_5020 = ARMATURE_5020 * NATURAL_FREQ**2
STIFFNESS_7520_14 = ARMATURE_7520_14 * NATURAL_FREQ**2
STIFFNESS_7520_22 = ARMATURE_7520_22 * NATURAL_FREQ**2
STIFFNESS_4010 = ARMATURE_4010 * NATURAL_FREQ**2

DAMPING_5020 = 2.0 * DAMPING_RATIO * ARMATURE_5020 * NATURAL_FREQ
DAMPING_7520_14 = 2.0 * DAMPING_RATIO * ARMATURE_7520_14 * NATURAL_FREQ
DAMPING_7520_22 = 2.0 * DAMPING_RATIO * ARMATURE_7520_22 * NATURAL_FREQ
DAMPING_4010 = 2.0 * DAMPING_RATIO * ARMATURE_4010 * NATURAL_FREQ

VR_H3_1_ISAACLAB_JOINTS = ['pelvis', 'left_hip_pitch_link', 'right_hip_pitch_link', 'waist_yaw_link', 'left_hip_roll_link', 'right_hip_roll_link', 'waist_roll_link', 'left_hip_yaw_link', 'right_hip_yaw_link', 'left_shoulder_pitch_link', 'right_shoulder_pitch_link', 'left_knee_pitch_link', 'right_knee_pitch_link', 'left_shoulder_roll_link', 'right_shoulder_roll_link', 'left_ankle_pitch_link', 'right_ankle_pitch_link', 'left_shoulder_yaw_link', 'right_shoulder_yaw_link', 'left_ankle_roll_link', 'right_ankle_roll_link', 'left_elbow_pitch_link', 'right_elbow_pitch_link', 'left_wrist_yaw_link', 'right_wrist_yaw_link', 'left_wrist_roll_link', 'right_wrist_roll_link', 'left_wrist_pitch_link', 'right_wrist_pitch_link']

# Mapping between IsaacLab order and MuJoCo order
VR_H3_1_ISAACLAB_TO_MUJOCO_DOF = [0, 3, 6, 10, 14, 18, 1, 4, 7, 11, 15, 19, 2, 5, 8, 12, 16, 20, 22, 24, 26, 9, 13, 17, 21, 23, 25, 27]
VR_H3_1_MUJOCO_TO_ISAACLAB_DOF = [0, 6, 12, 1, 7, 13, 2, 8, 14, 21, 3, 9, 15, 22, 4, 10, 16, 23, 5, 11, 17, 24, 18, 25, 19, 26, 20, 27]
VR_H3_1_ISAACLAB_TO_MUJOCO_BODY = [0, 1, 4, 7, 11, 15, 19, 2, 5, 8, 12, 16, 20, 3, 6, 9, 13, 17, 21, 23, 25, 27, 10, 14, 18, 22, 24, 26, 28, 6, 6]
VR_H3_1_MUJOCO_TO_ISAACLAB_BODY = [0, 1, 7, 13, 2, 8, 14, 3, 9, 15, 22, 4, 10, 16, 23, 5, 11, 17, 24, 6, 12, 18, 25, 19, 26, 20, 27, 21, 28]

VR_H3_1_ISAACLAB_TO_MUJOCO_MAPPING = {
    "isaaclab_joints": VR_H3_1_ISAACLAB_JOINTS,
    "isaaclab_to_mujoco_dof": VR_H3_1_ISAACLAB_TO_MUJOCO_DOF,
    "mujoco_to_isaaclab_dof": VR_H3_1_MUJOCO_TO_ISAACLAB_DOF,
    "isaaclab_to_mujoco_body": VR_H3_1_ISAACLAB_TO_MUJOCO_BODY,
    "mujoco_to_isaaclab_body": VR_H3_1_MUJOCO_TO_ISAACLAB_BODY,
}

VR_H3_1_CFG = ArticulationCfg(
    spawn=sim_utils.UrdfFileCfg(
        fix_base=False,
        replace_cylinders_with_capsules=True,
        asset_path=f"{ASSET_DIR}/robot_description/urdf/vr_h3_1/vr_h3_1_rl_28_dof.urdf",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=4,
        ),
        joint_drive=sim_utils.UrdfConverterCfg.JointDriveCfg(
            gains=sim_utils.UrdfConverterCfg.JointDriveCfg.PDGainsCfg(stiffness=0, damping=0)
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.85),
        joint_pos={
            # --- Left leg (6) ---
            "left_hip_pitch_joint":  -0.2,
            "left_hip_roll_joint":    0.0,
            "left_hip_yaw_joint":     0.0,
            "left_knee_pitch_joint":  0.4,
            "left_ankle_pitch_joint": -0.2,
            "left_ankle_roll_joint":  0.0,
            # --- Right leg (6) ---
            "right_hip_pitch_joint":  -0.2,
            "right_hip_roll_joint":    0.0,
            "right_hip_yaw_joint":     0.0,
            "right_knee_pitch_joint":  0.4,
            "right_ankle_pitch_joint": -0.2,
            "right_ankle_roll_joint":  0.0,
            # --- Waist (2) ---
            "waist_yaw_joint":  0.0,
            "waist_roll_joint": 0.0,
            # --- Left arm (7) ---
            "left_shoulder_pitch_joint": 0.0,
            "left_shoulder_roll_joint":  0.2,
            "left_shoulder_yaw_joint":   0.0,
            "left_elbow_pitch_joint":    1.0,
            "left_wrist_yaw_joint":      0.0,
            "left_wrist_roll_joint":     0.0,
            "left_wrist_pitch_joint":    0.0,
            # --- Right arm (7) ---
            "right_shoulder_pitch_joint": 0.0,
            "right_shoulder_roll_joint": -0.2,
            "right_shoulder_yaw_joint":   0.0,
            "right_elbow_pitch_joint":    1.0,
            "right_wrist_yaw_joint":      0.0,
            "right_wrist_roll_joint":     0.0,
            "right_wrist_pitch_joint":    0.0,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*_hip_yaw_joint",
                ".*_hip_roll_joint",
                ".*_hip_pitch_joint",
                ".*_knee_pitch_joint",
            ],
            effort_limit_sim={
                ".*_hip_yaw_joint": 191.0,
                ".*_hip_roll_joint": 369.0,
                ".*_hip_pitch_joint": 369.0,
                ".*_knee_pitch_joint": 369.0,
            },
            velocity_limit_sim=3.141,
            stiffness={
                ".*_hip_pitch_joint": 913.0,
                ".*_hip_roll_joint": 906.0,
                ".*_hip_yaw_joint": 155.0,
                ".*_knee_pitch_joint": 561.0,
            },
            damping={
                ".*_hip_pitch_joint": 73.0,
                ".*_hip_roll_joint": 72.0,
                ".*_hip_yaw_joint": 12.0,
                ".*_knee_pitch_joint": 45.0,
            },
            armature={
                ".*_hip_pitch_joint": 3.08632,
                ".*_hip_roll_joint": 3.08632,
                ".*_hip_yaw_joint": 0.95791,
                ".*_knee_pitch_joint": 3.08632,
            },
        ),
        "feet": ImplicitActuatorCfg(
            joint_names_expr=[".*_ankle_pitch_joint", ".*_ankle_roll_joint"],
            effort_limit_sim=140.0,
            velocity_limit_sim=3.141,
            stiffness={
                ".*_ankle_pitch_joint": 658.0,
                ".*_ankle_roll_joint": 646.0,
            },
            damping={
                ".*_ankle_pitch_joint": 35.0,
                ".*_ankle_roll_joint": 34.0,
            },
            armature=0.45348,
        ),
        "waist": ImplicitActuatorCfg(
            joint_names_expr=["waist_roll_joint", "waist_yaw_joint"],
            effort_limit_sim=102.0,
            velocity_limit_sim=4.18,
            stiffness=367.0,
            damping=29.0,
            armature=0.5804369,
        ),
        "arms": ImplicitActuatorCfg(
            joint_names_expr=[
                ".*_shoulder_pitch_joint",
                ".*_shoulder_roll_joint",
                ".*_shoulder_yaw_joint",
                ".*_elbow_pitch_joint",
                ".*_wrist_yaw_joint",
                ".*_wrist_roll_joint",
                ".*_wrist_pitch_joint",
            ],
            effort_limit_sim={
                ".*_shoulder_pitch_joint": 66.0,
                ".*_shoulder_roll_joint": 66.0,
                ".*_shoulder_yaw_joint": 66.0,
                ".*_elbow_pitch_joint": 66.0,
                ".*_wrist_yaw_joint": 34.0,
                ".*_wrist_roll_joint": 11.0,
                ".*_wrist_pitch_joint": 11.0,
            },
            velocity_limit_sim={
                ".*_shoulder_pitch_joint": 3.141,
                ".*_shoulder_roll_joint": 2.356,
                ".*_shoulder_yaw_joint": 2.967,
                ".*_elbow_pitch_joint": 1.571,
                ".*_wrist_yaw_joint": 1.571,
                ".*_wrist_roll_joint": 1.571,
                ".*_wrist_pitch_joint": 1.571,
            },
            stiffness={
                ".*_shoulder_pitch_joint": 103.0,
                ".*_shoulder_roll_joint": 94.0,
                ".*_shoulder_yaw_joint": 291.0,
                ".*_elbow_pitch_joint": 291.0,
                ".*_wrist_yaw_joint": 291.0,
                ".*_wrist_roll_joint": 213.0,
                ".*_wrist_pitch_joint": 212.0,
            },
            damping={
                ".*_shoulder_pitch_joint": 8.0,
                ".*_shoulder_roll_joint": 7.0,
                ".*_shoulder_yaw_joint": 23.0,
                ".*_elbow_pitch_joint": 23.0,
                ".*_wrist_yaw_joint": 12.0,
                ".*_wrist_roll_joint": 8.0,
                ".*_wrist_pitch_joint": 8.0,
            },
            armature={
                ".*_shoulder_pitch_joint": 0.3896782,
                ".*_shoulder_roll_joint": 0.3896782,
                ".*_shoulder_yaw_joint": 0.3896782,
                ".*_elbow_pitch_joint": 0.3896782,
                ".*_wrist_yaw_joint": 0.1142512,
                ".*_wrist_roll_joint": 0.0836482,
                ".*_wrist_pitch_joint": 0.0836482,
            },
        ),
    },
)

VR_H3_1_ACTION_SCALE = {}
for a in VR_H3_1_CFG.actuators.values():
    e = a.effort_limit_sim
    s = a.stiffness
    names = a.joint_names_expr
    if not isinstance(e, dict):
        e = dict.fromkeys(names, e)
    if not isinstance(s, dict):
        s = dict.fromkeys(names, s)
    for n in names:
        if n in e and n in s and s[n]:
            VR_H3_1_ACTION_SCALE[n] = 0.25 * e[n] / s[n]
