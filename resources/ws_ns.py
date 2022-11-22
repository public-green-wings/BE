from flask_socketio import Namespace, emit, join_room, leave_room, close_room
from flask import session, request
from models.user import UserModel
from datetime import datetime
from pytz import timezone
import eventlet

rooms={
    "DRONE":"",
    "USER":""
}
class ChatNamespace(Namespace):

    def on_connect(self):
        print("Client connected",)
        #sessioned= session.get()

    def on_disconnect(self):
        leave_room(request.sid)
        close_room(request.sid)

        if rooms["USER"] == request.sid:
            rooms["USER"] = ""
        elif rooms["DRONE"] == request.sid:
            rooms["DRONE"] = ""

        print("Client disconnected", )
        #sessioned = session.get()

    def on_JOIN(self,data):
        join_room(request.sid)
        if data["type"] == "DRONE":
            rooms["DRONE"] = request.sid
        elif data["type"] == "USER":
            rooms["USER"] = request.sid

    def on_CUR_POS(self,data):
        emit("REV_POS",data,to=rooms["USER"])

    def on_PUB_POS(self,data):

        emit("REQ_POS", {"lat": float(data["x"]), "long": float(data["y"]), 'alt': float(data["z"])},to=rooms["DRONE"])
        eventlet.sleep(3)




