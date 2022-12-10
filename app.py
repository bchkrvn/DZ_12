from flask import Flask, request, render_template, send_from_directory
from main.main import main_blueprint
from loader.loader import load_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(load_blueprint)

app.run(debug=True)

