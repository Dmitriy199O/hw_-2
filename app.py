from flask import Flask, request, render_template, send_from_directory
from functions import load_posts, upload_post
import logging
from main.main_views import main_blueprint
from loader.loader_views import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

logging.basicConfig(encoding='utf-8', level=logging.INFO)

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route(f'/post/upload/<path:path>/')
def static_dir(path):
    return send_from_directory('uploads/images/', path)


app.run(debug=True)

