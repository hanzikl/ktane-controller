from enum import Enum

from .AbstractModule import AbstractModule, ModuleState


class WireColors(Enum):
    MISSING = 'missing'
    BLACK = 'black'
    RED = 'red'
    WHITE = 'white'
    BLUE = 'blue'
    YELLOW = 'yellow'


def get_correct_wire(sequence, boolpar):
    raise NotImplementedError


class WiresModule(AbstractModule):
    def export_to_string(self):
        raise NotImplementedError

    def import_from_string(self, string):
        raise NotImplementedError

    def translate_to_commands(self):
        raise NotImplementedError

    def __init__(self):
        super().__init__()
        self.name = "WiresModule"
        self.type_number = 10
        self.state = ModuleState.Armed
