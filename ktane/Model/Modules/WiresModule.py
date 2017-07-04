from enum import Enum

from .AbstractModule import AbstractModule, ModuleState


class WireColors(Enum):
    MISSING = 0
    BLACK = 1
    RED = 2
    WHITE = 3
    BLUE = 4
    YELLOW = 5


def get_correct_wire(sequence):
    raise NotImplementedError

class WiresModule(AbstractModule):
    def export_to_string(self):
        pass

    def import_from_string(self, string):
        pass

    def translate_to_commands(self):
        pass

    def __init__(self):
        super().__init__()
        self.name = "WiresModule"
        self.type_number = 10
        self.state = ModuleState.Armed
