"""This module handles errors from subprocess code errors"""
import subprocess
from colorama import Fore
from custom_types.error import Error

"""Global errors object (a list of errors)"""
ERRORS: list[Error] = Error.load_from_file("errors.json")


def errors(error, command_args: str, msg: str):
    """Function that handles errors"""
    error_found = False
    for i in range(len(ERRORS)):
        message = str(msg)
        list_of_commands = [i for i in command_args]

        if (ERRORS[i].code in message):
            option = get_option_if_any(
                name=error, command_args=list_of_commands)
            arguments = get_command_argument_if_any(
                command_args=list_of_commands)
            if (ERRORS[i].code == "2") or (ERRORS[i].code == "1"):
                if len(option) > 0:
                    for opt in option:
                        message = ERRORS[len(
                            ERRORS) - 1].output.replace("%1$", error).replace("%2$", "'" + opt[1:2] + "'")
                        print(f"{Fore.RED} {message} {Fore.RESET}")
                        error_found = True
                        break
                elif len(arguments) > 0:
                    message = ERRORS[i].output.replace("%1$", error)
                    for opt2 in arguments:
                        message = message.replace("%2$", opt2)
                        print(f"{Fore.RED} {message} {Fore.RESET}")
                else:
                    pass
                error_found = True
                break
            else:
                message = ERRORS[i].output.replace("%1$", error)
            print(f"{Fore.RED} {message} {Fore.RESET}")
            error_found = True
            break

    if not error_found:
        print(f"{Fore.RED} Unknown error {Fore.RESET}")


def get_option_if_any(name: str, command_args: list) -> list[str] | None:
    """Look for command options"""
    result = []
    temp = []

    for command in command_args:
        if command.startswith('-') and len(command) >= 2:
            result.append(command)

    for i in result:
        if i not in temp:
            temp.append(i)

    try:
        if len(temp) > 0:
            subprocess.check_call([name, " ".join(temp)],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNUL)
    except Exception:
        return (temp)

    return ([])


def get_command_argument_if_any(command_args: list) -> list[str] | None:
    """Look for command arguments"""
    result = []

    for command in command_args:
        if not command.startswith('-') or len(command) == 1:
            result.append(command)

    return (result)
