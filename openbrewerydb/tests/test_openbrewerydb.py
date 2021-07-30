import pytest
import requests
import cerberus

from openbrewerydb.test_data.test_data import cities, names, breweries_id, breweries_type
from openbrewerydb.test_data.schema_brewery import schema_brewery_obj


def test_get_list_breweries(base_url):
    response = requests.get(f"{base_url}/breweries").json()
    validator = cerberus.Validator()
    for brewery in response:
        assert validator.validate(brewery, schema_brewery_obj), f"{validator.errors}"


@pytest.mark.parametrize("city", cities)
def test_get_breweries_by_city(base_url, city):
    payload = {'by_city': city}
    response = requests.get(f"{base_url}/breweries", params=payload).json()
    for brewery in response:
        assert brewery["city"] == city


@pytest.mark.parametrize("name", names)
def test_get_breweries_by_name(base_url, name):
    payload = {'by_name': name}
    response = requests.get(f"{base_url}/breweries", params=payload).json()
    for brewery in response:
        assert brewery["name"] == name


@pytest.mark.parametrize("brewery_id", breweries_id)
def test_get_brewery(base_url, brewery_id):
    response = requests.get(f"{base_url}/breweries/{brewery_id}").json()
    assert response["id"] == int(brewery_id)


@pytest.mark.parametrize("brewery_type", breweries_type)
def test_get_breweries_by_type(base_url, brewery_type):
    payload = {'by_type': brewery_type}
    response = requests.get(f"{base_url}/breweries", params=payload).json()
    for brewery in response:
        assert brewery["brewery_type"] == brewery_type
