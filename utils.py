import json
from os.path import getsize
from random import randint


def data():
    with open("data.json") as file:
        data = json.load(file)
    return data


def getSize():
    return getsize("data.json")


def getRandomData():
    return data()[randint(1, 97)]
