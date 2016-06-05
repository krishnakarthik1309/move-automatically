#!/usr/bin/python
import os
import re
import sys
import time
import subprocess
from ConfigParser import SafeConfigParser


def load_reader(config):
    config_directory = '/home/kvothe/Dropbox/repos/' +\
        'mv_automatically/config_files/'
    config = (os.path.abspath(
        os.path.join(config_directory, config)))

    reader = SafeConfigParser()
    reader.read(config)
    return reader


def load_sleep_time(config):
    reader = load_reader(config)
    sleep_time = reader.get('time', 'sleep')
    return float(sleep_time)


def load_path_to_watch(config):
    reader = load_reader(config)
    path_to_watch = reader.get('source', 'src_path')
    return path_to_watch


def is_compressed(file):
    dicti = {'.tar.bz2', '.tar.gz',
             '.bz2', '.rar',
             '.gz', '.tar',
             '.tbz2', '.tgz',
             '.zip', '.Z', '.7z'}
    for ext in dicti:
        match = re.search(ext, file)
        if match:
            return match
    return match


def move(config='config.ini'):
    path_to_watch = load_path_to_watch(config)
    sleep_time = load_sleep_time(config)
    before = []

    try:
        while True:
            time.sleep(sleep_time)
            after = os.listdir(path_to_watch)
            new_files = []
            for f in after:
                if f not in before:
                    f = os.path.join(path_to_watch, f)
                    if is_compressed(f):
                        os.system('./extract.sh %s %s' % (f, path_to_watch))
                        subprocess.call(['notify-send', '"extracted"'])
                    else:
                        new_files.append(f)
            for new_file in new_files:
                move_to_destination(new_file)
            before = after
    except KeyboardInterrupt:
        sys.exit()


def move_to_destination(new_file):
    extension = get_extension(new_file)
    destination = get_destination(extension)
    if destination is not None:
        subprocess.call(['mv', new_file, destination])
        subprocess.call(['notify-send',
                         'moved %s to %s' % (new_file, destination)])
    else:
        return


def get_extension(file):
    file_extension = os.path.splitext(file)[1]
    return file_extension


def get_destination(extension):
    reader = load_reader('config.ini')

    try:
        destination = reader.get('destination', extension[1:])
        return destination
    except:
        return


if __name__ == '__main__':
    move()
