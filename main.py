from Chat import chat

def start():
    chat_1 = chat.Chat("Chat 1")
    chat_1.sendMessage("ZoukiDev", "Hello world")

    print("Start app")

if __name__ == "__main__":
    start()