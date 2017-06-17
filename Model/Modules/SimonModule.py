from Model.Modules.AbstractModule import AbstractModule, ModuleState


class SimonModule(AbstractModule):
    def __init__(self):
        super().__init__()
        self.name = "SimonSaysModule"
        self.type_number = 2
        self.state = ModuleState.Armed
