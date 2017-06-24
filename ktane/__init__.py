import ktane.conf as config
import time

if config.serial_mock:
    from ktane.Mvc import serial_mock as serial
else:
    import serial

from .Mvc.MessageController import MessageController
from .Services.MessageService import MessageService

connection = serial.Serial('/dev/ttyUSB0', 9600, config.serial_timeout)

messageService = MessageService(connection)
messageController = MessageController(connection)

outputBuffer = ['ST1', 'SR 0 1 212 192']

time.sleep(2)

while True:
    messageController.recieve_messages()
    if outputBuffer:
        messageService.send_simple_message(outputBuffer.pop())
