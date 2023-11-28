"""Support of command from file"""

from os.path import isfile
import sys


def read_file(file):
    """Function that read from a file"""
    commands_list = []
    with open(file, "r", encoding="UTF-8") as f:
        for line in f:
            commands_list.append(line.strip())

    return commands_list


# TODO: handle a proper errors
def handle_file_argument():
    """Function that handle file argument"""
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        if isfile(file_path):
            return read_file(file_path)
        print(f"{file_path}: is not a file")
    else:
        print("Error: too many arguments")
    return -1
