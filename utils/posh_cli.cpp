
#include <iostream>
#include "posh.h"


int main(int argc, const char * argv[]) {
    bool ret =  posh_train("citar", "/Users/rayb/src/posh/data/corpora/brown/brown_combined.txt lexicon ngrams");
}
