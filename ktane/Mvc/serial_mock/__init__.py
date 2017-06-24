from ktane.Mvc.serial_mock.Serial import Serial as MSerial


def Serial(file, baud, timeout = 0):
    return MSerial(file, baud, timeout)
