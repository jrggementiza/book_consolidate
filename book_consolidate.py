#!/usr/bin/python3
""" Simple script that undiscriminately moves book files from a target folder to a destination folder """
import sys
import os, shutil
import glob


def create_destination_directory(destination_folder, filetype):
    """ Accepts a destination_folder and a filetype and
    creates a directory. Returns the destination_directory_name """
    destination_directory_name = destination_folder + '/' + filetype[1:]
    try:
        os.mkdir(destination_directory_name)
    except Exception as e:
        print(e)
        pass
    return destination_directory_name


def generate_filetype_and_filepaths_payload(target_folder, filetypes_to_consolidate):
    """ Returns a list of lists for [[filetype1, [filepaths1]], [filetype2, [filepaths2]], etc]
    based on a list of filetypes on the target folder
    """
    return [generate_filepaths(filetype, target_folder) for filetype in filetypes_to_consolidate]


def generate_filepaths(filetype, target_folder):
    """ Returns a list of filepaths based on accepted
    filetype and target_folder
    """

    path_of_files_to_move = []
    for dirpath, dirname, filename in os.walk(target_folder):
        for file in filename:
            name, ext = os.path.splitext(file)
            if ext == filetype:
                path_of_file = os.path.join(dirpath, file)
                path_of_files_to_move.append(path_of_file)
    payload = [filetype, path_of_files_to_move]
    return payload


def generate_filetypes_to_consolidate():
    """ Deprecated: Asks users to input filetypes to watch
    and returns a list of said filetypes
    """
    # TODO: Actual Implementation (cli version of args passed / gui clicky buttons)
    # TODO: would look like : script.py target_folder destination_folder -delete_soource=True *filetypes_to_consolidate
    return ['.pdf', '.epub']


def main():
    # TARGET_FOLDER = '/Users/jrggementiza/Documents/_Sharpening/_Books'
    target_folder = sys.argv[1]
    try:
        destination_folder = sys.argv[2]
    except Exception as e:
        destination_folder = os.getcwd()

    filetypes_to_consolidate = generate_filetypes_to_consolidate()

    filetype_filepaths_payload = generate_filetype_and_filepaths_payload(target_folder, filetypes_to_consolidate)
    
    for filetype, filepaths in filetype_filepaths_payload:
        destination_directory_name = create_destination_directory(destination_folder, filetype)
        for filepath in filepaths:
            shutil.move(filepath, destination_directory_name)
            print(f'move from {filepath} - to {destination_directory_name}')
        

if __name__ == '__main__':
    main()
