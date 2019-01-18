'''
This software is able to generate wordpress environment
=======================================================
Autor         : Mahabub Elahi
contact       : shojibmahabub630@gmail.com
version       : 1.0
license       : MIT
documentation :
=======================================================
'''
import os

# importing file system builder
from inc.builder import theme_folder_address

# importing generator
from inc.generator import generate_theme_directory
from inc.generator import generate_wp_directories
from inc.generator import generate_wp_files

'''
interaction with user
=========================================================
this portion of code will ask the user for desired theme
name. based on this theme name file system will generate
=========================================================
'''
theme_name = input("What is your theme name ?")

'''
file system building
========================================================
creating base directory location,
based on base dir and theme name

currently this software is able generate folder in the
same path of main.py file. This can be improved such a 
way that it can generate files and folders in document
root directry according to server.
========================================================
'''
base_dir = os.path.dirname(os.path.realpath(__file__))
locations = theme_folder_address(base_dir, theme_name)

'''
file system generation
========================================================
generate required wp files and folders using generator
locations of this files and folders came from file system 
builder.
========================================================
'''
generate_theme_directory(locations['dev_directory'])
generate_wp_directories(locations['theme_directory'])
generate_wp_files(locations['theme_directory'])


