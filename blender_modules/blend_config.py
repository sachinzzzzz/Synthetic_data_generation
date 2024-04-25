import bpy
import bpycv
import os
import json
import cv2
import numpy as np
import random
from blend_config import Camera




class Blendfile(Camera):
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

class Camera:
    def __init__(self, name):
        self.name  = name               
        

    
