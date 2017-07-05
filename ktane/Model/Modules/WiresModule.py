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
    wires_count = get_wires_count(sequence)


def get_wires_count(sequence):
    return len([1 for x in sequence if x != WireColors.MISSING.value])


def get_nth_wire_position(sequence, n):
    NotImplementedError


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
