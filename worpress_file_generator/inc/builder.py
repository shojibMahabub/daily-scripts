import os

def theme_folder_address (base_directory, theme_name):
    dev_directory = os.path.join(base_directory, theme_name)
    theme_directory = dev_directory + '/'
    locations = {
        'dev_directory': dev_directory,
        'theme_directory': theme_directory
    }
    return locations

