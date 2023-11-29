# this code here generate command for the autocompletion.

"""
import re
import json
import subprocess

output = subprocess.check_output(["apropos", "-s", "4", ""])

pattern = r"^(.*?) \((\d+)\)\s+- (.*)$"

data = []

for line in output.decode().splitlines():
    # Match the regex pattern against each line
    match = re.match(pattern, line)
    if match:
        command = match.group(1)
        section = match.group(2)
        description = match.group(3)

        entry = {
            "command": command,
            "description": description,
            "section": section,
        }

        data.append(entry)

with open("cmd_sections_4.json", "w") as file:
    json.dump(data, file)
"""

import re
import json
import subprocess

data = []

for section in range(1, 9):  # Iterate through sections 1 to 8
    output = subprocess.check_output(["apropos", "-s", str(section), ""])

    pattern = r"^(.*?) \((\d+)\)\s+- (.*)$"

    for line in output.decode().splitlines():
        # Match the regex pattern against each line
        match = re.match(pattern, line)
        if match:
            command = match.group(1)
            section = match.group(2)
            description = match.group(3)

            entry = {
                "command": command,
                "description": description,
                "section": section,
            }

            data.append(entry)

with open("cmd_sections_all.json", "w") as file:
    json.dump(data, file)
