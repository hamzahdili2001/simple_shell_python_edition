"""All function that runs command or execute command are here"""
import subprocess
from .external_commands import *

external_commands = {
    "cd": cd_command,
    "exit": exit_command,
    "pwd": pwd_command,
}


def run(command):
    """runs command: external commands or internal commands"""
    command_name = command[0]
    command_args = command[1:]
    internal_command = None
    try:
        internal_command = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except subprocess.SubprocessError as e:
        print(f"Error: {e}")

    if command_name in external_commands:
        external_commands[command_name](command_args)
    elif internal_command is not None:
        print(internal_command.stdout)
