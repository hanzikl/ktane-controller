import sys, os

sys.path.append(os.path.abspath('..'))
from model.modules.abstract_module import AbstractModule, ModuleState
from model import Model
import unittest


class TranslateCommandOnKnownValues(unittest.TestCase):
    known_values_translations = (
        (0, 0,  ModuleState.ARMED, ['SMT 0 -1', 'SMS 0 2']),
        (1, 0, ModuleState.DISARMED, ['SMT 1 -1', 'SMS 1 1']),
        (2, 3, ModuleState.TESTING, ['SMT 2 -1', 'SMG 2 3', 'SMS 2 0']),
        (3, 2, ModuleState.DISARMING_IN_PROGRESS, ['SMT 3 -1', 'SMG 3 2', 'SMS 3 4']),
    )

    def test_translations(self):
        """translate_to_commands should give known result for given know module settings"""

        for module_number, module_stage, module_state, translation in self.known_values_translations:
            ktane_model = Model()
            abstract_module = AbstractModule(ktane_model)
            abstract_module.state = module_state
            abstract_module.stage = module_stage
            abstract_module.number = module_number

            result = abstract_module.translate_to_commands()
            self.assertEqual(translation, result)


if __name__ == "__main__":
    unittest.main()
