import sys, os

from ktane.model import Indicators

sys.path.append(os.path.abspath('..'))
from model.modules.big_button_module import BigButtonModule, ButtonColor, ButtonText, StripColor
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

    def test_get_correct_behaviour_known_values(self):
        """get_correct_behaviour should give known result for known value"""
        for color, text, batteries_count, indicators, behaviour in self.known_values_rules:
            ktane_model = Model()
            ktane_model.indicators = [Indicators(x) for x in indicators]
            ktane_model.batteries_count = batteries_count
            big_button_module = BigButtonModule(ktane_model)
            big_button_module.color = ButtonColor(color)
            big_button_module.text = ButtonText(text)

            result = big_button_module.get_correct_behaviour()
            self.assertEqual(behaviour, result.value)


class KnownStripColorAndDigitValues(unittest.TestCase):
    """ known strip colors"""
    known_strip_colors_and_digits_rules = (
        # all 4 rules
        ('blue', 4),
        ('white', 1),
        ('yellow', 5),
        ('red', 1),
    )

    def test_get_correct_digit_known_values(self):
        """get_correct_digit should give known result for known value"""
        for color, digit in self.known_strip_colors_and_digits_rules:
            ktane_model = Model()
            big_button_module = BigButtonModule(ktane_model)

            result = big_button_module.get_correct_digit(StripColor(color))
            self.assertEqual(digit, result)


class TranslateCommandOnKnownValues(unittest.TestCase):
    known_values_translations = (
        ('blue', 'abort', 3, ['frk'], ['white', 'red', 'blue'], 0,
         ['SMD 0 0 49 65 20 0 0']),
        ('red', 'detonate', 2, [], [None, None, None], 8,
         ['SMD 8 0 0 0 0 0 0']),
        ('red', 'abort', 2, ['frk', 'car'], ['blue', 'red', 'yellow'], 3,
         ['SMD 3 0 20 65 37 0 0']),
    )

    def test_translations(self):
        """translate_to_commands should contain known result for given know module settings"""

        for color, text, batteries, indicators, strip_colors, module_number, translation \
                in self.known_values_translations:
            ktane_model = Model()
            ktane_model.indicators = [Indicators(x) for x in indicators]
            ktane_model.batteries_count = batteries

            module = BigButtonModule(ktane_model)
            module.color = ButtonColor(color)
            module.text = ButtonText(text)
            module.number = module_number
            module.strip_colors = [(lambda x: None if x is None else StripColor(x))(x) for x in strip_colors]

            result = module.translate_to_commands()

            for item in translation:
                self.assertTrue(item in result, "{} does not contain '{}'".format(result, item))


if __name__ == "__main__":
    unittest.main()
