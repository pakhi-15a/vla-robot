def compute_target_position(obj_positions, parsed_cmd):
    target_pos = obj_positions[parsed_cmd["target"]]

    offset = 0.2

    if parsed_cmd["relation"] == "right":
        return [target_pos[0] + offset, target_pos[1], target_pos[2]]

    return target_pos