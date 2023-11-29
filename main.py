#!/usr/bin/env python3
"""Main program"""
from modules.prompt_functions import *
from modules.external_commands import *
from modules.run_functions import *
import sys
from modules.run_functions import run_from_file
import readline
from modules.completion import *


def main():
    """the main function that runs everything"""
    if len(sys.argv) > 1:
        run_from_file()
    else:
        readline.set_completer(auto_complete)
        readline.parse_and_bind("ctrl: complete")

        while True:
            line = getline()
            command = parseline(line)

            if not command:
                continue
            run(command)


if __name__ == "__main__":
    main()
