from enum import Enum
from ..model import Model


class ModuleState(Enum):
    TESTING = 0
    DISARMED = 1
    ARMED = 2
    FAILED_TO_DISARM = 3
    DISARMING_IN_PROGRESS = 4


class AbstractModule:
    def __init__(self, model: Model):
        self.name = "AbstractModule"
        self.type_number = -1
        self.stage = 0
        self.state = ModuleState.DISARMED
        self.data = []
        self.model = model
        self.number = 0

    def import_from_string(self, string):
        raise NotImplementedError

    def export_to_string(self):
        raise NotImplementedError

    def translate_to_commands(self):
        # set module type command:
        commands = ["SMT {} {}".format(self.number, self.type_number)]

        # set module stage command:
        if self.stage != 0:
            commands.append("SMG {} {}".format(self.number, self.stage))

        # set module state command
        commands.append("SMS {} {}".format(self.number, self.state.value))

        return commands
