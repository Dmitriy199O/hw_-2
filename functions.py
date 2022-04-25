import json

POST_PATH = 'posts.json'


def load_posts():
    try:
        with open(POST_PATH, 'r', encoding='utf-8') as f:
            posts = json.load(f)
            return posts
    except FileNotFoundError:
        return 'Ошибка. Файл json не найден'

    except ValueError:
        return 'Ошибка чтения файла'


def upload_post(posts):
    try:
        with open(POST_PATH, 'w', encoding='utf-8') as file:
            json.dump(posts, file, ensure_ascii=False, indent=4)

    except FileNotFoundError:
        return 'Ошибка. Файл json не найден'

    except ValueError:
        return 'Ошибка чтения файла'
