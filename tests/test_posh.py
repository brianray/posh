from __future__ import print_function  # noqa
import unittest
import posh
from os.path import exists
import os


download = True


class CleaningMixin(object):

    files = ('data/ngrams',
             'data/lexicon')

    def clean_up(self):
        for f in self.files:
            try:
                os.unlink(f)
            except Exception as ex:
                print(str(ex))
                print("could not unlink {}".format(f))


class PoshSetupTests(unittest.TestCase, CleaningMixin):

    def setUp(self):
        self.clean_up()

    def tearDown(self):
        self.clean_up()

    def test_setup(self):
        posh.setup(download=download)
        for f in self.files:
            self.assertTrue(exists(f),
                            "{} should exist".format(f))


class PoshTests(unittest.TestCase, CleaningMixin):

    def setUp(self):
        posh.setup(download=download)

    def tearDown(self):
        self.clean_up()

    def test_rule(self):
        """ Rule should match 'not injured'"""
        session = posh.Session(syntax="stem")
        session.addRule("not_injured",
                        "SENT: RB(not) & VBN(injured) => true")
        not_injured_hash_id = session.addTarget("I was not injured.")
        injured_hash_id = session.addTarget("I was injured.")
        session.run_rules()
        self.assertTrue(session.getResult(not_injured_hash_id))
        self.assertFalse(session.getResult(injured_hash_id))
        session.close()


if __name__ == '__main__':
    try:
        unittest.main(buffer=True)
    except Exception as e:
        import pdb
        pdb.set_trace()
