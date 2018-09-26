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

    def import_from_string(self, string):
        raise NotImplementedError

    def export_to_string(self):
        raise NotImplementedError

    def translate_to_commands(self):
        raise NotImplementedError
