"""VR H3_1 28-DOF IsaacLab config.

Actuator constants are ported from the standard VR_H3_1 28-DOF MJCF config.
"""

from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
import isaaclab.sim as sim_utils

ASSET_DIR = "gear_sonic/data/assets"

ARMATURE_EROB110H100 = 3.08632
ARMATURE_EROB90H100 = 0.95791
ARMATURE_EROB70H100 = 0.22674
ARMATURE_TD7080 = 0.5804369
ARMATURE_TD6070 = 0.3896782
ARMATURE_TD5060 = 0.1142512
ARMATURE_TD4052 = 0.0836482

VR_H3_1_28DOF_ARMATURE = {
    "hip_pitch": ARMATURE_EROB110H100,
    "hip_roll": ARMATURE_EROB110H100,
    "hip_yaw": ARMATURE_EROB90H100,
    "knee_pitch": ARMATURE_EROB110H100,
    "ankle_pitch": ARMATURE_EROB70H100 * 2,
    "ankle_roll": ARMATURE_EROB70H100 * 2,
    "waist_yaw": ARMATURE_TD7080,
    "waist_roll": ARMATURE_TD7080,
    "shoulder_pitch": ARMATURE_TD6070,
    "shoulder_roll": ARMATURE_TD6070,
    "shoulder_yaw": ARMATURE_TD6070,
    "elbow_pitch": ARMATURE_TD6070,
    "wrist_yaw": ARMATURE_TD5060,
    "wrist_roll": ARMATURE_TD4052,
    "wrist_pitch": ARMATURE_TD4052,
}

VR_H3_1_28DOF_EFFORT_LIMITS = {
    "hip_pitch": 369.0,
    "hip_roll": 369.0,
    "hip_yaw": 191.0,
    "knee_pitch": 369.0,
    "ankle_pitch": 140.0,
    "ankle_roll": 140.0,
    "waist_yaw": 102.0,
    "waist_roll": 102.0,
    "shoulder_pitch": 66.0,
    "shoulder_roll": 66.0,
    "shoulder_yaw": 66.0,
    "elbow_pitch": 66.0,
    "wrist_yaw": 34.0,
    "wrist_roll": 11.0,
    "wrist_pitch": 11.0,
}

VR_H3_1_28DOF_SATURATION_EFFORTS = {
    "hip_pitch": 612.0,
    "hip_roll": 612.0,
    "hip_yaw": 321.0,
    "knee_pitch": 612.0,
    "ankle_pitch": 216.0,
    "ankle_roll": 216.0,
    "waist_yaw": 153.0,
    "waist_roll": 153.0,
    "shoulder_pitch": 99.0,
    "shoulder_roll": 99.0,
    "shoulder_yaw": 99.0,
    "elbow_pitch": 99.0,
    "wrist_yaw": 99.0,
    "wrist_roll": 99.0,
    "wrist_pitch": 99.0,
}

VR_H3_1_28DOF_VELOCITY_LIMITS = {
    "hip_pitch": 3.141,
    "hip_roll": 3.141,
    "hip_yaw": 3.141,
    "knee_pitch": 3.141,
    "ankle_pitch": 3.141,
    "ankle_roll": 3.141,
    "waist_yaw": 4.18,
    "waist_roll": 4.18,
    "shoulder_pitch": 3.141,
    "shoulder_roll": 2.356,
    "shoulder_yaw": 2.967,
    "elbow_pitch": 1.571,
    "wrist_yaw": 1.571,
    "wrist_roll": 1.571,
    "wrist_pitch": 1.571,
}

VR_H3_1_28DOF_STIFFNESS = {
    "hip_pitch": 913.0,
    "hip_roll": 906.0,
    "hip_yaw": 155.0,
    "knee_pitch": 561.0,
    "ankle_pitch": 658.0,
    "ankle_roll": 646.0,
    "waist_yaw": 367.0,
    "waist_roll": 367.0,
    "shoulder_pitch": 103.0,
    "shoulder_roll": 94.0,
    "shoulder_yaw": 291.0,
    "elbow_pitch": 291.0,
    "wrist_yaw": 291.0,
    "wrist_roll": 213.0,
    "wrist_pitch": 212.0,
}

VR_H3_1_28DOF_DAMPING = {
    "hip_pitch": 73.0,
    "hip_roll": 72.0,
    "hip_yaw": 12.0,
    "knee_pitch": 45.0,
    "ankle_pitch": 35.0,
    "ankle_roll": 34.0,
    "waist_yaw": 29.0,
    "waist_roll": 29.0,
    "shoulder_pitch": 8.0,
    "shoulder_roll": 7.0,
    "shoulder_yaw": 23.0,
    "elbow_pitch": 23.0,
    "wrist_yaw": 12.0,
    "wrist_roll": 8.0,
    "wrist_pitch": 8.0,
}

VR_H3_1_28DOF_STATIC_FRICTION = {
    "hip_pitch": 19.460412,
    "hip_roll": 11.980386,
    "hip_yaw": 14.677236,
    "knee_pitch": 7.925990,
    "ankle_pitch": 3.882755,
    "ankle_roll": 1.366163,
    "waist_yaw": 0.5,
    "waist_roll": 0.5,
    "shoulder_pitch": 0.3,
    "shoulder_roll": 0.3,
    "shoulder_yaw": 0.3,
    "elbow_pitch": 0.3,
    "wrist_yaw": 0.3,
    "wrist_roll": 0.3,
    "wrist_pitch": 0.3,
}

VR_H3_1_28DOF_DYNAMIC_FRICTION = {
    "hip_pitch": 16.217010,
    "hip_roll": 9.983655,
    "hip_yaw": 12.231030,
    "knee_pitch": 6.604992,
    "ankle_pitch": 3.235630,
    "ankle_roll": 1.138469,
    "waist_yaw": 0.5,
    "waist_roll": 0.5,
    "shoulder_pitch": 0.3,
    "shoulder_roll": 0.3,
    "shoulder_yaw": 0.3,
    "elbow_pitch": 0.3,
    "wrist_yaw": 0.3,
    "wrist_roll": 0.3,
    "wrist_pitch": 0.3,
}

VR_H3_1_28DOF_VISCOUS_FRICTION = {
    "hip_pitch": 16.798800,
    "hip_roll": 25.018775,
    "hip_yaw": 16.996860,
    "knee_pitch": 11.045945,
    "ankle_pitch": 14.933965,
    "ankle_roll": 16.810630,
    "waist_yaw": 0.3,
    "waist_roll": 0.3,
    "shoulder_pitch": 0.3,
    "shoulder_roll": 0.3,
    "shoulder_yaw": 0.3,
    "elbow_pitch": 0.3,
    "wrist_yaw": 0.3,
    "wrist_roll": 0.3,
    "wrist_pitch": 0.3,
}

VR_H3_1_ISAACLAB_JOINTS = ['pelvis', 'left_hip_pitch_link', 'right_hip_pitch_link', 'waist_yaw_link', 'left_hip_roll_link', 'right_hip_roll_link', 'waist_roll_link', 'left_hip_yaw_link', 'right_hip_yaw_link', 'left_shoulder_pitch_link', 'right_shoulder_pitch_link', 'left_knee_pitch_link', 'right_knee_pitch_link', 'left_shoulder_roll_link', 'right_shoulder_roll_link', 'left_ankle_pitch_link', 'right_ankle_pitch_link', 'left_shoulder_yaw_link', 'right_shoulder_yaw_link', 'left_ankle_roll_link', 'right_ankle_roll_link', 'left_elbow_pitch_link', 'right_elbow_pitch_link', 'left_wrist_yaw_link', 'right_wrist_yaw_link', 'left_wrist_roll_link', 'right_wrist_roll_link', 'left_wrist_pitch_link', 'right_wrist_pitch_link']

# Mapping between IsaacLab order and MuJoCo order
VR_H3_1_ISAACLAB_TO_MUJOCO_DOF = [0, 3, 6, 10, 14, 18, 1, 4, 7, 11, 15, 19, 2, 5, 8, 12, 16, 20, 22, 24, 26, 9, 13, 17, 21, 23, 25, 27]
VR_H3_1_MUJOCO_TO_ISAACLAB_DOF = [0, 6, 12, 1, 7, 13, 2, 8, 14, 21, 3, 9, 15, 22, 4, 10, 16, 23, 5, 11, 17, 24, 18, 25, 19, 26, 20, 27]
# H3 tuning 2026-05-05: keep the mapping on the 29-body actuated set used by
# current H3 motion PKLs. The previous list had two duplicate fixed-head entries
# at the end ([6, 6]), which can scramble full-body converter/eval paths.
VR_H3_1_ISAACLAB_TO_MUJOCO_BODY = [0, 1, 4, 7, 11, 15, 19, 2, 5, 8, 12, 16, 20, 3, 6, 9, 13, 17, 21, 23, 25, 27, 10, 14, 18, 22, 24, 26, 28]
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
                ".*_hip_yaw_joint": VR_H3_1_28DOF_EFFORT_LIMITS["hip_yaw"],
                ".*_hip_roll_joint": VR_H3_1_28DOF_EFFORT_LIMITS["hip_roll"],
                ".*_hip_pitch_joint": VR_H3_1_28DOF_EFFORT_LIMITS["hip_pitch"],
                ".*_knee_pitch_joint": VR_H3_1_28DOF_EFFORT_LIMITS["knee_pitch"],
            },
            velocity_limit_sim={
                ".*_hip_yaw_joint": VR_H3_1_28DOF_VELOCITY_LIMITS["hip_yaw"],
                ".*_hip_roll_joint": VR_H3_1_28DOF_VELOCITY_LIMITS["hip_roll"],
                ".*_hip_pitch_joint": VR_H3_1_28DOF_VELOCITY_LIMITS["hip_pitch"],
                ".*_knee_pitch_joint": VR_H3_1_28DOF_VELOCITY_LIMITS["knee_pitch"],
            },
            stiffness={
                ".*_hip_pitch_joint": VR_H3_1_28DOF_STIFFNESS["hip_pitch"],
                ".*_hip_roll_joint": VR_H3_1_28DOF_STIFFNESS["hip_roll"],
                ".*_hip_yaw_joint": VR_H3_1_28DOF_STIFFNESS["hip_yaw"],
                ".*_knee_pitch_joint": VR_H3_1_28DOF_STIFFNESS["knee_pitch"],
            },
            damping={
                ".*_hip_pitch_joint": VR_H3_1_28DOF_DAMPING["hip_pitch"],
                ".*_hip_roll_joint": VR_H3_1_28DOF_DAMPING["hip_roll"],
                ".*_hip_yaw_joint": VR_H3_1_28DOF_DAMPING["hip_yaw"],
                ".*_knee_pitch_joint": VR_H3_1_28DOF_DAMPING["knee_pitch"],
            },
            armature={
                ".*_hip_pitch_joint": VR_H3_1_28DOF_ARMATURE["hip_pitch"],
                ".*_hip_roll_joint": VR_H3_1_28DOF_ARMATURE["hip_roll"],
                ".*_hip_yaw_joint": VR_H3_1_28DOF_ARMATURE["hip_yaw"],
                ".*_knee_pitch_joint": VR_H3_1_28DOF_ARMATURE["knee_pitch"],
            },
        ),
        "feet": ImplicitActuatorCfg(
            joint_names_expr=[".*_ankle_pitch_joint", ".*_ankle_roll_joint"],
            effort_limit_sim=VR_H3_1_28DOF_EFFORT_LIMITS["ankle_pitch"],
            velocity_limit_sim={
                ".*_ankle_pitch_joint": VR_H3_1_28DOF_VELOCITY_LIMITS["ankle_pitch"],
                ".*_ankle_roll_joint": VR_H3_1_28DOF_VELOCITY_LIMITS["ankle_roll"],
            },
            stiffness={
                ".*_ankle_pitch_joint": VR_H3_1_28DOF_STIFFNESS["ankle_pitch"],
                ".*_ankle_roll_joint": VR_H3_1_28DOF_STIFFNESS["ankle_roll"],
            },
            damping={
                ".*_ankle_pitch_joint": VR_H3_1_28DOF_DAMPING["ankle_pitch"],
                ".*_ankle_roll_joint": VR_H3_1_28DOF_DAMPING["ankle_roll"],
            },
            armature=VR_H3_1_28DOF_ARMATURE["ankle_pitch"],
        ),
        "waist": ImplicitActuatorCfg(
            joint_names_expr=["waist_roll_joint", "waist_yaw_joint"],
            effort_limit_sim=VR_H3_1_28DOF_EFFORT_LIMITS["waist_roll"],
            velocity_limit_sim=VR_H3_1_28DOF_VELOCITY_LIMITS["waist_roll"],
            stiffness=VR_H3_1_28DOF_STIFFNESS["waist_roll"],
            damping=VR_H3_1_28DOF_DAMPING["waist_roll"],
            armature=VR_H3_1_28DOF_ARMATURE["waist_roll"],
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
                ".*_shoulder_pitch_joint": VR_H3_1_28DOF_EFFORT_LIMITS["shoulder_pitch"],
                ".*_shoulder_roll_joint": VR_H3_1_28DOF_EFFORT_LIMITS["shoulder_roll"],
                ".*_shoulder_yaw_joint": VR_H3_1_28DOF_EFFORT_LIMITS["shoulder_yaw"],
                ".*_elbow_pitch_joint": VR_H3_1_28DOF_EFFORT_LIMITS["elbow_pitch"],
                ".*_wrist_yaw_joint": VR_H3_1_28DOF_EFFORT_LIMITS["wrist_yaw"],
                ".*_wrist_roll_joint": VR_H3_1_28DOF_EFFORT_LIMITS["wrist_roll"],
                ".*_wrist_pitch_joint": VR_H3_1_28DOF_EFFORT_LIMITS["wrist_pitch"],
            },
            velocity_limit_sim={
                ".*_shoulder_pitch_joint": VR_H3_1_28DOF_VELOCITY_LIMITS["shoulder_pitch"],
                ".*_shoulder_roll_joint": VR_H3_1_28DOF_VELOCITY_LIMITS["shoulder_roll"],
                ".*_shoulder_yaw_joint": VR_H3_1_28DOF_VELOCITY_LIMITS["shoulder_yaw"],
                ".*_elbow_pitch_joint": VR_H3_1_28DOF_VELOCITY_LIMITS["elbow_pitch"],
                ".*_wrist_yaw_joint": VR_H3_1_28DOF_VELOCITY_LIMITS["wrist_yaw"],
                ".*_wrist_roll_joint": VR_H3_1_28DOF_VELOCITY_LIMITS["wrist_roll"],
                ".*_wrist_pitch_joint": VR_H3_1_28DOF_VELOCITY_LIMITS["wrist_pitch"],
            },
            stiffness={
                ".*_shoulder_pitch_joint": VR_H3_1_28DOF_STIFFNESS["shoulder_pitch"],
                ".*_shoulder_roll_joint": VR_H3_1_28DOF_STIFFNESS["shoulder_roll"],
                ".*_shoulder_yaw_joint": VR_H3_1_28DOF_STIFFNESS["shoulder_yaw"],
                ".*_elbow_pitch_joint": VR_H3_1_28DOF_STIFFNESS["elbow_pitch"],
                ".*_wrist_yaw_joint": VR_H3_1_28DOF_STIFFNESS["wrist_yaw"],
                ".*_wrist_roll_joint": VR_H3_1_28DOF_STIFFNESS["wrist_roll"],
                ".*_wrist_pitch_joint": VR_H3_1_28DOF_STIFFNESS["wrist_pitch"],
            },
            damping={
                ".*_shoulder_pitch_joint": VR_H3_1_28DOF_DAMPING["shoulder_pitch"],
                ".*_shoulder_roll_joint": VR_H3_1_28DOF_DAMPING["shoulder_roll"],
                ".*_shoulder_yaw_joint": VR_H3_1_28DOF_DAMPING["shoulder_yaw"],
                ".*_elbow_pitch_joint": VR_H3_1_28DOF_DAMPING["elbow_pitch"],
                ".*_wrist_yaw_joint": VR_H3_1_28DOF_DAMPING["wrist_yaw"],
                ".*_wrist_roll_joint": VR_H3_1_28DOF_DAMPING["wrist_roll"],
                ".*_wrist_pitch_joint": VR_H3_1_28DOF_DAMPING["wrist_pitch"],
            },
            armature={
                ".*_shoulder_pitch_joint": VR_H3_1_28DOF_ARMATURE["shoulder_pitch"],
                ".*_shoulder_roll_joint": VR_H3_1_28DOF_ARMATURE["shoulder_roll"],
                ".*_shoulder_yaw_joint": VR_H3_1_28DOF_ARMATURE["shoulder_yaw"],
                ".*_elbow_pitch_joint": VR_H3_1_28DOF_ARMATURE["elbow_pitch"],
                ".*_wrist_yaw_joint": VR_H3_1_28DOF_ARMATURE["wrist_yaw"],
                ".*_wrist_roll_joint": VR_H3_1_28DOF_ARMATURE["wrist_roll"],
                ".*_wrist_pitch_joint": VR_H3_1_28DOF_ARMATURE["wrist_pitch"],
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
