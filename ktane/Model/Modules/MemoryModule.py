from ktane.Model.Modules.AbstractModule import AbstractModule, ModuleState


class MemoryModule(AbstractModule):
    def export_to_string(self):
        pass

    def import_from_string(self, string):
        pass

    def translate_to_commands(self):
        pass

    def __init__(self):
        super().__init__()
        self.name = "MemoryModule"
        self.type_number = 6
        self.state = ModuleState.Armed
