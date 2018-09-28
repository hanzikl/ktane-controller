import sys, os

sys.path.append(os.path.abspath('..'))
from model.modules.simon_module import SimonModule
from model import Model
import unittest


class TranslateCommandOnKnownValues(unittest.TestCase):
    known_values_translations = (
        (True, 3, ['SMD 3 0 3 2 1 0 0', 'SMD 3 1 2 3 0 1 0', 'SMD 3 2 3 0 1 2 0']),
        (False, 1, ['SMD 1 0 1 3 2 0 0', 'SMD 1 1 0 2 1 3 0', 'SMD 1 2 2 3 0 1 0']),
        (True, 0, ['SMD 0 0 3 2 1 0 0', 'SMD 0 1 2 3 0 1 0', 'SMD 0 2 3 0 1 2 0']),
        (False, 7, ['SMD 7 0 1 3 2 0 0', 'SMD 7 1 0 2 1 3 0', 'SMD 7 2 2 3 0 1 0']),
    )

    def test_translations(self):
        """translate_to_commands should contain known result for given know module settings"""

        for boolpar, module_number, translation in self.known_values_translations:
            ktane_model = Model()
            ktane_model.serial_number_contains_vowel = boolpar
            simon_module = SimonModule(ktane_model)
            simon_module.number = module_number

            result = simon_module.translate_to_commands()

            for item in translation:
                self.assertTrue(item in result, "{} does not contain '{}'".format(result, item))


if __name__ == "__main__":
    unittest.main()
