"""VR H3-1 supplemental info: actuated joints, groups, limits, and defaults."""

from dataclasses import dataclass
from enum import Enum

import numpy as np

from gear_sonic.data.robot_model.supplemental_info.robot_supplemental_info import (
    RobotSupplementalInfo,
)


class WaistLocation(Enum):
    """Enum for waist location configuration."""

    LOWER_BODY = "lower_body"
    UPPER_BODY = "upper_body"
    LOWER_AND_UPPER_BODY = "lower_and_upper_body"


@dataclass
class VRH31SupplementalInfo(RobotSupplementalInfo):
    """Supplemental information for the VR H3-1 28-DOF body model."""

    def __init__(
        self,
        waist_location: WaistLocation = WaistLocation.LOWER_BODY,
    ):
        body_actuated_joints = [
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

        joint_limits = {
            "left_hip_pitch_joint": [-1.571, 0.436],
            "left_hip_roll_joint": [-0.175, 1.047],
            "left_hip_yaw_joint": [-0.785, 0.785],
            "left_knee_pitch_joint": [-0.175, 2.094],
            "left_ankle_pitch_joint": [-0.873, 0.524],
            "left_ankle_roll_joint": [-0.262, 0.262],
            "right_hip_pitch_joint": [-1.571, 0.436],
            "right_hip_roll_joint": [-1.047, 0.175],
            "right_hip_yaw_joint": [-0.785, 0.785],
            "right_knee_pitch_joint": [-0.175, 2.094],
            "right_ankle_pitch_joint": [-0.873, 0.524],
            "right_ankle_roll_joint": [-0.262, 0.262],
            "waist_yaw_joint": [-2.618, 2.618],
            "waist_roll_joint": [-0.262, 0.262],
            "left_shoulder_pitch_joint": [-3.14, 1.047],
            "left_shoulder_roll_joint": [0.0, 2.356],
            "left_shoulder_yaw_joint": [-2.967, 2.967],
            "left_elbow_pitch_joint": [-0.524, 1.571],
            "left_wrist_yaw_joint": [-2.967, 2.967],
            "left_wrist_roll_joint": [-1.134, 0.698],
            "left_wrist_pitch_joint": [-0.96, 0.96],
            "right_shoulder_pitch_joint": [-3.14, 1.047],
            "right_shoulder_roll_joint": [-2.356, 0.0],
            "right_shoulder_yaw_joint": [-2.967, 2.967],
            "right_elbow_pitch_joint": [-0.524, 1.571],
            "right_wrist_yaw_joint": [-2.967, 2.967],
            "right_wrist_roll_joint": [-0.698, 1.134],
            "right_wrist_pitch_joint": [-0.96, 0.96],
        }

        joint_groups = {
            "waist": {"joints": ["waist_yaw_joint", "waist_roll_joint"], "groups": []},
            "left_leg": {
                "joints": [
                    "left_hip_pitch_joint",
                    "left_hip_roll_joint",
                    "left_hip_yaw_joint",
                    "left_knee_pitch_joint",
                    "left_ankle_pitch_joint",
                    "left_ankle_roll_joint",
                ],
                "groups": [],
            },
            "right_leg": {
                "joints": [
                    "right_hip_pitch_joint",
                    "right_hip_roll_joint",
                    "right_hip_yaw_joint",
                    "right_knee_pitch_joint",
                    "right_ankle_pitch_joint",
                    "right_ankle_roll_joint",
                ],
                "groups": [],
            },
            "legs": {"joints": [], "groups": ["left_leg", "right_leg"]},
            "left_arm": {
                "joints": [
                    "left_shoulder_pitch_joint",
                    "left_shoulder_roll_joint",
                    "left_shoulder_yaw_joint",
                    "left_elbow_pitch_joint",
                    "left_wrist_yaw_joint",
                    "left_wrist_roll_joint",
                    "left_wrist_pitch_joint",
                ],
                "groups": [],
            },
            "right_arm": {
                "joints": [
                    "right_shoulder_pitch_joint",
                    "right_shoulder_roll_joint",
                    "right_shoulder_yaw_joint",
                    "right_elbow_pitch_joint",
                    "right_wrist_yaw_joint",
                    "right_wrist_roll_joint",
                    "right_wrist_pitch_joint",
                ],
                "groups": [],
            },
            "arms": {"joints": [], "groups": ["left_arm", "right_arm"]},
            "hands": {"joints": [], "groups": []},
            "lower_body": {"joints": [], "groups": ["waist", "legs"]},
            "upper_body_no_hands": {"joints": [], "groups": ["arms"]},
            "body": {"joints": [], "groups": ["lower_body", "upper_body_no_hands"]},
            "upper_body": {"joints": [], "groups": ["upper_body_no_hands"]},
        }

        modified_joint_groups = joint_groups.copy()
        if waist_location == WaistLocation.UPPER_BODY:
            modified_joint_groups["lower_body"] = {"joints": [], "groups": ["legs"]}
            modified_joint_groups["upper_body_no_hands"] = {
                "joints": [],
                "groups": ["arms", "waist"],
            }
        elif waist_location == WaistLocation.LOWER_AND_UPPER_BODY:
            modified_joint_groups["upper_body_no_hands"] = {
                "joints": [],
                "groups": ["arms", "waist"],
            }

        joint_name_mapping = {
            "waist_roll": "waist_roll_joint",
            "waist_yaw": "waist_yaw_joint",
            "shoulder_pitch": {
                "left": "left_shoulder_pitch_joint",
                "right": "right_shoulder_pitch_joint",
            },
            "shoulder_roll": {
                "left": "left_shoulder_roll_joint",
                "right": "right_shoulder_roll_joint",
            },
            "shoulder_yaw": {
                "left": "left_shoulder_yaw_joint",
                "right": "right_shoulder_yaw_joint",
            },
            "elbow_pitch": {
                "left": "left_elbow_pitch_joint",
                "right": "right_elbow_pitch_joint",
            },
            "wrist_yaw": {"left": "left_wrist_yaw_joint", "right": "right_wrist_yaw_joint"},
            "wrist_roll": {"left": "left_wrist_roll_joint", "right": "right_wrist_roll_joint"},
            "wrist_pitch": {
                "left": "left_wrist_pitch_joint",
                "right": "right_wrist_pitch_joint",
            },
        }

        default_joint_q = {
            "shoulder_roll": {"left": 0.2, "right": -0.2},
            "elbow_pitch": {"left": 1.0, "right": 1.0},
        }

        super().__init__(
            name="VR_H3_1",
            body_actuated_joints=body_actuated_joints,
            left_hand_actuated_joints=[],
            right_hand_actuated_joints=[],
            joint_limits=joint_limits,
            joint_groups=modified_joint_groups,
            root_frame_name="pelvis",
            hand_frame_names={"left": "left_wrist_pitch_link", "right": "right_wrist_pitch_link"},
            calibration_joint_q={"elbow_pitch": {"left": 0.0, "right": 0.0}},
            joint_name_mapping=joint_name_mapping,
            hand_rotation_correction=np.eye(3),
            default_joint_q=default_joint_q,
            teleop_upper_body_motion_scale=1.0,
        )
