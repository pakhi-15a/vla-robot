import pybullet as p
import pybullet_data
import time

def setup_env():
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    p.setGravity(0, 0, -9.8)

    plane = p.loadURDF("plane.urdf")

    robot = p.loadURDF("kuka_iiwa/model.urdf", [0, 0, 0])

    # Add objects
    cube1 = p.loadURDF("cube_small.urdf", [0.5, 0, 0.05])
    cube2 = p.loadURDF("cube_small.urdf", [0.7, 0.2, 0.05])

    return robot, cube1, cube2