"""All function that runs command or execute command are here"""
import subprocess
from .external_commands import *


def run_command(command):
    """function that returns a executed command"""
    return subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )


def run_external_commands(command):
    """Function that excute commands and have external commands if the command
    not a built-in"""
    external_commands = {
        "cd": cd_command,
        "exit": exit_command,
        "pwd": pwd_command,
    }

    command_name = command[0]
    command_args = command[1:]

    if command_name in external_commands:
        external_commands[command_name](command_args)
    else:
        try:
            run = run_command(command)
            print(run.stdout)
        except Exception as e:
            print("An unexpected error occurred:", str(e))
