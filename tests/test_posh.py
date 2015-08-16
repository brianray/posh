import unittest
import posh


class PoshTests(unittest.TestCase):

    def test_rule(self):
        """ Rule should match 'not injured'"""
        session = posh.Session(syntax="wordnet")
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
    except Exception, e:
        import pdb
        pdb.set_trace()