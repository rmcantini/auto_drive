'''Auto drive script to upload everything'''
import os
import shutil
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

filePath = filedialog.askopenfilename(title='Abra a lista')
folderPath = filedialog.askdirectory(title='Selecione onde estão as pastas')
destination = filedialog.askdirectory(title='Selecione o destino')

# First, create a list and populate it with the files

# you want to find (1 file per row in myfiles.txt)

foldersToFind = []
with open(filePath, encoding='UTF-8') as fh:
    for row in fh:
        foldersToFind.append(row.strip())
        # print(foldersToFind)

print(folderPath)
print(destination)
print(foldersToFind)


# Had an issue here but needed to define and then reference the filename variable itself
for foldername in os.listdir(folderPath):
    if foldername in foldersToFind:
        foldername = os.path.join(folderPath, foldername)
        print(foldername)
        shutil.copytree(foldername, destination)

    else:
        print(f"Did not copy: {foldername}")
