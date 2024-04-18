import os
import random
import shutil

def split_it(input_dir, output_train_dir, output_test_dir, split_ratio=0.8, seed=42):
    random.seed(seed)

    # Create train and test directories if they don't exist
    os.makedirs(os.path.join(output_train_dir, "images"), exist_ok=True)
    os.makedirs(os.path.join(output_train_dir, "labels"), exist_ok=True)
    os.makedirs(os.path.join(output_test_dir, "images"), exist_ok=True)
    os.makedirs(os.path.join(output_test_dir, "labels"), exist_ok=True)

    # Get list of data points (directories)
    data_points = os.listdir(input_dir)
    random.shuffle(data_points)

    # Calculate number of data points for train and test
    num_train = int(len(data_points) * split_ratio)
    train_data_points = data_points[:num_train]
    test_data_points = data_points[num_train:]

    # Copy data points to train directory
    for idx, data_point in enumerate(train_data_points, start=1):
        data_point_path = os.path.join(input_dir, data_point)

        # Copy image file
        image_src = os.path.join(data_point_path, "bbox.jpg")
        image_dst = os.path.join(output_train_dir, "images", f"{idx}.jpg")
        shutil.copy(image_src, image_dst)

        # Copy text file
        txt_src = os.path.join(data_point_path, "bbox.txt")
        txt_dst = os.path.join(output_train_dir, "labels", f"{idx}.txt")
        shutil.copy(txt_src, txt_dst)

    # Copy data points to test directory
    for idx, data_point in enumerate(test_data_points, start=1):
        data_point_path = os.path.join(input_dir, data_point)

        # Copy image file
        image_src = os.path.join(data_point_path, "bbox.jpg")
        image_dst = os.path.join(output_test_dir, "images", f"{idx}.jpg")
        shutil.copy(image_src, image_dst)

        # Copy text file
        txt_src = os.path.join(data_point_path, "bbox.txt")
        txt_dst = os.path.join(output_test_dir, "labels", f"{idx}.txt")
        shutil.copy(txt_src, txt_dst)

# Example usage
input_dir = r"E:\3D+animation\dataline\src\data_points"
output_train_dir = r"E:\3D+animation\dataline\training\grocery\train"
output_test_dir = r"E:\3D+animation\dataline\training\grocery\test"
# split_train_test_data(input_dir, output_train_dir, output_test_dir)
