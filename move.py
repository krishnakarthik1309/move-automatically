import os
import sys
import time
import subprocess
from ConfigParser import SafeConfigParser


def load_reader(config):
    config_directory = './config_files/'
    config = (os.path.abspath(
        os.path.join(config_directory, config)))

    reader = SafeConfigParser()
    reader.read(config)
    return reader


def load_path_to_watch(config):
    reader = load_reader(config)
    path_to_watch = reader.get('source', 'src_path')
    return path_to_watch


def move(config='config.ini'):
    path_to_watch = load_path_to_watch(config)
    before = os.listdir(path_to_watch)

    try:
        while True:
            time.sleep(5)
            after = os.listdir(path_to_watch)
            print 'after:'
            print after

            new_files = []
            for f in after:
                if f not in before:
                    new_files.append(f)
            print 'new_files:'
            print new_files
            for new_file in new_files:
                print '1'
                move_to_destination(new_file)
            before = after
    except KeyboardInterrupt:
        sys.exit()


def move_to_destination(new_file):
    print '2'
    extension = get_extension(new_file)
    destination = get_destination(extension)
    if destination is not None:
        print '5'
        subprocess.call(['mv',
                         '/home/kvothe/Downloads/' + new_file,
                         destination])
    else:
        return


def get_extension(file):
    print '3'
    file_name, file_extension = os.path.splitext(file)
    return file_extension


def get_destination(extension):
    print '4'
    reader = load_reader('config.ini')

    destination = reader.get('destination', extension[1:])
    return destination


if __name__ == '__main__':
    move()
