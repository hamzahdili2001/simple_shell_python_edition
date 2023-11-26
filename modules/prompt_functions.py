"""All Functions that are connected to the prompt are here"""

import os
import re


def getline():
    """Function that shows the prompt"""
    cwd = os.getcwd()
    line = input(f"{cwd} -> ")

    return line


def parseline(line):
    """Function that parses the line"""
    result = line.replace("\t", "")
    result = re.sub(r"\s{2,}", " ", result)
    result = result.replace("\r", "")
    result = result.split(" ")
    return result
