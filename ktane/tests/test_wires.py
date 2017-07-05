import sys, os

sys.path.append(os.path.abspath('..'))
from Model.Modules import WiresModule
import unittest


class KnownValues(unittest.TestCase):
    """ known sequences - colors or missing wire, and boolean parameter
        first wire has number 0
    """
    known_values = (  # just random 3 wires
        (['red', 'white', 'blue', 'missing', 'missing', 'missing'], True, 2),
        (['white', 'yellow', 'blue', 'missing', 'missing', 'missing'], False, 1),
        (['missing', 'white', 'yellow', 'missing', 'red', 'missing'], True, 4),
        # all cases of 3 wires rules
        (['missing', 'missing', 'missing', 'yellow', 'yellow', 'blue'], False, 4),
        (['missing', 'red', 'red', 'white', 'missing', 'missing'], True, 3),
        (['blue', 'blue', 'red', 'missing', 'missing', 'missing'], False, 2),
        (['missing', 'missing', 'red', 'missing', 'yellow', 'blue'], True, 5),
        # all cases of 4 wires rules
        (['red', 'missing', 'red', 'missing', 'yellow', 'blue'], True, 2),
        (['missing', 'white', 'missing', 'yellow', 'blue', 'yellow'], True, 1),
        (['red', 'missing', 'red', 'missing', 'yellow', 'blue'], False, 0),
        (['missing', 'white', 'missing', 'yellow', 'yellow', 'red'], True, 5),
        (['white', 'missing', 'missing', 'red', 'yellow', 'red'], False, 3),
    )

    def test_get_correct_wire_known_values(self):
        """get_correct_wire should give known result for known value"""
        for sequence, boolpar, number in self.known_values:
            result = WiresModule.get_correct_wire(sequence, boolpar)
            self.assertEqual(number, result)


if __name__ == "__main__":
    unittest.main()
