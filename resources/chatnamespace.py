from flask_socketio import Namespace, emit
from flask import session, request
from resources import main_ai
from models.user import UserModel
from models.chat import ChatModel
from datetime import datetime

class ChatNamespace(Namespace):

    def on_connect(self):
        print("Client connected",)
        #sessioned= session.get()

    def on_disconnect(self):
        print("Client disconnected", )
        #sessioned = session.get()

    def on_SEND_MESSAGE(self,data):
        print(data)
        now = datetime.now()
        YMD = str(now.year) + str(now.month) + str(now.day)
        YMDHMS = YMD + str(now.hour) + str(now.minute) + str(now.second)

        processed_data = main_ai.run("Hello", data['message'])
        print(processed_data["System_Corpus"])

        now = datetime.now()
        YMD = str(now.year) + str(now.month) + str(now.day)
        YMDHMS = YMD + str(now.hour) + str(now.minute) + str(now.second)

        emit("RECEIVE_MESSAGE", {"response": processed_data["System_Corpus"],"day":YMD,'time':YMDHMS})
