def compute_target_position(obj_positions, parsed_cmd):
    target_pos = obj_positions[parsed_cmd["target"]]

    offset_xy = 0.2
    offset_z = 0.2

    relation = parsed_cmd.get("relation")

    if relation == "right":
        return [target_pos[0] + offset_xy, target_pos[1], target_pos[2]]

    if relation == "left":
        return [target_pos[0] - offset_xy, target_pos[1], target_pos[2]]

    if relation == "in_front_of":
        return [target_pos[0], target_pos[1] + offset_xy, target_pos[2]]

    if relation == "behind":
        return [target_pos[0], target_pos[1] - offset_xy, target_pos[2]]

    if relation == "above":
        return [target_pos[0], target_pos[1], target_pos[2] + offset_z]

    if relation == "below":
        return [target_pos[0], target_pos[1], target_pos[2] - offset_z]

    if relation == "on_top_of":
        return [target_pos[0], target_pos[1], target_pos[2] + offset_z]

    if relation == "near":
        return [target_pos[0] + 0.1, target_pos[1], target_pos[2]]

    if relation == "far":
        return [target_pos[0] + 0.5, target_pos[1], target_pos[2]]

    return target_pos