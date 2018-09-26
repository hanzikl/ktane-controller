from ktane.model.modules.abstract_module import AbstractModule, ModuleState


class SimonModule(AbstractModule):
    def export_to_string(self):
        pass

    def import_from_string(self, string):
        pass

    def translate_to_commands(self):
        pass

    def __init__(self):
        super().__init__()
        self.name = "SimonSaysModule"
        self.type_number = 2
        self.state = ModuleState.ARMED
