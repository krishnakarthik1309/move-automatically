# mv_automatically
Whenever a file is downloaded from browser into Downloads folder, the program looks up the type of the file(software or video or picture etc) and move the file from Downloads folder to corresponding desired folder.
Example: you can download an example.mp4 video to Downloads but this program will move this video to the ~/Videos directory(or any other directory you desire.)

Edit the config.ini file to choose the source folder(Ex: /home/username/Downloads/), type of files to move(Ex:deb or png) and the destination folder for the corresponding files.(Ex: /home/username/Pictures for png)

# Advantages
Organizes your folders automatically rather than choosing the destination from browser/torrent popup window for every single download.

# Usage/Steps
* make move.py and extract.sh as executable.
chmod u+x 'file_name' makes it executable.
* For the first time you must modify config.ini in config_files directory to edit source folder, file type and the corresponding destination folder.
An example extension is given in config.ini.
* Now you can run it directly from terminal by ./move.py from this repository directory.
* Another way is to add it to your startup applications so that it starts in the background.

# Note
* This also includes auto extraction and the compressed file will be deleted as it served it purpose.
* The default sleep_time is 5s for this program, you can modify it in config.ini.
* Currently this is only for linux.
