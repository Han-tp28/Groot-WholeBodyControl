from typing import Dict
import tyro
from gear_sonic.utils.mujoco_sim.simulator_factory import SimulatorFactory, init_channel
from gear_sonic.utils.mujoco_sim.configs import SimLoopConfig
from gear_sonic.data.robot_model.instantiation import instantiate_g1_robot_model
from gear_sonic.data.robot_model.robot_model import RobotModel

def main():
    config = tyro.cli(SimLoopConfig, args=["--robot", "g1", "--interface", "lo"])
    wbc_config = config.load_wbc_yaml()
    wbc_config["ENV_NAME"] = config.env_name
    
    # 1. Test before instantiate
    # init_channel(config=wbc_config)
    
    robot_model = instantiate_g1_robot_model()
    
    print("Calling init_channel")
    init_channel(config=wbc_config)
    print("init_channel succeeded")
    
    sim = SimulatorFactory.create_simulator(
        config=wbc_config,
        env_name=config.env_name,
    )
    print("Success")

if __name__ == "__main__":
    main()
