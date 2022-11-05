import itchat
import json

import chat

chatbot=chat.Chatbot(vocab_path="chat/vocab/vocab.txt",model_path='chat/model')

@itchat.msg_register(['Text'],isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        return f"@{msg.actualNickName} {chatbot.chat(msg.text.replace('@涩涩人 ',''),msg.actualUserName)}"
    # print(msg.content)
    # print(msg.text)
    # print(msg.content==msg.text)
    # return str(dict(msg))


itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run()
