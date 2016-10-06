import unittest
from texter import Texter
 
class TestTexter(unittest.TestCase):

    texter = Texter()
 
    def test_function(self):
        self.assertEqual(self.texter.toText(42), None)

if __name__ == '__main__':
    unittest.main()