import posh


class Syntax(object):
    """ handles loading a syntax """

    def __init__(self, name):
        self.load(name)

    def load(self, name):
        if name == "wordnet":
            from nltk.corpus import wordnet as wn  # noqa
            posh.core.load_corpus('a')
