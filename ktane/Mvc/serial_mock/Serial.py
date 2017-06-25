import time
import random
from ktane.conf.settings import DEBUG_CHAR

ACK_MESSAGE = b'ack'
RANDOM_DEBUG_MESSAGE_PROBABILITY = 0.00003


class Serial:
    def __init__(self, file, baud_rate, timeout=0):
        self.buffer_in = []
        self.buffer_out = []
        self.in_waiting = 0
        self.timeout = timeout

    def update_in_waiting(self):
        self.in_waiting = len(self.buffer_in)

    def write(self, message):
        # add acknowledge message to buffer_in
        self.buffer_in.append(ACK_MESSAGE)

    def add_random_debug_message(self):
        self.buffer_in.append(bytes("{}debug message #{}".format(DEBUG_CHAR, random.randint(1, 1000)), 'utf8'))
        self.update_in_waiting()

    def readline(self):
        if self.buffer_in:
            msg = self.buffer_in.pop()
            self.update_in_waiting()
            return msg
        else:
            time.sleep(self.timeout)
            # TODO: raise TimeoutException?
            return None

    def update_mock(self):
        if random.random() < RANDOM_DEBUG_MESSAGE_PROBABILITY:
            self.add_random_debug_message()
