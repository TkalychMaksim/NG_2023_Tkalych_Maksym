import os
import argparse


def find_files(folder, key):
    for file in os.listdir(folder):  # Scan files in  user directory
        file_path = os.path.join(folder, file)  # Add path to every file
        if os.path.isdir(file_path):  # If the file by the file specified in file_path a folder, the function is
            # restarted with the new path
            for sub_file_path in find_files(file_path, key):
                yield sub_file_path
        elif os.path.isfile(file_path):  # If there is a part in the file name, the file path is returned
            if key in os.path.splitext(file):
                yield file_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", required=True, help='Folder to search in')
    parser.add_argument("--filename", required=True, help="Keyword to search for in file names")
    args = parser.parse_args()
    folder = args.folder  # Arguments to function find_files
    key = args.filename
    find_files(folder, key)
    for file_path in find_files(folder, key):
        print(file_path)

