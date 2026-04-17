import pybullet as p

def get_object_positions(objects):
    positions = {}
    for name, obj_id in objects.items():
        pos, _ = p.getBasePositionAndOrientation(obj_id)
        positions[name] = pos
    return positions