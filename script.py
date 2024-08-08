import os
import subprocess

def open_folder(path):
    try:
        os.startfile(path)
    except Exception as e:
        print(f"Failed to open folder {path}. Reason: {e}")

def run_disk_cleanup():
    try:
        subprocess.run(['cleanmgr', '/sagerun:1'])
    except Exception as e:
        print(f"Failed to run Disk Cleanup. Reason: {e}")

# Get the system directories
recent_folder = os.path.join(os.environ['USERPROFILE'], 'Recent')
temp_folder = os.getenv('TEMP')
local_temp_folder = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Temp')
prefetch_folder = os.path.join(os.environ['WINDIR'], 'Prefetch')

# Opening the folders
open_folder(recent_folder)
open_folder(temp_folder)
open_folder(local_temp_folder)
open_folder(prefetch_folder)

# Run Disk Cleanup
run_disk_cleanup()

print("Opened Recent, Temp, %TEMP%, and Prefetch folders and initiated Disk Cleanup. Please complete the cleanup manually.")
