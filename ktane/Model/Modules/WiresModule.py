from enum import Enum

from .AbstractModule import AbstractModule, ModuleState


class WireColors(Enum):
    MISSING = 'missing'
    BLACK = 'black'
    RED = 'red'
    WHITE = 'white'
    BLUE = 'blue'
    YELLOW = 'yellow'


def get_correct_wire(sequence: list, boolpar):
    wires_count = get_wires_count(sequence)
    if wires_count == 3:
        if count_wires_of_given_color(sequence, WireColors.RED.value) == 0:
            # no red wires
            return get_nth_wire_position(sequence, 2)

        sequence_reversed = sequence[::-1]
        if sequence_reversed[get_nth_wire_position(sequence_reversed, 1)] \
                == WireColors.WHITE.value:
            # last wire is white
            return len(sequence_reversed) - 1 - get_nth_wire_position(sequence_reversed, 1)

        blue_filtered_reversed = filter_color_in_sequence(
            sequence_reversed, WireColors.BLUE.value)
        if get_wires_count(blue_filtered_reversed) > 1:
            # more than one blue wire - cut the last blue
            return len(sequence_reversed) - 1 - get_nth_wire_position(blue_filtered_reversed, 1)

        # otherwise cut last wire
        return len(sequence_reversed) - 1 - get_nth_wire_position(sequence_reversed, 1)

    return None


def get_wires_count(sequence):
    return len([1 for x in sequence if x != WireColors.MISSING.value])


def get_nth_wire_position(sequence, n):
    counter = 0
    for idx, value in enumerate(sequence):
        if value != WireColors.MISSING.value:
            counter += 1
        if counter == n:
            return idx

    return None


def filter_color_in_sequence(sequence, color):
    """
    Any other colors in sequence are replaced by WireColors.MISSING
    :param sequence: list of WireColors
    :param color: str
    :return: sequence with filtered colors
    """
    return [x if x == color else WireColors.MISSING.value for x in sequence]


def count_wires_of_given_color(sequence, color):
    return len([1 for x in sequence if x == color])


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
