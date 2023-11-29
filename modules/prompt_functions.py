"""All Functions that are connected to the prompt are here"""

import os
import re
import sys
from .suggestions import suggestions
from prompt_toolkit import prompt


# TODO: add auto complition for the commands using: readline ;)
def getline():
    """Function that shows the prompt"""
    cwd = os.getcwd()

    prompt_str = f"{cwd} -> "
    try:
        line = prompt(
            prompt_str,
            completer=suggestions(),
            complete_while_typing=True,
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
