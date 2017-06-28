import ktane.conf as config
import time

from .Services.delayingMessageService import DelayingMessageService
from .Mvc.MessageController import MessageController
from .Services.MessageService import MessageService

if config.serial_mock:
    from ktane.Mvc import serial_mock as serial
else:
    import serial

connection = serial.Serial('/dev/ttyUSB0', 9600, config.serial_timeout)

messageService = DelayingMessageService(connection)
messageService.prolong_delay(4)
messageController = MessageController(connection)

outputBuffer = ['ST1', 'SR 0 1 212 192']

time.sleep(2)

while True:
    messageController.recieve_messages()
    messageService.tick()
    if outputBuffer:
        messageService.add_delaying_message(outputBuffer.pop(), 5)
