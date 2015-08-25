#ifndef POSH_RULE_H
#define POSH_RULE_H

class Rule
{
    public:
        Rule(const char* rule);
        bool check();

    private:
        const char* original_rule;
};


#endif



