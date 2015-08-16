import unittest
import posh


class PoshTests(unittest.TestCase):

    def xtest_rule(self):
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

    def test_setup(self):
        """ Rule should match 'not injured'"""
        posh.setup()


if __name__ == '__main__':
    try:
        unittest.main(buffer=True)
    except Exception, e:
        import pdb
        pdb.set_trace()