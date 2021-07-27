import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_posts_id():
    with open(f"{dir_path}/posts.json", "r") as posts_json_file:
        posts = json.loads(posts_json_file.read())
        return [post["id"] for post in posts]


posts_id = get_posts_id()
