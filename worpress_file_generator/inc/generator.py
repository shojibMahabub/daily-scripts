import os
from inc.elements import directories as dirs
from inc.elements import files


def generate_theme_directory(directory_location):
    loc = directory_location
    if not os.path.exists(loc):
        os.makedirs(loc)
    else:
        print(loc, ' Directory already exists !')


def generate_wp_directories(directory_location):
    loc = directory_location
    # creating directories
    for item in dirs:
        dir_name = loc + item
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        else:
            print(loc, ' Directory already exists !')


def generate_wp_files(directory_location):
    loc = directory_location
    # creating files
    for file_name in files:
        f = open(loc + file_name, 'w')
        f.close()
