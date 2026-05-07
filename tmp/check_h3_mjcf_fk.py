import joblib
import mujoco
import numpy as np


XML = "gear_sonic/data/assets/robot_description/mjcf/vr_h3_1_rl.xml"
MOTION = "data/my_robot_motions/robot_filtered/240529/neutral_deep_breath_001__A544.pkl"


def body_id(model, name):
    return mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, name)


def geom_id(model, name):
    return mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, name)


def print_body_z(model, data, names):
    for name in names:
        bid = body_id(model, name)
        print(f"{name:24s} body_z={data.xpos[bid, 2]: .6f} pos={data.xpos[bid]}")


def print_geom_z(model, data, body_name):
    bid = body_id(model, body_name)
    rows = []
    for gid in range(model.ngeom):
        if model.geom_bodyid[gid] == bid:
            rows.append((mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_GEOM, gid), data.geom_xpos[gid, 2]))
    for name, z in rows:
        print(f"  geom {name:36s} center_z={z: .6f}")


motion_all = joblib.load(MOTION)
entry = motion_all[next(iter(motion_all))]
root = np.asarray(entry["root_trans_offset"])
root_rot = np.asarray(entry["root_rot"])
dof = np.asarray(entry["dof"])

model = mujoco.MjModel.from_xml_path(XML)
data = mujoco.MjData(model)

print("model nq/nv/nbody/ngeom", model.nq, model.nv, model.nbody, model.ngeom)
print("motion frames", len(root), "root_z min/max/mean", root[:, 2].min(), root[:, 2].max(), root[:, 2].mean())

body_names = [
    "pelvis",
    "left_ankle_roll_link",
    "right_ankle_roll_link",
    "waist_roll_link",
    "head_yaw_link",
]

for quat_mode in ["xyzw_to_wxyz", "as_wxyz"]:
    data.qpos[:] = 0.0
    data.qpos[:3] = root[0]
    if quat_mode == "xyzw_to_wxyz":
        q = root_rot[0]
        data.qpos[3:7] = [q[3], q[0], q[1], q[2]]
    else:
        data.qpos[3:7] = root_rot[0]
    data.qpos[7:7 + dof.shape[1]] = dof[0]
    mujoco.mj_forward(model, data)
    print("\nframe0", quat_mode, "root", root[0], "root_rot", root_rot[0])
    print_body_z(model, data, body_names)
    print("left ankle geoms")
    print_geom_z(model, data, "left_ankle_roll_link")
    print("right ankle geoms")
    print_geom_z(model, data, "right_ankle_roll_link")

    min_geom_z = np.inf
    min_geom = None
    for gid in range(model.ngeom):
        z = data.geom_xpos[gid, 2]
        if z < min_geom_z:
            min_geom_z = z
            min_geom = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_GEOM, gid)
    print("lowest geom center", min_geom, min_geom_z)

print("\nstanding init from vr_h3_1.py")
init = {
    "left_hip_pitch_joint": -0.2,
    "left_hip_roll_joint": 0.0,
    "left_hip_yaw_joint": 0.0,
    "left_knee_pitch_joint": 0.4,
    "left_ankle_pitch_joint": -0.2,
    "left_ankle_roll_joint": 0.0,
    "right_hip_pitch_joint": -0.2,
    "right_hip_roll_joint": 0.0,
    "right_hip_yaw_joint": 0.0,
    "right_knee_pitch_joint": 0.4,
    "right_ankle_pitch_joint": -0.2,
    "right_ankle_roll_joint": 0.0,
    "waist_yaw_joint": 0.0,
    "waist_roll_joint": 0.0,
    "left_shoulder_pitch_joint": 0.0,
    "left_shoulder_roll_joint": 0.2,
    "left_shoulder_yaw_joint": 0.0,
    "left_elbow_pitch_joint": 1.0,
    "left_wrist_yaw_joint": 0.0,
    "left_wrist_roll_joint": 0.0,
    "left_wrist_pitch_joint": 0.0,
    "right_shoulder_pitch_joint": 0.0,
    "right_shoulder_roll_joint": -0.2,
    "right_shoulder_yaw_joint": 0.0,
    "right_elbow_pitch_joint": 1.0,
    "right_wrist_yaw_joint": 0.0,
    "right_wrist_roll_joint": 0.0,
    "right_wrist_pitch_joint": 0.0,
}
data.qpos[:] = 0.0
data.qpos[:3] = [0, 0, 0.85]
data.qpos[3:7] = [1, 0, 0, 0]
for name, val in init.items():
    jid = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, name)
    qadr = model.jnt_qposadr[jid]
    data.qpos[qadr] = val
mujoco.mj_forward(model, data)
print_body_z(model, data, body_names)
print("left ankle geoms")
print_geom_z(model, data, "left_ankle_roll_link")
print("right ankle geoms")
print_geom_z(model, data, "right_ankle_roll_link")
