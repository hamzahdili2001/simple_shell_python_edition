"""All function that runs command or execute command are here"""
from os import error
import subprocess
from .external_commands import *
from colorama import init, Fore
from .file_support import handle_file_argument

init()

# TODO: add all the commands needed
external_commands = {
    "cd": cd_command,
    "exit": exit_command,
}


# TODO: move this to a proper file for handing output.
def errors(error, msg):
    """Function that handles errors"""
    print(f"{Fore.RED} {error}: {msg} {Fore.RESET}")


def run(command):
    """runs command: external commands or internal commands"""
    command_name = command[0]
    command_args = command[1:]
    internal_command = None

    try:
        if command_name not in external_commands:
            internal_command = subprocess.run(
                # INFO: using string command with 'shell=True'
                # may lead to  shell injection vulnerabilities.
                " ".join(map(str, command)),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True,
                shell=True,
            )
    except subprocess.CalledProcessError as e:
        errors(command_name, e)
    except subprocess.SubprocessError as e:
        errors(command_name, e)
    except (KeyboardInterrupt, EOFError):
        sys.exit(0)
    except FileNotFoundError:
        errors(command_name, "The command does not exist")
    if command_name in external_commands:
        external_commands[command_name](command_args)
    elif internal_command is not None:
        print(internal_command.stdout)
    else:
        # TODO: add some propter message.
        pass


def run_from_file():
    """run a list of commands comes form a file"""
    commands = handle_file_argument()
    if commands == -1:
        return -1
    for command in commands:
        command = command.split(" ")  # make the command an array again
        run(command)
    return 0
