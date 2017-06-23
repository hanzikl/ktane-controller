class MessageService:
    def __init__(self, connection):
        self.connection = connection

    def send_simple_message(self, message):
        print("Sending message: {}".format(message))
        enc_message = bytes(source=message, encoding='utf8')
        self.connection.write(enc_message)
        self.connection.write(b'\n')
