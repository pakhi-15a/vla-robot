from simulation.env import setup_env
from perception.detect import get_object_positions
from language.parser import parse_command
from planning.planner import compute_target_position
from control.robot import move_object

import time

robot, cube1, cube2 = setup_env()

objects = {
    "blue_cube": cube1,
    "green_cube": cube2
}

time.sleep(2)

command = "Move blue cube to the right of green cube"

parsed = parse_command(command)

positions = get_object_positions(objects)

target_pos = compute_target_position(positions, parsed)

move_object(objects[parsed["object"]], target_pos)