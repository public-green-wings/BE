from flask_socketio import Namespace, emit
from flask import session, request
from resources import main_ai
from models.user import UserModel
from models.chat import ChatModel
from datetime import datetime
from pytz import timezone

format_data = "%d/%m/%y %H:%M:%S.%f"

class ChatNamespace(Namespace):

    def on_connect(self):
        print("Client connected",)
        #sessioned= session.get()

    def on_disconnect(self):
        print("Client disconnected", )
        #sessioned = session.get()

    def on_SEND_MESSAGE(self,data):
        print(data)
        now = datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H%M%S")
        print("DAY: ",now[:8])
        print("TIME: ",now[8:])
        processed_data = main_ai.run("Hello", data['message'])

        now = datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H%M%S")

        emit("RECEIVE_MESSAGE", {"response": processed_data["System_Corpus"],"day":now[:8],'time':now[8:]})
