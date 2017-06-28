from ktane.Mvc.serial_mock.Serial import Serial as MSerial


def Serial(file, baudrate, timeout=0):
    return MSerial(file, baudrate, timeout)
