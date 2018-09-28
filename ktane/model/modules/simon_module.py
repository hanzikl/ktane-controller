from ktane.model.modules.abstract_module import AbstractModule, ModuleState

rules_permutations_dict = {True: [[3, 2, 1, 0], [2, 3, 0, 1], [3, 0, 1, 2]],
                           False: [[1, 3, 2, 0], [0, 2, 1, 3], [2, 3, 0, 1]]}


class SimonModule(AbstractModule):

    def export_to_string(self):
        pass

    def import_from_string(self, string):
        pass

    def translate_to_commands(self):
        commands = super().translate_to_commands()

        my_permutations = rules_permutations_dict.get(self.model.serial_number_contains_vowel)

        for idx, permutation in enumerate(my_permutations):
            permutation_str = [str(x) for x in permutation]
            data = " ".join(permutation_str)
            commands.append("SMD {} {} {} 0".format(self.number, idx, data))

        return commands

    def __init__(self, model):
        super().__init__(model)
        self.name = "SimonSaysModule"
        self.type_number = 2
        self.state = ModuleState.ARMED
