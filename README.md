# mv_automatically
Moves the predefined extension files from Downloads to the destination folder<br \>
Using this program now you can choose your default download directory from browsers as Downloads but your specific files will automatically will go to the directory you desired for this type of extensions rather than always choosing the destination path of the download from the pop up from the browser.<br \>
Example: you can download an .mp4 video to Downloads but this program will move this video to the Videos or any other directory you desire.<br \>

# Usage
make move.py and extract.sh as executable.<br \>
chmod u+x 'file_name' makes it executable.<br \>
For the first time you must modify this_path(in move.py) to the path of directory in which this repository is present.<br \>
To change the settings modify config.ini in config_files directory.<br \>
Add an extension and its destination in config.ini. An example extension is given in config.ini.<br \>
Now you can run it directly from terminal by ./move.py from this repository directory.<br \>
Another way is to add it to your startup applications so that it starts in the background.<br \>

# Note
This also includes auto extraction and the compressed file will be deleted as it served it purpose.<br \>
The default sleep_time is 5s for this program, you can modify it in config.ini.<br\>

