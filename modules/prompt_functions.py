"""All Functions that are connected to the prompt are here"""

import os
import re
import sys
from colorama import init, Fore


init()


# TODO: add auto complition for the commands using: readline ;)
def getline():
    """Function that shows the prompt"""
    cwd = os.getcwd()
    try:
        line = input(
            f"{Fore.YELLOW}{cwd}{Fore.RESET} {Fore.BLUE}->{Fore.RESET} "
        )
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)

    return line


def parseline(line):
    """Function that parses the line"""
    result = line.replace("\t", "")
    result = re.sub(r"\s{2,}", " ", result)
    result = result.replace("\r", "")
    result = result.split(" ")
    return result
