
import posh.core as core


class Session(object):

    """This is the main POS session handleraddRule

        Attributes:
            syntax (str): stores the `syntax` name.

    """

    def __init__(self, syntax):
        """
        Args:
            syntax (str): Should be a known `syntax` like 'wordnet'.
        """
        self.syntax = syntax
        self.rules = {}

    def addRule(self, rule_handle, rule):
        self.rules[rule_handle] = rule
        result = core.prefligt_rule(rule)
        if result != 'OK':
            raise Exception(result)

    def addTarget(self):
    	pass
