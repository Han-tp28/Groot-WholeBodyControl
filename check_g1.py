import argparse
from isaaclab.app import AppLauncher
parser = argparse.ArgumentParser()
app_launcher = AppLauncher({"headless": True})
app_launcher.add_app_launcher_args(parser)
simulation_app = app_launcher.app

import isaaclab.sim as sim_utils
from isaaclab.assets import Articulation
from gear_sonic.envs.manager_env.robots.g1 import G1_CYLINDER_MODEL_12_DEX_CFG

sim_cfg = sim_utils.SimulationCfg()
sim = sim_utils.SimulationContext(sim_cfg)
robot = Articulation(G1_CYLINDER_MODEL_12_DEX_CFG.replace(prim_path="/World/Robot"))
sim.reset()
print("G1 BODY NAMES:", robot.data.body_names)
print("G1 JOINT NAMES:", robot.data.joint_names)
simulation_app.close()
