"""All function that runs command or execute command are here"""
import subprocess
from .external_commands import *

# TODO: add all the commands needed
external_commands = {
    "cd": cd_command,
    "exit": exit_command,
}


def run(command):
    """runs command: external commands or internal commands"""
    command_name = command[0]
    command_args = command[1:]
    internal_command = None

    try:
        if command_name not in external_commands:
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
    except (KeyboardInterrupt, EOFError):
        sys.exit(0)
    except FileNotFoundError:
        print(f"{command_name}: the command does not exist.")

    if command_name in external_commands:
        external_commands[command_name](command_args)
    elif internal_command is not None:
        print(internal_command.stdout)
    else:
        # TODO: add some propter message.
        print("error!!!")
