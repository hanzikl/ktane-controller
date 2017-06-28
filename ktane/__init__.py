import ktane.conf as config
import time

from .Services.delayingMessageService import DelayingMessageService
from .Mvc.MessageController import MessageController
from .Services.MessageService import MessageService

if config.serial_mock:
    from ktane.Mvc import serial_mock as serial
else:
    import serial

connection = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=config.serial_timeout)

messageService = DelayingMessageService(connection)
messageService.prolong_delay(4)
messageController = MessageController(connection)

outputBuffer = ['SMT 2 7', 'SMS 2 2', 'SMT 1 2', 'SMS 1 2', 'SMT 0 1', 'SMS 0 1', 'I', 'SR 0 1 212 192', 'GMS', 'GMT',
                'ST1']

time.sleep(2)

while True:
    messageController.recieve_messages()
    messageService.tick()
    if outputBuffer:
        messageService.add_delaying_message(outputBuffer.pop(0), 1 / float(config.serial_message_rate))
