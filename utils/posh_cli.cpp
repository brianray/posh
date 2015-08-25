
#include <iostream>
#include "posh.h"


int main(int argc, const char * argv[]) {
    bool ret =  posh_train("citar", "data/corpora/brown/brown_combined.txt lexicon ngrams");
    bool ret2 = posh_preflight_rule("SENT: RB(not) & VBN(injured) => true");
     
}
