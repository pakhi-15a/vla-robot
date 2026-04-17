import pybullet as p
import pybullet_data
import time

def setup_env():
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    p.setGravity(0, 0, -9.8)

    plane = p.loadURDF("plane.urdf")

    table_pos = [0.5, 0.0, 0.0]
    table_scale = 1.6
    table = p.loadURDF("table/table.urdf", table_pos, globalScaling=table_scale)
    table_top_z = 0.62 * table_scale

    robot = p.loadURDF("kuka_iiwa/model.urdf", [table_pos[0], table_pos[1], table_top_z])

    # Add objects
    spread_x = 0.35 * table_scale
    spread_y = 0.22 * table_scale

    cube_half = 0.05 * 3.0
    cube1 = p.loadURDF(
        "cube_small.urdf",
        [table_pos[0] - spread_x, table_pos[1] - spread_y, table_top_z + cube_half],
        globalScaling=3.0,
    )
    cube2 = p.loadURDF(
        "cube_small.urdf",
        [table_pos[0] + spread_x, table_pos[1] + spread_y, table_top_z + cube_half],
        globalScaling=3.0,
    )

    p.changeVisualShape(cube1, -1, rgbaColor=[0.1, 0.4, 1.0, 1.0])
    p.changeVisualShape(cube2, -1, rgbaColor=[0.1, 0.9, 0.2, 1.0])

    sphere_radius = 0.1
    cylinder_radius = 0.1
    cylinder_height = 0.2

    sphere_collision = p.createCollisionShape(p.GEOM_SPHERE, radius=sphere_radius)
    cylinder_collision = p.createCollisionShape(
        p.GEOM_CYLINDER,
        radius=cylinder_radius,
        height=cylinder_height,
    )

    sphere_red_visual = p.createVisualShape(p.GEOM_SPHERE, radius=sphere_radius, rgbaColor=[1.0, 0.2, 0.2, 1.0])
    sphere_pink_visual = p.createVisualShape(p.GEOM_SPHERE, radius=sphere_radius, rgbaColor=[1.0, 0.5, 0.7, 1.0])
    cylinder_orange_visual = p.createVisualShape(
        p.GEOM_CYLINDER,
        radius=cylinder_radius,
        length=cylinder_height,
        rgbaColor=[1.0, 0.5, 0.1, 1.0],
    )
    cylinder_yellow_visual = p.createVisualShape(
        p.GEOM_CYLINDER,
        radius=cylinder_radius,
        length=cylinder_height,
        rgbaColor=[1.0, 0.9, 0.1, 1.0],
    )

    sphere_z = table_top_z + sphere_radius
    cylinder_z = table_top_z + (cylinder_height / 2)

    sphere_red = p.createMultiBody(
        baseMass=1.0,
        baseCollisionShapeIndex=sphere_collision,
        baseVisualShapeIndex=sphere_red_visual,
        basePosition=[table_pos[0] - spread_x, table_pos[1] + spread_y, sphere_z],
    )
    sphere_pink = p.createMultiBody(
        baseMass=1.0,
        baseCollisionShapeIndex=sphere_collision,
        baseVisualShapeIndex=sphere_pink_visual,
        basePosition=[table_pos[0] + spread_x, table_pos[1] - spread_y, sphere_z],
    )
    cylinder_orange = p.createMultiBody(
        baseMass=1.0,
        baseCollisionShapeIndex=cylinder_collision,
        baseVisualShapeIndex=cylinder_orange_visual,
        basePosition=[table_pos[0], table_pos[1] - spread_y, cylinder_z],
    )
    cylinder_yellow = p.createMultiBody(
        baseMass=1.0,
        baseCollisionShapeIndex=cylinder_collision,
        baseVisualShapeIndex=cylinder_yellow_visual,
        basePosition=[table_pos[0], table_pos[1] + spread_y, cylinder_z],
    )

    objects = {
        "blue_cube": cube1,
        "green_cube": cube2,
        "red_sphere": sphere_red,
        "pink_sphere": sphere_pink,
        "orange_cylinder": cylinder_orange,
        "yellow_cylinder": cylinder_yellow,
    }

    scene = {
        "table_pos": table_pos,
        "table_top_z": table_top_z,
    }

    return robot, objects, scene