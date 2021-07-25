from datetime import datetime

class ChatMessage:
    def __init__(self, author, msg, debug=True) -> None:
        self.author = author
        self.message = msg
        self.date = datetime.now()

        if debug:
            self.debug()

    def debug(self):
        str_date = "[{}:{}:{}]".format(self.date.hour, self.date.minute, self.date.second)
        str_msg = "{}: {}".format(self.author, self.message)
        print(str_date, str_msg)