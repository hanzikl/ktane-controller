class MessageService:
    def __init__(self, connection):
        self.connection = connection

    def send_simple_message(self, message):
        print("Sending message: {}".format(message))
        self.connection.write(message)
        self.connection.write(b'\n')
