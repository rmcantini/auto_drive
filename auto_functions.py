import os
import shutil

# Define the source and destination paths


def new_task(src_folder, dest_folder)
    shutil.copytree(src_folder, dest_folder, dirs_exist_ok=False)


def task_update(src_folder, dest_folder)
    # Iterate over the files in the source folder
    for root, dirs, files in os.walk(src_folder):
        # Get the relative path of the current directory
        rel_dir = os.path.relpath(root, src_folder)

        # Create the corresponding directory in the destination folder
        dest_dir = os.path.join(dest_folder, rel_dir)
        os.makedirs(dest_dir, exist_ok=True)

        # Copy the files from the source directory to the destination directory
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)

            # Copy the file only if it does not exist in the destination directory - or if it's different
            if not os.path.exists(dest_file) or not os.path.samefile(src_file, dest_file):
                shutil.copy2(src_file, dest_file)

def up_go(src_folder, dest_folder):
    try:
        new_task(src_folder, dest_folder)
    except ValueError as e:
        print("The folder task already exists: ", e)
        print("Running task update instead")
        task_update(src_folder, dest_folder)
