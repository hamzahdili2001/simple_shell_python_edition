import json
from colorama import Fore

ERRORS = json.load(open("errors.json", "r", encoding="utf-8"))


def errors(error, msg: str):
    """Function that handles errors"""
    error_found = False
    for e in ERRORS:
        temp = [(k, v) for k, v in dict(e).items()]
        message = str(msg)

        if (temp[0][0] in message):
            message = temp[0][1].replace("%1$", error)
            print(f"{Fore.RED} {message} {Fore.RESET}")
            error_found = True
            break
        
    if not error_found:
        print(f"{Fore.RED} Unknown error {Fore.RESET}")
