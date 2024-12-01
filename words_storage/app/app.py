from flask import Flask

from db.database import init_db
from routes.words import words_core


def create_app():
    app = Flask(__name__)
    with app.app_context():
        init_db()
    app.register_blueprint(words_core)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
