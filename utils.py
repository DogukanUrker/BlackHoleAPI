import json
from os.path import getsize


def data():
    with open("data.json") as file:
        data = json.load(file)
    return data


def getSize():
    return getsize("data.json")
