import os
import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory

# hide root window
root = tk.Tk()
root.withdraw()


def get_files_modified_within_hours(path, hours):
    """Get list of files modified within a certain number of hours"""
    files_modified = []
    time_now = os.path.getctime(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if (time_now - os.path.getctime(filepath)) / 3600 <= hours:
                files_modified.append(filepath)
    return files_modified


def copy_files_to_folder(files, dest_folder):
    """Copy a list of files to a destination folder, preserving folder structure"""
    for file in files:
        rel_path = os.path.relpath(file, start=path_main)
        dest_file = os.path.join(dest_folder, rel_path)
        dest_dir = os.path.dirname(dest_file)
        os.makedirs(dest_dir, exist_ok=True)
        shutil.copy2(file, dest_file)


if __name__ == "__main__":
    # intro explanation pop-up
    tk.messagebox.showinfo("info", "Select the folder with the modified files.")

    # asks what directory to work with
    path_main = askdirectory(
        initialdir="~/downloads", title="Select the folder with the modified files."
    )

    # ask destination folder for the copied files
    dest_folder = askdirectory(
        initialdir="~/downloads",
        title="Select the destination folder for the copied files.",
    )

    # get list of files modified within the last 24 hours
    files_to_copy = get_files_modified_within_hours(path_main, 24)

    # copy files to destination folder, preserving folder structure
    copy_files_to_folder(files_to_copy, dest_folder)

    # success message pop-up
    tk.messagebox.showinfo("info", "Files copied successfully!")

"""
This code uses the relpath function from the os module to 
get the relative path of each file from the path_main 
directory, and then creates the corresponding directories 
in the dest_folder directory using os.makedirs with the exist_ok
 argument set to True to avoid errors if the directories 
 already exist. Finally, it uses shutil.copy2 to copy the 
 files while preserving their metadata.

"""
