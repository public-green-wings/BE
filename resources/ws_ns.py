from flask_socketio import Namespace, emit
from flask import session, request
from models.user import UserModel
from datetime import datetime
from pytz import timezone
import eventlet

class ChatNamespace(Namespace):

    def on_connect(self):
        print("Client connected",)

        #sessioned= session.get()

    def on_disconnect(self):
        print("Client disconnected", )
        #sessioned = session.get()

    def on_REQ_MESSAGE(self):

        x,y,z = input("(lat,long,alt)=?: ").split()
        emit("RES_MESSAGE", {"lat": float(x), "long": float(y), 'alt': float(z)})
