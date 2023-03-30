import tkinter as tk
from tkinter import filedialog
import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read("config.ini")

# If the "Settings" section doesn't exist, create it
if "Settings" not in config:
    config["Settings"] = {}

# Function to handle folder selection and saving
def choose_folder(key_name, label):
    folder_path = filedialog.askdirectory()
    config["Settings"][key_name] = folder_path
    with open("config.ini", "w") as configfile:
        config.write(configfile)
    label.config(text=f"{key_name} path: {folder_path}"[-32:])
    print(f"{key_name} path saved to config.ini file.")


# Create the Tkinter window
root = tk.Tk()
root.title("Minha janelinha top")

# Set the window size and position
root.geometry("540x156")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - root.winfo_width()) // 2 - 100
y = (screen_height - root.winfo_height()) // 2 - 100
root.geometry(f"+{x}+{y}")

# Create two frames, one for each column
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

# Add widgets to the first frame (column 0)
label1 = tk.Label(frame1, text="")
button1 = tk.Button(
    frame1, text="Choose Local Folder", command=lambda: choose_folder("Folder1", label1)
)
if "Folder1" in config["Settings"]:
    folder_path = config["Settings"]["Folder1"]
    label1.config(text=f"Folder1 path: {folder_path}"[-32:])
label1.pack()
button1.pack()

# Add widgets to the second frame (column 1)
label2 = tk.Label(frame2, text="")
button2 = tk.Button(
    frame2, text="Choose Drive Folder", command=lambda: choose_folder("Folder2", label2)
)
if "Folder2" in config["Settings"]:
    folder_path = config["Settings"]["Folder2"]
    label2.config(text=f"Folder2 path: {folder_path}"[-32:])
label2.pack()
button2.pack()

# Use grid geometry manager to place the frames
frame1.grid(row=0, column=0, sticky="n")
frame2.grid(row=0, column=1, sticky="s")

# Center the columns in the window
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Create the action button
button3 = tk.Button(root, text="Update Drive", width=16, height=2)
button3.place(relx=0.5, rely=1.0, anchor=tk.S, y=-8)

root.mainloop()
