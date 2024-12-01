from flask import Blueprint, jsonify

from db.database import get_db
from db.serializers import parse_word
from models.word import Word

from db.database import EXISTS_TABLE

words_core = Blueprint('words_core', __name__)


@words_core.route('/add_word/<from_lang>_<to_lang>', methods=['POST'])
def add_word(from_lang, to_lang):
    word = parse_word()
    db = get_db()
    cursor = db.cursor()
    db_name = 'words_{}_{}'.format(from_lang, to_lang)
    if db_name not in EXISTS_TABLE:
        return jsonify({"message": "Not supported language"}), 404

    cursor.execute(
        'INSERT INTO {} (original, translation, meta) VALUES (?, ?, ?)'.format(db_name),
        (word.original, word.translation, str(word.meta))
    )
    db.commit()
    return jsonify({"message": "Word added successfully!"}), 201


@words_core.route('/translate/<from_lang>_<to_lang>/<original>', methods=['GET'])
def translate(from_lang, to_lang, original):
    db = get_db()
    cursor = db.cursor()
    db_name = 'words_{}_{}'.format(from_lang, to_lang)
    if db_name not in EXISTS_TABLE:
        return jsonify({"message": "Not supported language"}), 404

    cursor.execute('SELECT * FROM {} WHERE original = ?'.format(db_name), (original,))
    row = cursor.fetchone()

    if row is None:
        return jsonify({"message": "Word not found."}), 404

    word = Word(row['original'], row['translation'], row['meta'])
    return jsonify(word.to_dict())
