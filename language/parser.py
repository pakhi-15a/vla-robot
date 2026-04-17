def parse_command(command):
    command = command.lower()

    result = {
        "action": "move",
        "object": None,
        "target": None,
        "relation": None
    }

    if "throw" in command or "toss" in command:
        result["action"] = "throw"

    if "drop" in command or "release" in command:
        result["action"] = "drop"

    color_map = {
        "blue": "blue_cube",
        "green": "green_cube",
        "red": "red_sphere",
        "pink": "pink_sphere",
        "orange": "orange_cylinder",
        "yellow": "yellow_cylinder",
    }

    mentions = []
    for color, obj_name in color_map.items():
        index = command.find(color)
        if index != -1:
            mentions.append((index, obj_name, color))

    mentions.sort(key=lambda item: item[0])

    if mentions:
        result["object"] = mentions[0][1]

    if len(mentions) > 1:
        result["target"] = mentions[1][1]

    if "on top of" in command or "on top" in command:
        result["relation"] = "on_top_of"

    if "in front of" in command or "in front" in command:
        result["relation"] = "in_front_of"

    if "behind" in command:
        result["relation"] = "behind"

    if "above" in command:
        result["relation"] = "above"

    if "below" in command:
        result["relation"] = "below"

    if "near" in command or "next to" in command:
        result["relation"] = "near"

    if "far" in command or "far from" in command:
        result["relation"] = "far"

    if "right" in command:
        result["relation"] = "right"

    if "left" in command:
        result["relation"] = "left"

    if result["action"] == "move":
        if result["object"] in ("blue_cube", "green_cube") and not result["target"]:
            result["target"] = "green_cube" if result["object"] == "blue_cube" else "blue_cube"

        if result["target"] in ("blue_cube", "green_cube") and not result["object"]:
            result["object"] = "blue_cube" if result["target"] == "green_cube" else "green_cube"

    return result