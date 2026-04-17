import pybullet as p
import time

def _get_end_effector_index(robot_id):
    return p.getNumJoints(robot_id) - 1

def _move_end_effector(robot_id, target_pos, steps=180, force=200):
    ee_index = _get_end_effector_index(robot_id)
    joint_count = p.getNumJoints(robot_id)

    joint_positions = p.calculateInverseKinematics(robot_id, ee_index, target_pos)
    p.setJointMotorControlArray(
        robot_id,
        list(range(joint_count)),
        p.POSITION_CONTROL,
        targetPositions=joint_positions,
        forces=[force] * joint_count,
    )

    for _ in range(steps):
        p.stepSimulation()
        time.sleep(1 / 240)

def _attach_object(robot_id, obj_id):
    obj_pos, _ = p.getBasePositionAndOrientation(obj_id)

    pre_grasp = [obj_pos[0], obj_pos[1], obj_pos[2] + 0.2]
    grasp = [obj_pos[0], obj_pos[1], obj_pos[2] + 0.05]

    _move_end_effector(robot_id, pre_grasp)
    _move_end_effector(robot_id, grasp)

    ee_index = _get_end_effector_index(robot_id)
    constraint_id = p.createConstraint(
        robot_id,
        ee_index,
        obj_id,
        -1,
        p.JOINT_FIXED,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    )

    return obj_pos, constraint_id

def move_object(robot_id, obj_id, target_pos, scene):
    obj_pos, constraint_id = _attach_object(robot_id, obj_id)

    lift = [obj_pos[0], obj_pos[1], obj_pos[2] + 0.3]
    place_above = [target_pos[0], target_pos[1], target_pos[2] + 0.2]
    place = [target_pos[0], target_pos[1], target_pos[2] + 0.05]

    _move_end_effector(robot_id, lift)
    _move_end_effector(robot_id, place_above)
    _move_end_effector(robot_id, place)

    p.removeConstraint(constraint_id)
    _move_end_effector(robot_id, place_above)

def drop_object(robot_id, obj_id, scene):
    obj_pos, constraint_id = _attach_object(robot_id, obj_id)

    table_pos = scene["table_pos"]
    table_top_z = scene["table_top_z"]

    lift = [obj_pos[0], obj_pos[1], obj_pos[2] + 0.3]
    drop_above = [table_pos[0] + 0.7, table_pos[1], table_top_z + 0.35]

    _move_end_effector(robot_id, lift)
    _move_end_effector(robot_id, drop_above)

    p.removeConstraint(constraint_id)

    for _ in range(240):
        p.stepSimulation()
        time.sleep(1 / 240)

def throw_object(robot_id, obj_id, scene):
    obj_pos, constraint_id = _attach_object(robot_id, obj_id)

    table_pos = scene["table_pos"]
    table_top_z = scene["table_top_z"]

    lift = [obj_pos[0], obj_pos[1], obj_pos[2] + 0.3]
    throw_pose = [table_pos[0] + 0.3, table_pos[1], table_top_z + 0.45]

    _move_end_effector(robot_id, lift)
    _move_end_effector(robot_id, throw_pose)

    p.removeConstraint(constraint_id)
    p.resetBaseVelocity(obj_id, linearVelocity=[4.0, 0.0, 1.0])

    for _ in range(360):
        p.stepSimulation()
        time.sleep(1 / 240)