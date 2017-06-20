from enum import Enum


class ModuleState(Enum):
    Testing = 0
    Disarmed = 1
    Armed = 2
    FailedToDisarm = 3
    DisarmingInProgress = 4


class AbstractModule:
    def __init__(self):
        self.name = "AbstractModule"
        self.type_number = -1
        self.stage = 0
        self.state = ModuleState.Disarmed
        self.data = []

    def import_from_string(self, string):
        raise NotImplementedError

    def export_to_string(self):
        raise NotImplementedError

    def translate_to_commands(self):
        raise NotImplementedError