import unittest
from texter import Texter
 
class TestTexter(unittest.TestCase):

    texter = Texter()
 
    def test_units(self):
        units = {
            0: 'cero',
            # 1: 'uno',
            # 2: 'dos',
            # 3: 'tres',
            # 4: 'cuatro',
            # 5: 'cinco',
            # 6: 'seis',
            # 7: 'siete',
            # 8: 'ocho',
            # 9: 'nueve'
        }

        for unit, text in units.iteritems():
            self.assertEqual(self.texter.toText(unit), text)

if __name__ == '__main__':
    unittest.main()