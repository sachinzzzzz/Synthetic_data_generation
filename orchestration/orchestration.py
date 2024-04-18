import subprocess
import mod
from utils import create_bbox as bbox

# def run_blender_script(blender_script):
#     # Path to Blender executable
#     blender_executable = r"C:\Program Files\Blender Foundation\Blender 3.6\blender.exe"

#     # Command to run Blender with the specified script
#     command = [blender_executable, "--background", "--python", blender_script]

#     # Run Blender with the specified script
#     subprocess.run(command, check=True)

# if __name__ == "__main__":
#     # Path to the script to be run in Blender
#     blender_script = "blender.py"

#     # Run the Blender script
#     run_blender_script(blender_script)
#     mod.print_this()

#1.load and make json
#2.generate different masks
#3.make bbox
#4.make mask
#5.split train and valid



def orchestration():
    cwd = r"E:\3D+animation\dataline"
    json_path = r"E:\3D+animation\dataline\src\grocery.json"

    inst_image_path = r"E:\3D+animation\dataline\src\data_points\1\instance.png"
    inst_json_path = json_path
    segmentation_label_path = r"E:\3D+animation\dataline\src\data_points\1\segmentation.txt"
    bbox_label_path = r"E:\3D+animation\dataline\src\data_points\1\bbox.txt"
    rgb_path = f"{cwd}/src/data_points/1/rgb.png"
    res_bbox = f"{cwd}/src/data_points/1"

    bbox.save_segmentation_and_bbox(inst_image_path, inst_json_path, segmentation_label_path, bbox_label_path)
    bbox.make_bbox(rgb_path, bbox_label_path, res_bbox)
    print("orchestration successfull")
