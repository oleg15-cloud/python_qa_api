import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_list_of_breeds():
    with open(f"{dir_path}/breeds.json", "r") as file_breeds:
        breeds = json.loads(file_breeds.read())
    return [breed for breed in breeds]


list_of_breeds = get_list_of_breeds()
