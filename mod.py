import blend_config as config
import bpy
import math
import mathutils

class Main:
    def __init__(self, name):
        self.config  = name
        self.config.location = [2.3, -1.9, 2.3]
        print(self.config)
        print(f"how camera is {self.config.location}")

    def set_camera_orientation(self, camera_object, target_coordinate):
    # Get the camera location
        camera_location = camera_object.location

    # Calculate direction vector from camera to target
        direction_vector = target_coordinate - camera_location

    # Calculate Euler angles from the direction vector
        rotation_matrix = direction_vector.to_track_quat('-Z', 'Y').to_matrix().to_4x4()
        camera_object.matrix_world = rotation_matrix


    def set_camera_pos(self, present_co_ods, distance, angle):
        rad_angle =   math.radians(angle)
        target_coordinate = mathutils.Vector(present_co_ods)

        camera_location = (
        present_co_ods[0] + distance * math.cos(rad_angle),
        present_co_ods[1] + distance * math.sin(rad_angle),
        present_co_ods[2]  # Keep the same Z coordinate
        )

        self.config.location = camera_location
        print(f"how camera is {self.config.location}")
        self.set_camera_orientation(self.config, target_coordinate)
        ang = self.config.rotation_euler
        rotation_degrees = [math.degrees(angle) for angle in ang]
        print(f"how camera angle{rotation_degrees}")


blend_file = config.Blendfile(r"E:\3D+animation\dataline\blenderFiles\Cube.blend")
result = blend_file.load_blend_file()
camera = result[0].objects.get("My_camera")
camera1 = Main(camera)
object_coordinates = [0, 0, 0]
distance = 5
angle = 30

camera1.set_camera_pos(object_coordinates, distance, angle)
print(camera)
print (result[0].objects)

# Set the render resolution
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080

# Set other render settings as needed
# For example:
bpy.context.scene.render.engine = 'BLENDER_EEVEE'  # Set render engine to Cycles
bpy.context.scene.render.image_settings.file_format = 'PNG'

output_file_path = r"E:\multimedia"
bpy.context.scene.render.filepath = output_file_path
# # Render the scene
bpy.ops.render.render(write_still=True)

# Save rendered image in Blender's Image Editor
# bpy.data.images['Render Result'].save_render(output_file_path)