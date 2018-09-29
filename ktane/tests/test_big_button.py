import sys, os

from ktane.model import Indicators

sys.path.append(os.path.abspath('..'))
from model.modules.big_button_module import BigButtonModule, ButtonColor, ButtonText
from model import Model
import unittest


class KnownCorrectBehaviourValues(unittest.TestCase):
    """ known button colors and texts with given environment
    """
    known_values_rules = (
        # all 7 rules
        ('blue', 'abort', 3, ['frk'], 1),
        ('red', 'detonate', 2, [], 0),
        ('white', 'detonate', 1, ['car', 'frk'], 1),
        ('yellow', 'press', 3, ['frk'], 0),
        ('yellow', 'press', 2, ['frk'], 1),
        ('red', 'hold', 0, [], 0),
        ('red', 'abort', 2, ['frk', 'car'], 1),
        # some random combinations
        ('yellow', 'abort', 1, ['car'], 1),
        ('blue', 'hold', 2, ['frk'], 1),
        ('yellow', 'detonate', 3, [], 0),
    )

    def test_get_correct_wire_known_values(self):
        """get_correct_wire should give known result for known value"""
        for color, text, batteries_count, indicators, behaviour in self.known_values_rules:
            ktane_model = Model()
            ktane_model.indicators = [Indicators(x) for x in indicators]
            ktane_model.batteries_count = batteries_count
            big_button_module = BigButtonModule(ktane_model)
            big_button_module.color = ButtonColor(color)
            big_button_module.text = ButtonText(text)

            result = big_button_module.get_correct_behaviour()
            self.assertEqual(behaviour, result.value)


class TranslateCommandOnKnownValues(unittest.TestCase):
    known_values_translations = (
    )

    def test_translations(self):
        """translate_to_commands should contain known result for given know module settings"""

        # TODO
        pass


if __name__ == "__main__":
    unittest.main()
