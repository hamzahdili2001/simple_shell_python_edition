"""All external commands function will be in this file"""

import os
import sys


def cd_command(args):
    """Function that execute cd command"""
    try:
        os.chdir(args[0])
    except IndexError:
        print("cd: missing argument")
    except FileNotFoundError:
        print(f"cd: no such file or directory: [{args[0]}]")


def exit_command(args):
    """Function that exits the shell"""
    sys.exit(args[0] if args else 0)
