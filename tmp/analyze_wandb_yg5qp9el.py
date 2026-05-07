from pathlib import Path

import pandas as pd


path = Path("/home/hantp/Groot-WholeBodyControl/tmp/wandb_yg5qp9el/history.csv")
df = pd.read_csv(path)

metrics = [
    "_step",
    "Train/mean_reward",
    "Train/mean_episode_length",
    "Train/mean_action_noise_std",
    "Train/mean_entropy",
    "Env/Episode_Termination/time_out",
    "Env/Episode_Termination/anchor_pos",
    "Env/Episode_Termination/anchor_ori_full",
    "Env/Episode_Termination/ee_body_pos",
    "Env/Episode_Termination/foot_pos_xyz",
    "Env/Metrics/motion/error_anchor_pos",
    "Env/Metrics/motion/error_anchor_rot",
    "Env/Metrics/motion/error_body_pos",
    "Env/Metrics/motion/error_body_rot",
    "Env/Metrics/motion/error_joint_pos",
    "Env/Metrics/motion/error_joint_vel",
    "Env/Metrics/motion/error_body_ang_vel",
    "Env/Episode_Reward/tracking_vr_5point_local",
    "Env/Episode_Reward/tracking_relative_body_pos",
    "Env/Episode_Reward/action_rate_l2",
    "Env/Episode_Reward/feet_acc",
    "Env/adp_samp/failure_rate_mean",
    "Env/adp_samp/effective_num_bins",
]
present = [m for m in metrics if m in df.columns]

print("rows", len(df), "step_min", df["_step"].min(), "step_max", df["_step"].max())
print("present_metrics")
for m in present:
    print(" ", m)

def last_valid(col):
    s = df[["_step", col]].dropna()
    if s.empty:
        return None
    return s.iloc[-1]

print("\nlatest")
for m in present:
    if m == "_step":
        continue
    row = last_valid(m)
    if row is not None:
        print(f"{m}: step={int(row['_step'])} value={row[m]:.6g}")

print("\nwindows")
windows = [(0, 1000), (1000, 5000), (5000, 10000), (10000, 15000), (15000, 20000), (20000, 10**9)]
window_metrics = [m for m in present if m != "_step"]
for lo, hi in windows:
    w = df[(df["_step"] >= lo) & (df["_step"] < hi)]
    if w.empty:
        continue
    print(f"\nstep [{lo},{hi}) rows={len(w)}")
    for m in window_metrics:
        s = w[m].dropna()
        if not s.empty:
            print(f"  {m}: mean={s.mean():.5g} last={s.iloc[-1]:.5g}")

print("\ncolumns_matching")
for token in ["Termination", "mean", "Metrics/motion", "Episode_Reward"]:
    cols = [c for c in df.columns if token in c]
    print(token, len(cols))
    print(cols[:80])
