class Word:
    def __init__(self, original, translation, meta):
        self.original = original
        self.translation = translation
        self.meta = meta

    def to_dict(self):
        return {
            'original': self.original,
            'translation': self.translation,
            'meta': self.meta
        }
