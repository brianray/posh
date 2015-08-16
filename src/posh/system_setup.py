import posh.core as core
import nltk
from os.path import join, exists
import glob


def train(system, args):
    # citer corpus-train lexicon ngrams
    core.train(system, args)


def load_nltk_data_files(nltk_corpus_name, data_path="./data"):
    if not exists(data_path):
        raise IOError("No path found {}".format(data_path))
    if data_path not in nltk.data.path:
        nltk.data.path.append(data_path)
    nltk.download(nltk_corpus_name, download_dir=data_path, quiet=True)


def full_setup():
    data_path = join(".", "data")
    load_nltk_data_files("brown", data_path)
    brown_sub = join(data_path, "corpora", "brown")
    brown_corpus = join(brown_sub, "brown_combined.txt")
    f = open(brown_corpus, "wb")
    path_pattern = join(brown_sub, "c*")
    for afile in glob.glob(path_pattern):
        for line in open(afile, 'rb'):
            line = line.strip()
            if line == '':
                continue
            f.write(line)
    f.close()
    train("citer", "{} lexicon ngrams".format(brown_corpus))
