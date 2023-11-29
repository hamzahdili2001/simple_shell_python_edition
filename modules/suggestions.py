from prompt_toolkit.completion import WordCompleter
import json


def suggestions():
    """Function uses prompt_toolkit to implement auto suggestions"""
    file_path = "commands_data/cmd_sections_all.json"
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    commands = [entry["command"] for entry in data]

    completer = WordCompleter(commands)

    return completer
