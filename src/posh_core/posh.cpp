
#include "train.hh"
#include <string>
#include <sstream>
#include <vector>

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}


std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, elems);
    return elems;
}

char * 
posh_prefligt_rule(char *rule) {

 char *out = "no";
 return out;

}


bool
posh_train(char *system, char *arg_list) {
  
  
  std::vector<std::string> args = split(arg_list, " ");
  
  int ret = train_citar_main("./data/brown-corpus", "lexicon", "ngrams");


  if (ret != -1)
     return true;

   return false;
}


