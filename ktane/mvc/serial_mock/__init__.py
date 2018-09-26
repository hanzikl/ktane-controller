from ktane.mvc.serial_mock.serial import Serial as MSerial


def Serial(file, baudrate, timeout=0):
    return MSerial(file, baudrate, timeout)
