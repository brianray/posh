#include "rule.hh"
#include "posh_errors.hh"



Rule::Rule(const char* rule) {

 this->original_rule = rule;

}

bool
Rule::check() {
    
 throw PoshException("could not parse rule");
 return true;

}


