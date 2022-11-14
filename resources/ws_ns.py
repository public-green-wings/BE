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

    def IMG_MESSAGE(self,data):
        """send data to other client!"""
        #img = numpy.fromstring(data,np.int8)

        print(data)

    def on_REQ_MESSAGE(self):

        a= int(input("0:local 1:global"))

        if a == 1 :
            while 1:
                try:
                    x, y, z = input("(lat,long,alt)=?: ").split()
                    emit("RES_MESSAGE", {"lat": float(x), "long": float(y), 'alt': float(z)})
                    eventlet.sleep(3)

                except Exception as e:
                    print(e)
                    continue
        else :
            while 1:
                try:
                    x, y, z = input("(x,y,z)=?: ").split()
                    emit("RES_MESSAGE", {"lat": float(x), "long": float(y), 'alt': float(z)})
                    eventlet.sleep(3)

                except Exception as e:
                    print(e)
                    continue



