from flask import request

from models.word import Word


def parse_word():
    data = request.json
    return Word(
        original=data.get('original'),
        translation=data.get('translation'),
        meta=data.get('meta', {})
    )
