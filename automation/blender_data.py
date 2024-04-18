import blend_config as config
import cv2
import bpycv
import numpy as np
import os
import shutil

def generate_data_point(start_no, end_no):

    for iteration in range(start_no, end_no+1):
        cwd = r"E:\3D+animation\dataline\src\data_points"
        # Create directory if it doesn't exist
        data_point_dir = os.path.join(cwd, str(iteration))
        if not os.path.exists(data_point_dir):
            os.makedirs(data_point_dir)

        blend_file = config.Blendfile(r"E:\3D+animation\dataline\blenderFiles\W12001 3d Twin.blend")
        result = blend_file.load_blend_file()
        blend_file.make_json(r"E:\3D+animation\dataline\src\grocery.json", result[1])
        masks = bpycv.render_data()

        rgb_path = os.path.join(data_point_dir, "rgb.png")
        color_inst_path = os.path.join(data_point_dir, "color_inst.png")
        inst_path = os.path.join(data_point_dir, "instance.png")
        depth_path = os.path.join(data_point_dir, "depth.png")
        vis_path = os.path.join(data_point_dir, "vis.png")

        cv2.imwrite(rgb_path, masks["image"][..., ::-1])

        instance_mask = masks["inst"]
        colored_mask = np.zeros_like(masks["image"])
        visualize = blend_file.visualize_instance(colored_mask, instance_mask)
        json_source_path = r"E:\3D+animation\dataline\src\grocery.json"
        json_destination_path = os.path.join(data_point_dir, "grocery.json")
        shutil.copyfile(json_source_path, json_destination_path)
        cv2.imwrite(color_inst_path, visualize)
        cv2.imwrite(vis_path, cv2.cvtColor(masks.vis(), cv2.COLOR_RGB2BGR))
        cv2.imwrite(inst_path, np.uint16(masks["inst"]))

        # Convert depth units from meters to millimeters and save as 16-bit png
        depth_in_mm = masks["depth"] * 1000
        cv2.imwrite(depth_path, np.uint16(depth_in_mm))
        print("Instance map and depth image saved.")

        
        


        
cwd = r"E:\3D+animation\dataline"   
generate_data_point(1, 5)