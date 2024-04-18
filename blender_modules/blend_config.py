import bpy
import bpycv
import os
import json
import cv2
import numpy as np
import random

class Blendfile:
    def __init__(self, file_path):
        self.path =  file_path

    def load_blend_file(self):
        bpy.ops.wm.open_mainfile(filepath=self.path)
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        return bpy.data.collections
    
    def generate_json_data(self, objects):
        data = {}
        inst_id = 1
        for obj in objects:
            obj["inst_id"] = inst_id
            inst_id += 1
            name_parts = obj.name.split('.')
            if len(name_parts) >= 2:
                obj_name = name_parts[0]
                obj_instance = '.'.join(name_parts[:2])
                if obj_name not in data:
                    data[obj_name] = {}
                if obj_instance not in data[obj_name]:
                    data[obj_name][obj_instance] = {
                    "label": len(data),
                    "color": [],
                    "inst_id": obj["inst_id"]
                }
        return data
    
    def make_json(self, json_path, collections):
        self.json_path = json_path
        self.collections = collections
        print(self.json_path)
        # list = []
        # for obj in self.collections.objects:
        #     list.append(obj.name)
        if not os.path.exists(self.json_path):
            with open(self.json_path, "w") as json_file:
                json.dump({}, json_file)
        json_data = self.generate_json_data(self.collections.objects)
        with open(self.json_path, "w") as json_file:
            json.dump(json_data, json_file, indent=4)
        print(f"JSON data has been written to '{self.json_path}'")

    def visualize_instance(self, colored_mask, instance_mask):
        used_colors = set()
        with open(self.json_path, "r") as file:
            data = json.load(file)
        unique_instance_ids = np.unique(instance_mask)
        for instance_id in unique_instance_ids:
            if instance_id == 0:
                continue
            mask = (instance_mask == instance_id)
            color = self.generate_unique_color(used_colors)
            for obj_name, obj_instances in data.items():
                for obj_instance, obj_data in obj_instances.items():
                    if obj_data["inst_id"] == instance_id:
                        obj_data["color"] = list(color)
                        with open(self.json_path, "w") as file:
                            json.dump(data, file, indent=4)
            colored_mask[mask] = color
            used_colors.add(tuple(color))
        return colored_mask
    
    def generate_unique_color(self, used_colors):
        while True:
            # Generate a random color
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            # Check if the color is not already used
            if tuple(color) not in used_colors:
                return color

    def camera_config():
        # config camera randomization
        return

    def light_config():
        # light variations
        return            
        

    
blend_file = Blendfile(r"E:\3D+animation\dataline\blenderFiles\W12001 3d Twin.blend") 
result = blend_file.load_blend_file()
blend_file.make_json(r"E:\3D+animation\dataline\src\grocery.json", result[1])
masks = bpycv.render_data()

cwd = r"E:\3D+animation\dataline"
print(cwd)
rgb_path = f"{cwd}/src/data_points/1/rgb.png"
color_inst_path = f"{cwd}/src/data_points/1/color_inst.png"
inst_path = f"{cwd}/src/data_points/1/instance.png"
depth_path = f"{cwd}/src/data_points/1/depth.png"
vis_path = f"{cwd}/src/data_points/1/vis.png"

cv2.imwrite(rgb_path, masks["image"][..., ::-1])


instance_mask = masks["inst"]
colored_mask = np.zeros_like(masks["image"])
visualize = blend_file.visualize_instance(colored_mask, instance_mask)
cv2.imwrite(color_inst_path, visualize)
cv2.imwrite(vis_path, cv2.cvtColor(masks.vis(), cv2.COLOR_RGB2BGR))
print("Visualization images saved.")

# Save RGB image
cv2.imwrite(rgb_path, masks["image"][..., ::-1])

# Save instance map as 16-bit png
cv2.imwrite(inst_path, np.uint16(masks["inst"]))

# Convert depth units from meters to millimeters and save as 16-bit png
depth_in_mm = masks["depth"] * 1000
cv2.imwrite(depth_path, np.uint16(depth_in_mm))
print("Instance map and depth image saved.")



print(result[1])
 