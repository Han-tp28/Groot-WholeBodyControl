"""Factory function to instantiate a configured VR H3-1 RobotModel from URDF."""

from pathlib import Path
from typing import Literal

from gear_sonic.data.robot_model.robot_model import RobotModel
from gear_sonic.data.robot_model.supplemental_info.vr_h3_1.vr_h3_1_supplemental_info import (
    VRH31SupplementalInfo,
    WaistLocation,
)


def instantiate_vr_h3_1_robot_model(
    waist_location: Literal["lower_body", "upper_body", "lower_and_upper_body"] = "lower_body",
):
    """Instantiate a VR H3-1 robot model."""
    asset_dir = Path(__file__).resolve().parents[2] / "assets" / "robot_description"
    urdf_path = asset_dir / "urdf" / "vr_h3_1" / "vr_h3_1_rl_28_dof.urdf"

    assert waist_location in [
        "lower_body",
        "upper_body",
        "lower_and_upper_body",
    ], f"Invalid waist_location: {waist_location}"

    waist_location_enum = {
        "lower_body": WaistLocation.LOWER_BODY,
        "upper_body": WaistLocation.UPPER_BODY,
        "lower_and_upper_body": WaistLocation.LOWER_AND_UPPER_BODY,
    }[waist_location]

    return RobotModel(
        str(urdf_path),
        str(asset_dir),
        supplemental_info=VRH31SupplementalInfo(waist_location=waist_location_enum),
    )
