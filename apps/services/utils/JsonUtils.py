import json

"""
JsonUtils
---------

Contains all methods to manipulate JSON files.
"""


def readJson(path) -> object:
    """
    Read the Json file matching the path given in parameter.
    :param path: String - Path to the file to read.
    :return: object - The content of the file.
    """
    with open(path) as f:
        data = json.load(f)
    return data
