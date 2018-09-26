import serial
from .serial_mock.serial import Serial as SerialMock
from time import sleep

DELAY_BETWEEN_MESSAGES = 0.05


class MessageController:
    def __init__(self, connection):
        """

        :param connection: serial.Serial
        """
        assert isinstance(connection, serial.Serial) or isinstance(connection, SerialMock)
        self.connection = connection

    def process_message(self, msg):
        print("Processing message: {}".format(msg))

    def receive_messages(self):

        # mock update
        if isinstance(self.connection, SerialMock):
            self.connection.update_mock()

        while self.connection.in_waiting > 0:
            msg = self.connection.readline()
            self.process_message(msg)
            sleep(DELAY_BETWEEN_MESSAGES)
