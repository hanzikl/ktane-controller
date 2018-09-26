import sys, os

sys.path.append(os.path.abspath('..'))
from model.modules.wires_module import WiresModule
from model import Model
import unittest


class KnownValues(unittest.TestCase):
    """ known sequences - colors or missing wire, and boolean parameter
        first wire has number 0
    """
    known_values_rules = (  # just random 3 wires
        (['red', 'white', 'blue', '', '', ''], True, 2),
        (['white', 'yellow', 'blue', '', '', ''], False, 1),
        (['', 'white', 'yellow', '', 'red', ''], True, 4),
        # all cases of 3 wires rules
        (['', '', '', 'yellow', 'yellow', 'blue'], False, 4),
        (['', 'red', 'red', 'white', '', ''], True, 3),
        (['blue', 'blue', 'red', '', '', ''], False, 1),
        (['', '', 'red', '', 'yellow', 'blue'], True, 5),
        # all cases of 4 wires rules
        (['red', '', 'red', '', 'yellow', 'blue'], True, 2),
        (['', 'white', '', 'yellow', 'blue', 'yellow'], True, 1),
        (['red', '', 'red', '', 'yellow', 'blue'], False, 0),
        (['', 'white', '', 'yellow', 'yellow', 'red'], True, 5),
        (['white', '', '', 'red', 'yellow', 'red'], False, 3),
        # all cases of 5 wires rules
        (['red', '', 'red', 'blue', 'yellow', 'black'], True, 4),
        (['blue', 'white', '', 'yellow', 'yellow', 'red'], False, 0),
        (['', 'red', 'red', 'white', 'yellow', 'blue'], False, 2),
        (['red', '', 'red', 'blue', 'yellow', 'black'], False, 0),
        (['white', 'blue', 'red', 'black', '', 'black'], False, 0),
        # all cases of 6 wires rules
        (['white', 'blue', 'red', 'black', 'blue', 'black'], True, 2),
        (['black', 'white', 'black', 'yellow', 'white', 'red'], False, 3),
        (['white', 'yellow', 'blue', 'yellow', 'white', 'black'], True, 5),
        (['red', 'black', 'red', 'blue', 'white', 'yellow'], True, 3),
        (['white', 'blue', 'red', 'black', 'blue', 'black'], False, 3),
    )

    def test_get_correct_wire_known_values(self):
        """get_correct_wire should give known result for known value"""
        for sequence, boolpar, number in self.known_values_rules:
            ktane_model = Model()
            ktane_model.serial_number_contains_vowel = boolpar
            wires_module = WiresModule(ktane_model)
            wires_module.wires_sequence = sequence

            result = wires_module.get_correct_wire()
            self.assertEqual(number, result)


class WiresSubroutines(unittest.TestCase):
    """known values for counting wires"""
    known_values_counting = (
        (['', '', '', '', '', ''], 0),
        (['red', '', '', '', '', ''], 1),
        (['', '', '', 'blue', '', ''], 1),
        (['red', 'white', 'blue', '', '', ''], 3),
        (['', '', 'red', '', 'yellow', 'blue'], 3),
        (['', 'white', '', 'yellow', 'yellow', 'red'], 4),
        (['red', '', 'red', '', 'yellow', 'blue'], 4),
        (['blue', '', 'red', 'yellow', 'yellow', 'blue'], 5),
        (['red', 'white', 'blue', 'white', 'red', 'blue'], 6)
    )

    """known_values_nth_wire"""
    known_values_nth = (
        (['', '', 'red', '', 'yellow', 'blue'], 2, 4),
        (['', 'white', '', 'yellow', 'yellow', 'red'], 4, 5),
        (['', 'white', '', 'yellow', 'yellow', 'red'], 4, 5),
        (['red', '', '', '', '', ''], 1, 0),
        (['blue', 'blue', 'red', '', '', ''], 2, 1),
        (['red', 'white', 'blue', 'white', 'red', 'blue'], 6, 5),
        (['red', 'white', 'blue', 'white', 'red', 'blue'], 4, 3),
    )

    def test_count_wires(self):
        """get_wires_count should give known result for known value"""

        ktane_model = Model()
        wires_module = WiresModule(ktane_model)

        for sequence, number in self.known_values_counting:
            wires_module.wires_sequence = sequence
            result = wires_module.get_wires_count()
            self.assertEqual(number, result)

    def test_nth_wire(self):
        """get_nth_wire should give known result for known value"""

        ktane_model = Model()
        wires_module = WiresModule(ktane_model)

        for sequence, n, number in self.known_values_nth:
            wires_module.wires_sequence = sequence
            result = wires_module.get_nth_wire_position(n)
            self.assertEqual(number, result)


if __name__ == "__main__":
    unittest.main()
