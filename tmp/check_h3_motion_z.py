import joblib
import numpy as np


ROBOT_PATH = "data/my_robot_motions/robot_filtered/240529/neutral_deep_breath_001__A544.pkl"
SMPL_PATH = "data/smpl_filtered/neutral_deep_breath_001__A544.pkl"


def describe_array(name, value):
    arr = np.asarray(value)
    print(f"{name}: shape={arr.shape} dtype={arr.dtype}")
    if arr.size and np.issubdtype(arr.dtype, np.number):
        flat = arr.reshape(-1)
        print(
            f"  min={np.nanmin(flat):.6g} max={np.nanmax(flat):.6g} "
            f"mean={np.nanmean(flat):.6g}"
        )


def describe_entry(label, entry):
    print(f"\n== {label} ==")
    print("type", type(entry))
    if not isinstance(entry, dict):
        return
    print("keys", list(entry.keys()))
    for key in [
        "root_trans_offset",
        "root_rot",
        "pose_aa",
        "dof",
        "body_pos_w",
        "body_quat_w",
        "fps",
    ]:
        if key in entry:
            describe_array(key, entry[key])

    body_pos = entry.get("body_pos_w")
    if body_pos is not None:
        body_pos = np.asarray(body_pos)
        print("body z stats by index")
        for idx in range(min(body_pos.shape[1], 14)):
            z = body_pos[:, idx, 2]
            print(
                f"  body[{idx:02d}] z min={z.min():.4f} max={z.max():.4f} "
                f"mean={z.mean():.4f} first={z[0]:.4f}"
            )
    root = entry.get("root_trans_offset")
    if root is not None:
        root = np.asarray(root)
        print(
            "root z first/min/max/mean",
            root[0, 2],
            root[:, 2].min(),
            root[:, 2].max(),
            root[:, 2].mean(),
        )


for label, path in [("robot", ROBOT_PATH), ("smpl", SMPL_PATH)]:
    data = joblib.load(path)
    print(f"\nFILE {label}: {path}")
    print("loaded", type(data))
    if isinstance(data, dict):
        print("top keys", list(data.keys())[:20])
        if all(isinstance(v, dict) for v in data.values()):
            print("dict of motions", len(data))
            first_key = next(iter(data))
            print("first motion key", first_key)
            describe_entry(label + "/" + first_key, data[first_key])
        else:
            describe_entry(label, data)
    else:
        describe_entry(label, data)
