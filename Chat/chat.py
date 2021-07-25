from Chat.chatmessage import ChatMessage

class Chat:
    def __init__(self, name) -> None:
        self.name = name
        self.messages = []

    def sendMessage(self, author, msg):
        self.messages.append(ChatMessage(author, msg))