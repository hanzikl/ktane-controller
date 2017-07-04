import sys, os
sys.path.append(os.path.abspath('..'))
from Model.Modules import WiresModule
import unittest


class KnownValues(unittest.TestCase):
    ''' known sequences - colors or missing wire, first wire has number 0'''
    known_values = ( (['RED', 'WHITE', 'BLUE', 'MISSING', 'MISSING', 'MISSING'], 2),
                     (['WHITE', 'YELLOW', 'BLUE', 'MISSING', 'MISSING', 'MISSING', 1]))


    def test_get_correct_wire_known_values(self):
        '''get_correct_wire should give known result for known value'''
        for sequence, number in self.known_values:
            result = WiresModule.get_correct_wire(sequence)
            self.assertEqual(number, result)

if __name__ == "__main__":
    unittest.main()
 
