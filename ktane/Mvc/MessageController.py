import serial
from time import sleep

DELAY_BETWEEN_MESSAGES = 0.05


class MessageController:
    def __init__(self, connection):
        """

        :param connection: serial.Serial
        """
        assert isinstance(connection, serial.Serial)
        self.connection = connection

    def process_message(self, msg):
        print("Processing message: {}".format(msg))

    def recieve_messages(self):
        while self.connection.in_waiting > 0:
            msg = self.connection.readline()
            self.process_message(msg)
            sleep(DELAY_BETWEEN_MESSAGES)
