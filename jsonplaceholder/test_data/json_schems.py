schema_of_post = {
    "userId": {"type": "integer"},
    "id": {"type": "integer"},
    "title": {"type": "string"},
    "body": {"type": "string"}
}
schema_of_comment = {
    "postId": {"type": "integer"},
    "id": {"type": "integer"},
    "name": {"type": "string"},
    "email": {"type": "string"},
    "body": {"type": "string"}
}
