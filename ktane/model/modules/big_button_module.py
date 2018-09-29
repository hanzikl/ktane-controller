from enum import Enum

from ktane.model.indicators import Indicators
from ktane.model.modules.abstract_module import AbstractModule, ModuleState


class ButtonColors(Enum):
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
        if self.color == ButtonColors.BLUE and self.text == ButtonText.ABORT:
            return CorrectAction.PRESS_AND_HOLD

        if self.model.batteries_count > 1 and self.text == ButtonText.DETONATE:
            return CorrectAction.PRESS_AND_RELEASE

        if self.color == ButtonColors.WHITE and self.model.contains_indicator(Indicators.CAR):
            return CorrectAction.PRESS_AND_HOLD

        if self.model.batteries_count > 2 and self.model.contains_indicator(Indicators.FRK):
            return CorrectAction.PRESS_AND_RELEASE

        if self.color == ButtonColors.YELLOW:
            return CorrectAction.PRESS_AND_HOLD

        if self.color == ButtonColors.RED and self.text == ButtonText.HOLD:
            return CorrectAction.PRESS_AND_RELEASE

        return CorrectAction.PRESS_AND_HOLD

    def translate_to_commands(self):
        commands = super().translate_to_commands()

        return commands

    def __init__(self, model):
        super().__init__(model)
        self.name = "BigButtonModule"
        self.type_number = 3
        self.state = ModuleState.ARMED
        self.color = None
        self.text = None
