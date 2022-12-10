import logging

from flask import Blueprint, request, render_template, send_from_directory
from functions import load_posts, save_posts

load_blueprint = Blueprint("load_blueprint", __name__, template_folder='templates')
logging.basicConfig(level=logging.INFO)


@load_blueprint.route("/post_form")
def load_page():
    return render_template('post_form.html')


@load_blueprint.route('/upload', methods=['POST'])
def save_page():
    try:
        picture = request.files.get("picture")
    except:
        logging.error("Ошибка при загрузке файла")
        return '<h1>Ошибка загрузки</h1>'

    if not picture:
        logging.info("Файл не загружен")
        return f'<h1>Файл не загружен</h1>'

    filename = picture.filename
    extension = filename.split(".")[-1]
    if extension not in ['jpg', 'png', 'jpeg']:
        logging.info("Неверный формат файла")
        return f'<h1>Неверный формат файла</h1>'

    picture.save(f"./uploads/{filename}")
    content = request.form.get('content')

    posts = load_posts()
    new_post = {'pic': f"/uploads/{filename}", 'content': content}
    posts.append(new_post)
    save_posts(posts)

    return render_template('post_uploaded.html', pic=f"/uploads/{filename}", content=content)


@load_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
