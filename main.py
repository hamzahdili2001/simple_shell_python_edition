#!/usr/bin/env python3

from modules.prompt_functions import *
from modules.external_commands import *
from modules.run_functions import *


def main():
    """the main function that runs everything"""
    while True:
        line = getline()
        command = parseline(line)

        if not command:
            continue

        run_external_commands(command)


if __name__ == "__main__":
    main()
