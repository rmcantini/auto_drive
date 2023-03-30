import os
import shutil
import datetime

folder_path = "/path/to/Clientes"
modified_since_hours = 6

now = datetime.datetime.now()
modified_since = now - datetime.timedelta(hours=modified_since_hours)

destination_folder = os.path.join(folder_path, "ClientModified")
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for foldername, subfolders, filenames in os.walk(folder_path):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        if file_modified_time > modified_since:
            destination_file_path = os.path.join(destination_folder, filename)
            shutil.copy2(file_path, destination_file_path)


'''
This function will return a list of file paths for all files modified or created in the last interval_hours in the 'Clientes' folder.

After running this code, the user can manually upload the files from the "ClientModified" folder to the desired destination, such as Google Drive or another cloud storage service.
'''