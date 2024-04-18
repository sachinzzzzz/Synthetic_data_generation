import bpy
import bpycv


class Camera:
    def __init__(self,camera_name):
        self.camera = bpy.data.objects[camera_name]

    def config(self, resolution=(1920, 1080)):
        self.camera["resolution"] = resolution
        print(resolution)



# Create a new instance of MyObject with the camera name
camera = Camera("Camera")
# Render the scene
bpy.ops.render.render(write_still=True)


# Configure the camera using the config function
camera.config(resolution=(1920, 1080))
print("used blender")
