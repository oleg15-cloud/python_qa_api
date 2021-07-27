import random
import requests


def test_get_list_all_of_breeds(base_url):
    response = requests.get(f"{base_url}/api/breeds/list/all")
    assert response.ok and response.json()["status"] == "success"


def test_get_random_image(base_url):
    random_image1 = requests.get(f"{base_url}/api/breeds/image/random").json()
    random_image2 = requests.get(f"{base_url}/api/breeds/image/random").json()
    assert random_image1["message"] != random_image2["message"]


def test_get_some_random_images(base_url, count_images=random.randint(1, 50)):
    response = requests.get(f"{base_url}/api/breeds/image/random/{count_images}").json()
    assert len(response["message"]) == count_images


def test_get_images_by_breed(base_url, param_fixture):
    response = requests.get(f"{base_url}/api/breed/{param_fixture}/images").json()
    assert len(response["message"]) >= 1


def test_get_random_image_by_breed(base_url, param_fixture):
    response = requests.get(f"{base_url}/api/breed/{param_fixture}/images/random").json()
    assert param_fixture in response["message"]
