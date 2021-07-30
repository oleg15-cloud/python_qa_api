import pytest
import requests
import cerberus

from jsonplaceholder.test_data.json_schems import schema_of_post, schema_of_comment
from jsonplaceholder.test_data.test_data import posts_id


def test_get_100_posts(base_url):
    response = requests.get(f"{base_url}/posts").json()
    assert len(response) == 100


def test_check_schema_of_posts(base_url):
    response = requests.get(f"{base_url}/posts").json()
    v = cerberus.Validator()
    for post in response:
        assert v.validate(post, schema_of_post), f"{v.errors}"


def test_create_new_post(base_url):
    json_post = {
        "title": "Automation Python",
        "body": "Body Body Body",
        "userId": 6351
    }
    response = requests.post(f"{base_url}/posts", json=json_post).json()
    assert response["userId"] == json_post["userId"] and response["title"] == json_post["title"] and \
           response["body"] == json_post["body"]


@pytest.mark.parametrize("post_id", posts_id)
def test_get_post_by_id(base_url, post_id):
    response = requests.get(f"{base_url}/posts/{post_id}").json()
    assert response["id"] == post_id


@pytest.mark.parametrize("post_id", posts_id)
def test_get_post_comments(base_url, post_id):
    response = requests.get(f"{base_url}/posts/{post_id}/comments").json()
    v = cerberus.Validator()
    for comment in response:
        assert v.validate(comment, schema_of_comment), f"{v.errors}"
