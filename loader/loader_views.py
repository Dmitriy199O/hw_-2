from flask import Blueprint, request, render_template
from functions import load_posts, upload_post
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)

loader_blueprint = Blueprint('loader_blueprint', __name__, url_prefix='/post/', template_folder='templates',
                             static_folder='static')


@loader_blueprint.route('/form/')
def form_page():
    return render_template('post_form.html')


@loader_blueprint.route('/upload/', methods=["POST"])
def upload_page():
    ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif']
    try:
        file = request.files['picture']
        filename = file.filename
        file_extension = filename.split('.')[-1]
        if file_extension not in ALLOWED_EXTENSIONS:
            logging.info(f"Загружаемый файл имеет запрещённое расширение {file_extension}")
            raise TypeError(f"Загружаемый файл имеет запрещённое расширение {file_extension} ")  #

        logging.info(f'имя файла:{filename}')
        content = request.values['content']
        logging.info(f'текст поста:{content}')
        post = {'pic': f'/post/upload/{filename}',
            'content': content}
        posts = load_posts()
        posts.append(post)

        upload_post(posts)
        file.save(f'uploads/images/{filename}')
    except FileNotFoundError:
        logging.error("Ошибка при загрузке файла")
        return 'Ошибка при загрузке файла'
    else:
        return render_template('post_uploaded.html', post=post)
