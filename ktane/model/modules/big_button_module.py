import random
from enum import Enum

from ktane.model.indicators import Indicators
from ktane.model.modules.abstract_module import AbstractModule, ModuleState


class ButtonColor(Enum):
    BLACK = 'black'
    RED = 'red'
    WHITE = 'white'
    BLUE = 'blue'
    YELLOW = 'yellow'


class ButtonText(Enum):
    ABORT = 'abort'
    DETONATE = 'detonate'
    HOLD = 'hold'
    PRESS = 'press'


class CorrectAction(Enum):
    PRESS_AND_RELEASE = 0
    PRESS_AND_HOLD = 1


class StripColor(Enum):
    BLUE = 'blue'
    YELLOW = 'yellow'
    WHITE = 'white'
    RED = 'red'


def get_correct_digit(strip_color: StripColor):
    if strip_color is None:
        return None

    if strip_color == StripColor.BLUE:
        return 4

    if strip_color == StripColor.WHITE:
        return 1

    if strip_color == StripColor.YELLOW:
        return 5

    return 1


def translate_strip_color_to_data(color: StripColor):
    if color == StripColor.BLUE:
        return 1
    if color == StripColor.YELLOW:
        return 2
    if color == StripColor.WHITE:
        return 3
    if color == StripColor.RED:
        return 4

    # fallback
    return 0


class BigButtonModule(AbstractModule):

    def export_to_string(self):
        pass

    def import_from_string(self, string):
        pass

    def get_correct_behaviour(self):
        """
        find out correct behaviour of defuser
        :return:
        """
        if self.color == ButtonColor.BLUE and self.text == ButtonText.ABORT:
            return CorrectAction.PRESS_AND_HOLD

        if self.model.batteries_count > 1 and self.text == ButtonText.DETONATE:
            return CorrectAction.PRESS_AND_RELEASE

        if self.color == ButtonColor.WHITE and self.model.contains_indicator(Indicators.CAR):
            return CorrectAction.PRESS_AND_HOLD

        if self.model.batteries_count > 2 and self.model.contains_indicator(Indicators.FRK):
            return CorrectAction.PRESS_AND_RELEASE

        if self.color == ButtonColor.YELLOW:
            return CorrectAction.PRESS_AND_HOLD

        if self.color == ButtonColor.RED and self.text == ButtonText.HOLD:
            return CorrectAction.PRESS_AND_RELEASE

        return CorrectAction.PRESS_AND_HOLD

    def get_correct_digit(self, strip_color):

        return get_correct_digit(strip_color)

    def translate_to_commands(self):
        commands = super().translate_to_commands()

        data_values = []
        for strip_color in self.strip_colors:
            if strip_color is None:
                data_values.append(0)
                continue

            color_data = translate_strip_color_to_data(strip_color)
            correct_digit = get_correct_digit(strip_color)
            data_value = color_data * 16 + correct_digit
            data_values.append(data_value)

        data = " ".join([str(x) for x in data_values])
        commands.append("SMD {} 0 {} 0 0".format(self.number, data))

        return commands

    def get_random_strip_colors(self):

        if self.get_correct_behaviour() == CorrectAction.PRESS_AND_RELEASE:
            return [None, None, None]

        result = []
        all_strip_colors = [x for x in StripColor]
        for i in range(3):
            strip_color = random.choice(all_strip_colors)
            result.append(strip_color)

        return result

    def __init__(self, model):
        super().__init__(model)
        self.name = "BigButtonModule"
        self.type_number = 3
        self.state = ModuleState.ARMED
        self.color = None
        self.text = None
        self.strip_colors = []
