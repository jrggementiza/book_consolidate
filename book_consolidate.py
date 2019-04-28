#!/usr/bin/python3
""" A simple script that walks a root directories folders, subfolders, and files,
grabs a copy of files with a .pdf / .epub file extension,
and moves it to the root directory
sorted via folders named pdf and epub, per file type.
"""

import os
import shutil


def sort_file_and_move(path_of_files_to_move, destination_folders):
    """ Accepts a list of file paths to move, and a list of destination folders,
    sorts file paths and moves said file paths to destination folders that
    match their file paths """

    for source in path_of_files_to_move:
        name, ext = os.path.splitext(source)
        for destination in destination_folders:
            _, dest_ext = os.path.split(destination)
            if ext[1:] == dest_ext:
                try:
                    shutil.move(source, destination,
                                copy_function=shutil.copy(source, destination))
                except Exception as e:
                    print(e)


def generate_destination_folders(filetype_watchlist, path):
    """ Accepts a list of filetypes to watch,
    creates a directory per filetype to watch, and
    returns a list of paths per created directory 
    """

    destination_paths = []
    for directory_name in filetype_watchlist:
        path_directory_name = path + '/' + directory_name[1:]
        try:
            os.mkdir(path_directory_name)
        except Exception as e:
            print(e)
            pass
        destination_paths.append(path_directory_name)
    return destination_paths


def generate_path_of_files_to_move(filetype_watchlist, path):
    """ Accepts list of filetypes to watch and
    returns a list of paths of files to move
    """

    path_of_files_to_move = []
    for dirpath, dirname, filename in os.walk(path):
        for file in filename:
            name, ext = os.path.splitext(file)
            if ext in filetype_watchlist:
                path_of_file = os.path.join(dirpath, file)
                path_of_files_to_move.append(path_of_file)
    return path_of_files_to_move


def generate_filetype_to_watch():
    """ Asks users to input filetypes to watch
    and returns a list of said filetypes
    """

    # TODO: Actual Implementation (cli version of args passed / gui clicky buttons)
    return ['.pdf', '.epub']


def main():
    # TODO: "path" -> root_folder = os.getcwd()
    TARGET_FOLDER = '/Users/jrggementiza/Documents/_Sharpening/_Books' #TODO: TARGET_FOLDER in env
    target_folder = TARGET_FOLDER

    filetype_watchlist = generate_filetype_to_watch()

    path_of_files_to_move = generate_path_of_files_to_move(
        filetype_watchlist, target_folder)

    destination_folders = generate_destination_folders(
        filetype_watchlist, target_folder)

    sort_file_and_move(path_of_files_to_move, destination_folders)

    # TODO: Delete Files / Directories with permissions
    for file in path_of_files_to_move:
        try:
            shutil.rmtree(file)
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    main()
