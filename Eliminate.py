import tkinter as tk
import shutil as shu
import os
from tkinter import filedialog
from math import trunc

tk.messagebox.showinfo("Information", "Please select the source directory.") # type: ignore
dir_path = filedialog.askdirectory()

tk.messagebox.showinfo("Information", "Please select the destination (temporary) directory.") # type: ignore
dest_path = filedialog.askdirectory()

# Get all files/folders in the source directory
dirs = os.listdir(dir_path)

# Get a count of half of them
count = round(len(dirs) / 2)

# Empty list/array for logging last-moved items
moved = []

# Zero'd integer for logging 'no' answers
nos = 0

# Iterate through the half
for x in range(0, count):
    f = dirs[x]
    g = os.path.join(dir_path, f)
    moved.append(shu.move(g, dest_path)) # Move the files/folders to the destination and append it to the list

# Run infinitely until the user has answered 'no' twice. This should give only one folder / file that is the problem
while True:
    # Display a message box saying that the process was complete (that half of the files/folders have been moved to the destination)
    msg_box = tk.messagebox.askquestion('Complete', 'Half of the files and/or folders have been removed. Please validate, does the issue persist?') # type: ignore

    if (msg_box == 'yes'):
        moved = []
        nos = 0

        # Get all files/folders in the source directory
        dirs = os.listdir(dir_path)

        # Get a count of half of them    
        count = trunc(len(dirs) / 2)
        
        # Iterate through the half
        for x in range(0, count):
            f = dirs[x]
            g = os.path.join(dir_path, f)
            moved.append(shu.move(g, dest_path)) # Move the files/folders to the destination and append it to the list
    else:
        # Increase count of 'no' answers
        nos += 1

        # Check if the user has answered 'no' twice
        if nos >= 2:
            msg_box = tk.messagebox.showinfo('File found', 'It\'s likely that "' + moved[0] + '" is the file/folder in question.') # type: ignore
            break
        
        # Get all files/folders in the source directory
        dirs = os.listdir(dir_path)

        # Get a count of all of them
        count = len(dirs)

        # Force validation if there is only one file in the destination and the user has already given one 'no'
        if (count == 1 and nos >= 1):
            msg_box = tk.messagebox.showinfo('File found', 'It\'s likely that "' + dirs[0] + '" is the file/folder in question.') # type: ignore
            break

        # Iterate through the list
        for x in range(0, count):
            f = dirs[x]
            g = os.path.join(dir_path, f)
            shu.move(g, dest_path) # Move the files/folders to the destination

        # Get a count of all previously moved files
        count = len(moved)

        # Iterate throught them
        for x in range(0, count):
            f = moved[x]
            shu.move(f, dir_path) # Restore all files/folders from the destination back to the source directory

# Ask the user if they want to restore all files/folders that were moved into the destination back to the source directory
msg_box = tk.messagebox.askquestion('Restore', 'Do you want to move all files from the destination (temporary) directory into the original source directory?') # type: ignore

# If yes, move them back utilizing same process as above
if (msg_box == 'yes'):
    dirs = os.listdir(dest_path)
    count = len(dirs)

    for x in range(0, count):
        f = dirs[x]
        g = os.path.join(dest_path, f)
        shu.move(g, dir_path)
