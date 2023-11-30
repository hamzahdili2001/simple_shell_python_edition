import json


class Error():
    """
    An object representation from errors.json file

    Attributes:
        - code (optional, str): error code of the command
        - output (optional, str): the message to show to the user
        - message (optional, str): the string to check along with @code from the error message
    """

    def __init__(self) -> None:
        self.code = None
        self.output = None
        self.message = None

    @classmethod
    def instance_from_file(cls, values: dict[str, str]):
        """Create an instance from a key / value kind of object"""
        instance = cls()
        for k, v in values.items():
            setattr(instance, k, v)
        return (instance)

    @staticmethod
    def load_from_file(file_path: str) -> list:
        """Load all errors as python objects from the file"""
        result = []
        contents = json.load(open(file=file_path, encoding="utf-8"))
        for i in range(len(contents)):
            result.append(Error.instance_from_file(contents[i]))
        return (result)
