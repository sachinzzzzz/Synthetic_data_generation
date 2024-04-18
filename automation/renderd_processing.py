from utils import create_bbox as bbox
import os

def render_later_processing(start_p, end_p):
    for iteration in range(start_p, end_p+1):
        cwd = r"E:\3D+animation\dataline\src\data_points"
        data_point_dir = os.path.join(cwd, str(iteration))

        inst_image_path = os.path.join(data_point_dir, "instance.png")
        inst_json_path = os.path.join(data_point_dir, "grocery.json")
        rgb_path = os.path.join(data_point_dir, "rgb.png")
        segmentation_label_path = os.path.join(data_point_dir, "segmentation.txt")
        bbox_label_path = os.path.join(data_point_dir, "bbox.txt")
        bbox.save_segmentation_and_bbox(inst_image_path, inst_json_path, segmentation_label_path, bbox_label_path)
        bbox.make_bbox(rgb_path, bbox_label_path, data_point_dir)

       


