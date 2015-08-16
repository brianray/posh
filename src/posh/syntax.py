import core


class Syntax(object):
    """ handles loading a syntax """

    def __init__(self, name):
        self.load(name)

    def load(self, name):
        if name == "wordnet":
            from nltk.corpus import wordnet as wn
            import pdb
            pdb.set_trace()
            print wn.__dict__
            core.load_corpus('a')
