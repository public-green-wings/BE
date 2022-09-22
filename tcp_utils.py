import socket
import threading
import json
import time

user_list = {}
notice_flag = 0

def on_auth(client,addr,data):
    type = data['type']
    if type == "USER":
        user_serc = data['user_serc']
        serc = data['serc']

    elif type == "DRONE":
        user_serc = data['user_serc']
        serc = data['serc']

    else:
        res={
            "event": "auth_ret",
            "type": type,
            "code": 401,
            "message": "Invalid user type!"
        }
        client.send(json.dumps(res))
        client.close()
        return False

    user_list[serc][type] = client
    res = {
        "event": "auth_ret",
        "type": type,
        "code": 200,
        "message": "Auth success!"
    }
    return True

def on_send_msg(client,addr,data):
    type = data['type']
    if type == "USER":
        user_serc = data['user_serc']
        serc = data['serc']
        gps = data['gps']

    elif type == "DRONE":
        user_serc = data['user_serc']
        serc = data['serc']
        gps = data['gps']
        image = data['image']

    else:
        res={
            "event": "auth_ret",
            "type": type,
            "code": 401,
            "message": "Invalid user type!"
        }
        client.send(json.dumps(res))
        client.close()
        return False

    serc = data['serc']
    user_list[serc][type] = client
    return True


def handler(client, addr):
    while 1:
        raw_data = client.recv(1024)
        raw_data = raw_data.decode()
        data = json.loads(raw_data)

        if data["event"] == "auth":
            if not on_auth(client,addr,data):
                print("Auth failed... connection closed!")
                return
            else :
                print("Auth success!")

        if data["event"] == "send_msg":
            on_send_msg(client,addr,data)




        if string == "/종료" : break
        string = "%s : %s"%(user, string)
        print(string)
        for con in user_list.values():
            try:
                con.sendall(string.encode())
            except:
                print("연결이 비 정상적으로 종료된 소켓 발견")


    del user_list[user]
    client_socket.close()

def handle_notice(client_socket, addr, user):
    pass

def tcpRun(host,port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    #서버가 최대 5개의 클라이언트의 접속을 허용한다.
    server_socket.listen()

    while 1:

        client_socket, addr = server_socket.accept()

        for user, con in user_list:
            con.close()


        #accept()함수로 입력만 받아주고 이후 알고리즘은 핸들러에게 맡긴다.
        notice_thread = threading.Thread(target=handle_notice, args=(client_socket, addr))
        notice_thread.daemon = True
        notice_thread.start()

        receive_thread = threading.Thread(target=handle_receive, args=(client_socket, addr))
        receive_thread.daemon = True
        receive_thread.start()


if __name__ == '__main__':

    host = "127.0.0.1"
    port = 3001
    tcpRun(host,port)
