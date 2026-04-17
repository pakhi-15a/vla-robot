from simulation.env import setup_env
from perception.detect import get_object_positions
from language.parser import parse_command
from planning.planner import compute_target_position
from control.robot import move_object, drop_object, throw_object
from language.speechinput import get_voice_command

import pybullet as p
import time


def main():
    print("🚀 Starting VLA Robot System...")

    # Setup simulation
    robot, objects, scene = setup_env()

    time.sleep(2)

    # Get command from voice
    print("🎤 Initializing voice input...")
    command = get_voice_command()

    # Fallback to typing if voice fails
    if not command:
        print("⚠️ Voice input failed. Switching to manual input.")
        command = input("Type your command: ")

    print(f"📝 Command received: {command}")

    # Parse command
    parsed = parse_command(command)

    if not parsed or not parsed.get("object"):
        print("❌ Could not understand command properly.")
        return

    if parsed.get("action") == "move":
        if not parsed.get("target"):
            print("❌ Move command missing a target.")
            return

        positions = get_object_positions(objects)
        target_pos = compute_target_position(positions, parsed)

        print(f"📍 Moving {parsed['object']} to {parsed['relation']} of {parsed['target']}")
        move_object(robot, objects[parsed["object"]], target_pos, scene)

    if parsed.get("action") == "drop":
        print(f"📍 Dropping {parsed['object']} off the table")
        drop_object(robot, objects[parsed["object"]], scene)

    if parsed.get("action") == "throw":
        print(f"📍 Throwing {parsed['object']} away from the table")
        throw_object(robot, objects[parsed["object"]], scene)

    print("✅ Task completed!")

    while True:
        p.stepSimulation()
        time.sleep(1 / 240)


if __name__ == "__main__":
    main()