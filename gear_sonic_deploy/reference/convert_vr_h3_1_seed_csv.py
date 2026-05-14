#!/usr/bin/env python3
"""Convert flat VR_H3_1 seed CSV motions to the deploy reference layout."""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def quat_from_xyz_degrees(rx: float, ry: float, rz: float) -> tuple[float, float, float, float]:
    """Return wxyz quaternion from XYZ Euler angles in degrees."""
    x = math.radians(rx) * 0.5
    y = math.radians(ry) * 0.5
    z = math.radians(rz) * 0.5

    cx, sx = math.cos(x), math.sin(x)
    cy, sy = math.cos(y), math.sin(y)
    cz, sz = math.cos(z), math.sin(z)

    # q = qz * qy * qx, matching roll/pitch/yaw style XYZ input columns.
    w = cz * cy * cx + sz * sy * sx
    qx = cz * cy * sx - sz * sy * cx
    qy = cz * sy * cx + sz * cy * sx
    qz = sz * cy * cx - cz * sy * sx
    return (w, qx, qy, qz)


def write_csv(path: Path, headers: list[str], rows: list[list[float]]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def centered_velocity(values: list[list[float]], fps: float) -> list[list[float]]:
    if not values:
        return []

    velocities: list[list[float]] = []
    n = len(values)
    dims = len(values[0])
    for i in range(n):
        i0 = max(i - 1, 0)
        i1 = min(i + 1, n - 1)
        dt = max(i1 - i0, 1)
        velocities.append([(values[i1][j] - values[i0][j]) * fps / dt for j in range(dims)])
    return velocities


def convert_file(src: Path, dst_root: Path, fps: float, translate_scale: float, overwrite: bool) -> bool:
    motion_name = src.stem
    dst = dst_root / motion_name
    if dst.exists() and not overwrite:
        return False

    with src.open(newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        joint_columns = [name for name in fieldnames if name.endswith("_dof")]
        required = [
            "root_translateX",
            "root_translateY",
            "root_translateZ",
            "root_rotateX",
            "root_rotateY",
            "root_rotateZ",
        ]
        missing = [name for name in required if name not in fieldnames]
        if missing:
            raise ValueError(f"{src}: missing required columns {missing}")
        if len(joint_columns) != 28:
            raise ValueError(f"{src}: expected 28 *_dof columns, got {len(joint_columns)}")

        joint_pos: list[list[float]] = []
        body_pos: list[list[float]] = []
        body_quat: list[list[float]] = []

        for row in reader:
            joint_pos.append([math.radians(float(row[name])) for name in joint_columns])
            body_pos.append(
                [
                    float(row["root_translateX"]) * translate_scale,
                    float(row["root_translateY"]) * translate_scale,
                    float(row["root_translateZ"]) * translate_scale,
                ]
            )
            body_quat.append(
                list(
                    quat_from_xyz_degrees(
                        float(row["root_rotateX"]),
                        float(row["root_rotateY"]),
                        float(row["root_rotateZ"]),
                    )
                )
            )

    if not joint_pos:
        raise ValueError(f"{src}: no frames")

    joint_vel = centered_velocity(joint_pos, fps)
    body_lin_vel = centered_velocity(body_pos, fps)
    body_ang_vel = [[0.0, 0.0, 0.0] for _ in body_quat]

    dst.mkdir(parents=True, exist_ok=True)
    write_csv(dst / "joint_pos.csv", [f"joint_{i}" for i in range(28)], joint_pos)
    write_csv(dst / "joint_vel.csv", [f"joint_vel_{i}" for i in range(28)], joint_vel)
    write_csv(dst / "body_pos.csv", ["body_0_x", "body_0_y", "body_0_z"], body_pos)
    write_csv(dst / "body_quat.csv", ["body_0_w", "body_0_x", "body_0_y", "body_0_z"], body_quat)
    write_csv(dst / "body_lin_vel.csv", ["body_0_vel_x", "body_0_vel_y", "body_0_vel_z"], body_lin_vel)
    write_csv(dst / "body_ang_vel.csv", ["body_0_angvel_x", "body_0_angvel_y", "body_0_angvel_z"], body_ang_vel)

    with (dst / "metadata.txt").open("w") as f:
        f.write(f"Metadata for: {motion_name}\n")
        f.write("==============================\n\n")
        f.write("Body part indexes:\n")
        f.write("[0]\n\n")
        f.write(f"Total timesteps: {len(joint_pos)}\n\n")
        f.write("Data arrays summary:\n")
        f.write(f"  joint_pos: ({len(joint_pos)}, 28)\n")
        f.write(f"  joint_vel: ({len(joint_vel)}, 28)\n")
        f.write(f"  body_pos_w: ({len(body_pos)}, 1, 3)\n")
        f.write(f"  body_quat_w: ({len(body_quat)}, 1, 4)\n")

    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Raw seed CSV directory, e.g. /home/han/seed/vr_h3_1/221125")
    parser.add_argument("output", type=Path, help="Deploy reference output directory")
    parser.add_argument("--fps", type=float, default=50.0)
    parser.add_argument("--translate-scale", type=float, default=0.01, help="Scale root translations; seed files appear to use centimeters")
    parser.add_argument("--limit", type=int, default=0, help="Convert only the first N files after sorting")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    files = sorted(args.source.glob("*.csv"))
    if args.limit:
        files = files[: args.limit]
    if not files:
        raise SystemExit(f"No CSV files found in {args.source}")

    args.output.mkdir(parents=True, exist_ok=True)
    converted = 0
    for src in files:
        if convert_file(src, args.output, args.fps, args.translate_scale, args.overwrite):
            converted += 1

    print(f"Converted {converted}/{len(files)} motions to {args.output}")


if __name__ == "__main__":
    main()
