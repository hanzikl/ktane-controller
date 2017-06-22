import time

import serial

from .Services.MessageService import MessageService

connection = serial.Serial('/dev/ttyUSB0', 9600)

messageService = MessageService(connection)

outputBuffer = [b'ST1']
inputBuffer = []

time.sleep(2)

while connection.in_waiting > 0:
    in_waiting = connection.in_waiting
    bufferline = connection.readline()
    inputBuffer.append(bufferline)
    print('{}: {}'.format(in_waiting, bufferline))
    time.sleep(0.05)

for msg in outputBuffer:
    messageService.send_simple_message(msg)

for msg in inputBuffer:
    print(msg)
