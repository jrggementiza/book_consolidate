#!/usr/bin/python3
""" A Simple Script that moves specified files from a target folder and subfolders to a destination folder. """
import sys
import os, shutil
import glob


def move_filenames_per_filetype(destination_folder, filetype_filenames_payload):
    """ Moves filenames from a target path to a destination path per filetype """
    for filetype, filenames, filepaths in filetype_filenames_payload:
        for filename, filepath in zip(filenames, filepaths):
            target_path = os.path.join(filepath, filename)
            destination_path = os.path.join(destination_folder + '/' + filetype[1:] + '/' + filename)
            print(target_path, destination_path)
            try:
                shutil.move(target_path, destination_path)
                print(f'Moved {filename} to {destination_path}')
            except PermissionError as e:
                print(f'{e} - Copying instead!')
                pass


def create_filetype_destination_directory(destination_folder, filetypes_to_consolidate):
    """ Creates a directory for each filetypes_to_consolidate at a destination folder """
    for filetype in filetypes_to_consolidate:
        destination_directory_name = destination_folder + '/' + filetype[1:]
        try:
            os.mkdir(destination_directory_name)
        except Exception as e:
            print(f'{e} - Folder already exists! Skipping!')
            pass


def generate_filetype_filenames_filepaths_payload(target_folder, filetypes_to_consolidate):
    """ Walks a target_folder and looks for files based on filetypes_to_consolidate
    Returns a list of lists: [filetype, [filenames], [filepaths]] """
    payload = []
    for dirpath, dirname, filename in os.walk(target_folder):
        for filetype in filetypes_to_consolidate:
            filenames = []
            filepaths = []
            for file in filename:
                name, ext = os.path.splitext(file) # TODO: replace with glob
                if ext == filetype:
                    filenames.append(file)
                    filepaths.append(dirpath)
            payload.append([filetype, filenames, filepaths])
    return payload


def generate_filetypes_to_consolidate(args):
    """ Accepts filetypes passed by user and returns a list of valid filetypes to consolidate """
    valid_filetypes = []
    for arg in args:
        # TODO: Validate filetype is valid
        filetype = '.' + arg
        valid_filetypes.append(filetype)
    return valid_filetypes


def main():
    target_folder = sys.argv[1]
    try:
        destination_folder = sys.argv[2]
    except Exception as e:
        destination_folder = os.getcwd()

    filetypes_to_consolidate = generate_filetypes_to_consolidate(sys.argv[3:])

    filetype_filenames_filepaths_payload = generate_filetype_filenames_filepaths_payload(target_folder, filetypes_to_consolidate)

    create_filetype_destination_directory(destination_folder, filetypes_to_consolidate)

    move_filenames_per_filetype(destination_folder, filetype_filenames_filepaths_payload)


if __name__ == '__main__':
    main()
