import time

from ktane.Services.MessageService import MessageService


class DelayingMessage:
    def __init__(self, message, delay):
        self.message = message
        self.delay = delay


class DelayingMessageService(MessageService):
    def __init__(self, connection):
        super().__init__(connection)
        self.messageQueue = []
        self.nextMessageTime = time.time()

    def prolong_delay(self, delay):
        self.nextMessageTime += delay

    def add_delaying_message(self, message, delay):
        self.messageQueue.append(DelayingMessage(message, delay))

    def tick(self):
        now = time.time()
        if self.messageQueue and now >= self.nextMessageTime:
            delayed_message = self.messageQueue.pop(0)
            self.send_simple_message(delayed_message.message)
            self.nextMessageTime = now + delayed_message.delay
