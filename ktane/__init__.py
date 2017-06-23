import time

import serial

from .Mvc.MessageController import MessageController
from .Services.MessageService import MessageService

connection = serial.Serial('/dev/ttyUSB0', 9600)

messageService = MessageService(connection)
messageController = MessageController(connection)

outputBuffer = ['ST1', 'SR 0 1 212 192']

time.sleep(2)

while True:
    messageController.recieve_messages()
    if outputBuffer:
        messageService.send_simple_message(outputBuffer.pop())
