import argparse
from isaaclab.app import AppLauncher
parser = argparse.ArgumentParser()
app_launcher = AppLauncher({"headless": True})
app_launcher.add_app_launcher_args(parser)
simulation_app = app_launcher.app

import torch
import isaaclab.sim as sim_utils
from isaaclab.assets import Articulation
from gear_sonic.envs.manager_env.robots.vr_h3_1 import VR_H3_1_CFG

sim_cfg = sim_utils.SimulationCfg()
sim = sim_utils.SimulationContext(sim_cfg)
robot = Articulation(VR_H3_1_CFG.replace(prim_path="/World/Robot"))
sim.reset()
print("BODY NAMES:", robot.data.body_names)
print("NUM BODIES:", len(robot.data.body_names))
print("JOINT NAMES:", robot.data.joint_names)
print("NUM JOINTS:", len(robot.data.joint_names))
simulation_app.close()
