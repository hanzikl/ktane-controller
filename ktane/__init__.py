import ktane.conf as config
import time

from .services.delaying_message_service import DelayingMessageService
from .mvc.message_controller import MessageController
from .services.message_service import MessageService

if config.serial_mock:
    from ktane.mvc import serial_mock as serial
else:
    import serial


def dumb_run():

    connection = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=config.serial_timeout)

    message_service = DelayingMessageService(connection)
    message_service.prolong_delay(4)
    message_controller = MessageController(connection)


    output_buffer = ['SMT 2 7', 'SMS 2 2', 'SMT 1 2', 'SMS 1 2', 'SMT 0 1', 'SMS 0 1', 'I', 'SR 0 1 212 192', 'GMS', 'GMT',
                    'ST1']

    time.sleep(2)

    while True:
        message_controller.receive_messages()
        message_service.tick()
        if output_buffer:
            message_service.add_delaying_message(output_buffer.pop(0), 1 / float(config.serial_message_rate))


if __name__ == "__main__":
    dumb_run()

