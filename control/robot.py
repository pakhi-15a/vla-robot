import pybullet as p
import time

def move_object(obj_id, target_pos):
    p.resetBasePositionAndOrientation(obj_id, target_pos, [0,0,0,1])

    for _ in range(100):
        p.stepSimulation()
        time.sleep(1/240)