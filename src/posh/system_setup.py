import posh.core as core
import nltk
from os.path import join, exists, sep
import glob


def train(system, args):
    # citer corpus-train lexicon ngrams
    core.train(system, args)


def load_nltk_data_files(nltk_corpus_name, dpath="./data"):
    if not exists(dpath):
        raise IOError("No path found {}".format(dpath))
    if dpath not in nltk.data.path:
        nltk.data.path.append(dpath)
    nltk.download(nltk_corpus_name, download_dir=dpath, quiet=True)


FULL_SETUP = False
def full_setup(download=True):
    global FULL_SETUP
    if FULL_SETUP:
        return
    dpath = join(".", "data")
    if download:
        load_nltk_data_files("brown", dpath)
    brown_sub = join(dpath, "corpora", "brown")
    corpus = join(brown_sub, "brown_combined.txt")
    f = open(corpus, "wb")
    path_pattern = join(brown_sub, "c*")
    for afile in glob.glob(path_pattern):
        for line in open(afile, 'rb'):
            line = line.strip()
            if line == '':
                continue
            f.write(line)
    f.close()
    osep = sep
    arg_str = "{corpus} {dpath}{osep}lexicon {dpath}{osep}ngrams"
    train("citer", arg_str.format(**locals()))
    FULL_SETUP = True
