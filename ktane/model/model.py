class Model:

    def contains_indicator(self, indicator):
        return indicator in self.indicators

    def __init__(self):
        self.remainingTime = 0  # in seconds
        self.strikes = 0
        self.maxStrikes = 2
        self.serial_number_contains_vowel = False
        self.indicators = []
        self.batteries_count = 0
