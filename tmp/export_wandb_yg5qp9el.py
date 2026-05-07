import csv
import json
from pathlib import Path

import wandb


OUT_DIR = Path("/home/hantp/Groot-WholeBodyControl/tmp/wandb_yg5qp9el")
OUT_DIR.mkdir(parents=True, exist_ok=True)

api = wandb.Api(timeout=60)
run = api.run("/tranphuchan02-hust/TRL_VR_H3_1_Track/runs/yg5qp9el")

with open(OUT_DIR / "summary.json", "w") as f:
    json.dump(dict(run.summary), f, indent=2, default=str)

with open(OUT_DIR / "config.json", "w") as f:
    json.dump(dict(run.config), f, indent=2, default=str)

with open(OUT_DIR / "run_info.json", "w") as f:
    json.dump(
        {
            "id": run.id,
            "name": run.name,
            "state": run.state,
            "url": run.url,
            "created_at": str(run.created_at),
            "updated_at": str(getattr(run, "updated_at", "")),
        },
        f,
        indent=2,
        default=str,
    )

rows = []
keys = set()
for row in run.scan_history(page_size=1000):
    rows.append(row)
    keys.update(row.keys())

priority = ["_step", "_timestamp", "_runtime"]
fieldnames = priority + sorted(k for k in keys if k not in priority)
with open(OUT_DIR / "history.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)

print(OUT_DIR)
print("run", run.name, run.state, run.url)
print("rows", len(rows), "cols", len(fieldnames))
