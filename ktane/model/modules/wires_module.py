from enum import Enum

from .abstract_module import AbstractModule, ModuleState


class WireColors(Enum):
    MISSING = ''
    BLACK = 'black'
    RED = 'red'
    WHITE = 'white'
    BLUE = 'blue'
    YELLOW = 'yellow'


def get_correct_wire(sequence: list, boolpar):
    wires_count = get_wires_count(sequence)
    sequence_reversed = sequence[::-1]
    if wires_count == 3:
        if count_wires_of_given_color(sequence, WireColors.RED.value) == 0:
            # no red wires
            return get_nth_wire_position(sequence, 2)

        if sequence_reversed[get_nth_wire_position(sequence_reversed, 1)] \
                == WireColors.WHITE.value:
            # last wire is white - cut the last wire
            return get_nth_reversed_wire_position(sequence_reversed)

        blue_filtered_reversed = filter_color_in_sequence(
            sequence_reversed, WireColors.BLUE.value)
        if get_wires_count(blue_filtered_reversed) > 1:
            # more than one blue wire - cut the last blue
            return get_nth_reversed_wire_position(blue_filtered_reversed)

        # otherwise cut last wire
        return get_nth_reversed_wire_position(sequence_reversed)

    if wires_count == 4:
        red_filtered_reversed = filter_color_in_sequence(
            sequence_reversed, WireColors.RED.value)
        if get_wires_count(red_filtered_reversed) > 1 and boolpar:
            # more than one red and special condition - cut last red
            return get_nth_reversed_wire_position(red_filtered_reversed)

        if get_wires_count(red_filtered_reversed) == 0 \
                and sequence_reversed[get_nth_wire_position(sequence_reversed, 1)] \
                == \
                WireColors.YELLOW.value:
            # no red wires, last wire is yellow - cut first
            return get_nth_wire_position(sequence)

        if count_wires_of_given_color(sequence, WireColors.BLUE.value) == 1:
            # one blue wire - cut first
            return get_nth_wire_position(sequence)

        if count_wires_of_given_color(sequence, WireColors.YELLOW.value) > 1:
            # more than one yellow - cut last
            return get_nth_reversed_wire_position(sequence_reversed)

        return get_nth_wire_position(sequence, 2)

    if wires_count == 5:
        if boolpar and sequence_reversed[get_nth_wire_position(sequence_reversed, 1)] \
                == \
                WireColors.BLACK.value:
            # last is black and special condition - cut fourth
            return get_nth_wire_position(sequence, 4)

        if count_wires_of_given_color(sequence, WireColors.RED.value) == 1 and \
                count_wires_of_given_color(sequence, WireColors.YELLOW.value) > 1:
            # one red and more than 1 yellow - cut first
            return get_nth_wire_position(sequence)

        if count_wires_of_given_color(sequence, WireColors.BLACK.value) == 0:
            # no black wires - cut second
            return get_nth_wire_position(sequence, 2)

        # cut first
        return get_nth_wire_position(sequence)

    if wires_count == 6:
        if boolpar and count_wires_of_given_color(sequence, WireColors.YELLOW.value) == 0:
            # no yellow and special condition
            return get_nth_wire_position(sequence, 3)

        if count_wires_of_given_color(sequence, WireColors.YELLOW.value) == 1 and \
                count_wires_of_given_color(sequence, WireColors.WHITE.value) > 1:
            # one yellow and more than one white - cut fourth
            return get_nth_wire_position(sequence, 4)

        if count_wires_of_given_color(sequence, WireColors.RED.value) == 0:
            # no red - cut last
            return get_nth_reversed_wire_position(sequence_reversed)

        return get_nth_wire_position(sequence_reversed, 4)

    return None


def get_wires_count(sequence):
    return len([1 for x in sequence if x != WireColors.MISSING.value])


def get_nth_wire_position(sequence, n=1):
    counter = 0
    for idx, value in enumerate(sequence):
        if value != WireColors.MISSING.value:
            counter += 1
        if counter == n:
            return idx

    return None


def get_nth_reversed_wire_position(sequence_reversed, n=1):
    return len(sequence_reversed) - 1 - get_nth_wire_position(sequence_reversed, n)


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
        commands = super().translate_to_commands()

        mask = 0
        counter = 2
        for wire in self.wires_sequence:
            counter *= 2
            if wire != WireColors.MISSING.value:
                mask += counter

        correct_wire = self.get_correct_wire()
        target_mask = 2**(2 + correct_wire)

        commands.append("SMD {} 0 {} {} 0 0 0".format(self.number, mask, target_mask))

        return commands

    def __init__(self, model):
        super().__init__(model)
        self.name = "WiresModule"
        self.type_number = 4
        self.state = ModuleState.ARMED
        self.wires_sequence = None

    def get_correct_wire(self):
        return get_correct_wire(self.wires_sequence, self.model.serial_number_contains_vowel)

    def get_wires_count(self):
        return get_wires_count(self.wires_sequence)

    def get_nth_wire_position(self, n):
        return get_nth_wire_position(self.wires_sequence, n)
