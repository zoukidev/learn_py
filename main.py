from Chat import chat, author

def start():
    author_1 = author.Author("ZoukiDev")

    chat_1 = chat.Chat("Chat 1")
    chat_1.sendMessage(author_1, "Hello world")

    print("Start app")

if __name__ == "__main__":
    start()