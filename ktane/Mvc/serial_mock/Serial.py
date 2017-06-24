import time

ACK_MESSAGE = b'ack'


class Serial:
    def __init__(self, file, baud_rate, timeout=0):
        self.buffer_in = []
        self.buffer_out = []
        self.in_waiting = 0
        self.timeout = timeout

    def update_in_waiting(self):
        self.in_waiting = len(self.buffer_in)

    def write(self, message):
        # add acknowledge message to buffer_out
        self.buffer_in.append(ACK_MESSAGE)

    def readline(self):
        if self.buffer_in:
            return self.buffer_in.pop()
        else:
            time.sleep(self.timeout)
            # TODO: raise TimeoutException?
            return None
