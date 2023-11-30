"""auto completion implementation"""
import json

"""
# TODO: Make it auto complete directories and files if the command already
# exists, and get the system command in a proper dynaminc way.
# also, implement some proper logic
# add: autocompletion for the options too.
"""


def auto_complete(text, state):
    """Function that implement auto completion based on json file"""
    file_path = "commands_data/cmd_sections_all.json"

    with open(file_path, "r", encoding="UTF-8") as file:
        data = file.read()

    options = json.loads(data)

    # Find the maximum length of the command strings
    max_command_length = max(len(item["command"]) for item in options)

    # Create a list of formatted strings for each command and description
    formatted_options = [
        f"{item['command']} {' ' * (max_command_length - len(item['command']))} {item['description']}"
        for item in options
    ]

    if not text:
        return formatted_options[state]

    # Filter matches based on the input text
    matches = [
        option for option in formatted_options if option.startswith(text)
    ]

    if len(matches) == 1:
        # If there's only one match, complete only the command
        return matches[state].split()[0]
    elif state < len(matches):
        # If there are multiple matches, show the entire formatted string on the second Tab press
        return matches[state]
    else:
        return None
