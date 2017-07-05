import sys, os

sys.path.append(os.path.abspath('..'))
from Model.Modules import WiresModule
import unittest


class KnownValues(unittest.TestCase):
    """ known sequences - colors or missing wire, and boolean parameter
        first wire has number 0
    """
    known_values_rules = (  # just random 3 wires
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

    """known values for counting wires"""
    known_values_counting = (
        (['missing', 'missing', 'missing', 'missing', 'missing', 'missing'], 0),
        (['red', 'missing', 'missing', 'missing', 'missing', 'missing'], 1),
        (['missing', 'missing', 'missing', 'blue', 'missing', 'missing'], 1),
        (['red', 'white', 'blue', 'missing', 'missing', 'missing'], 3),
        (['missing', 'missing', 'red', 'missing', 'yellow', 'blue'], 3),
        (['missing', 'white', 'missing', 'yellow', 'yellow', 'red'], 4),
        (['red', 'missing', 'red', 'missing', 'yellow', 'blue'], 4),
        (['blue', 'missing', 'red', 'yellow', 'yellow', 'blue'], 5),
        (['red', 'white', 'blue', 'white', 'red', 'blue'], 6)
    )

    def test_get_correct_wire_known_values(self):
        """get_correct_wire should give known result for known value"""
        for sequence, boolpar, number in self.known_values_rules:
            result = WiresModule.get_correct_wire(sequence, boolpar)
            self.assertEqual(number, result)

    def test_count_wires(self):
        """get_wires_count should give known result for known value"""
        for sequence, number in self.known_values_counting:
            result = WiresModule.get_wires_count(sequence)
            self.assertEqual(number, result)


if __name__ == "__main__":
    unittest.main()
