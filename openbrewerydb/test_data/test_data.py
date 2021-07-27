import os

from csv import DictReader

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_list_cities():
    with open(f"{dir_path}/breweries.csv", "r") as breweries_csv:
        breweries_json = DictReader(breweries_csv)
        return [brewery["city"] for brewery in breweries_json]


def get_list_names():
    with open(f"{dir_path}/breweries.csv", "r") as breweries_csv:
        breweries_json = DictReader(breweries_csv)
        return [brewery["name"] for brewery in breweries_json]


def get_list_id():
    with open(f"{dir_path}/breweries.csv", "r") as breweries_csv:
        breweries_json = DictReader(breweries_csv)
        return [brewery["id"] for brewery in breweries_json]


def get_list_types():
    with open(f"{dir_path}/breweries.csv", "r") as breweries_csv:
        breweries_json = DictReader(breweries_csv)
        return [brewery["brewery_type"] for brewery in breweries_json]


cities = get_list_cities()
names = get_list_names()
breweries_id = get_list_id()
breweries_type = get_list_types()
