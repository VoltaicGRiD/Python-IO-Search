# Python IO Search
Great for testing which file, folder, mod, app, etc. is causing a problem / conflict. Will iterate through all files and folders in the specified directories and move them to a temporary directory for quick and painless testing.

This quick-fire application utilizes the process of elimination to determine whether an app or file is causing conflict.

## Usage
`python {Path-To-File}/Elimination.py`

Once run, you're prompted with basic instructions to select a source directory, and a destination directory.
After selecting both directories, the application will move (not copy) half (rounded-down) of the files and folders from the source directory to the destination.
As long as the user hasn't selected 'no' twice on the "does the issue persist?" question, and there is more than one file/folder in the source directory, the process repeats indefinitely.
Once the files/folders have been eliminated down to a single option, or the user has validated that the issue no longer persists, a dialog highlighting the name and path of the file is presented, along with a dialog asking the user if they would like to restore all files/folders from the temporary folder back to the source folder.
