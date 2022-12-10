import json

POSTS_FILE = "posts.json"


def load_posts() -> list:
    with open(POSTS_FILE, encoding='utf-8') as file:
        posts = json.load(file)

    return posts


def save_posts(posts: list) -> None:
    with open(POSTS_FILE, 'w', encoding='utf-8') as file:
        json.dump(posts, file)