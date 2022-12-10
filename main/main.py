import logging

from flask import Blueprint, request, render_template
from functions import load_posts

main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')
logging.basicConfig(level=logging.INFO)

@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    logging.info("Выполняется поиск")
    letters = request.args.get('s').lower()

    posts = load_posts()
    need_posts = [post for post in posts if letters in post['content']]
    return render_template('post_list.html', user_letters=letters, posts=need_posts)
