
#include "train.hh"
#include "rule.hh"
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

bool 
posh_prefligt_rule(char *rule) {
    Rule *rule_obj = new Rule(rule);
    return rule_obj->check();
}

bool
posh_train(char *system, char *arg_list) {
  std::vector<std::string> args = split(arg_list, ' ');
  int ret = train_citar_main(args[0].c_str(), args[1].c_str(), args[2].c_str());
  if (ret != -1)
     return true;
   return false;
}


