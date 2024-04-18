# import bpy
# import bpycv
# import cv2
# import numpy as np
import os

cwd = os.getcwd()

#path for blender file  = 
input_file_path = os.path.join(cwd, "blenderFiles\W12001 3d Twin.blend")
print(input_file_path)

#grocery base json path
json_ori_path = os.path.join(cwd,"src\grocery.json")