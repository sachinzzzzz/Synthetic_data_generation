import subprocess
# from utils import create_bbox as bbox
# from automation import renderd_processing as rp
# from automation import train_test

#1.load and make json
#2.generate different masks
#3.make bbox
#4.make mask
#5.split train and valid

def run_blender_script(blender_script):
    # Path to Blender executable
    blender_executable = r"C:\Program Files\Blender Foundation\Blender 3.6\blender.exe"

    # Command to run Blender with the specified script
    command = [blender_executable, "--background", "--python", blender_script]

    # Run Blender with the specified script
    subprocess.run(command, check=True)

# def genrate_data_points(start_p, end_p):
#     for iteration in range (start_p, end_p)    

def orchestration():

    # blender_script = r"E:\3D+animation\dataline\automation\blender_data.py"
    blender_script = r"E:\3D+animation\dataline\mod.py"
    input_dir = r"E:\3D+animation\dataline\src\data_points"
    output_train_dir = r"E:\3D+animation\dataline\training\grocery\train"
    output_test_dir = r"E:\3D+animation\dataline\training\grocery\test"
    # Run the Blender script
    run_blender_script(blender_script)

    # rp.render_later_processing(1, 5)

    # train_test.split_it(input_dir, output_train_dir, output_test_dir)


    print("orchestration successfull")
