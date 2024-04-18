from orchestration.orchestration import orchestration
import subprocess


def run_blender_script(blender_script):
    # Path to Blender executable
    blender_executable = r"C:\Program Files\Blender Foundation\Blender 3.6\blender.exe"

    # Command to run Blender with the specified script
    command = [blender_executable, "--background", "--python", blender_script]

    # Run Blender with the specified script
    subprocess.run(command, check=True)

if __name__ == "__main__":
    # Path to the script to be run in Blender
    blender_script = r"E:\3D+animation\dataline\blender_modules\blend_config.py"

    # Run the Blender script
    run_blender_script(blender_script)
    orchestration()