def parse_command(command):
    command = command.lower()

    result = {
        "action": "move",
        "object": None,
        "target": None,
        "relation": None
    }

    if "blue" in command:
        result["object"] = "blue_cube"

    if "green" in command:
        result["target"] = "green_cube"

    if "right" in command:
        result["relation"] = "right"

    return result