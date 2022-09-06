
def create_api(api):
    from .user import UserRegister, User, UserLogin

    api.add_resource(UserRegister, '/register')
    api.add_resource(User, '/user')
    api.add_resource(UserLogin, '/login')

def create_socketio(sock):
    from .chatnamespace import ChatNamespace
    sock.on_namespace(ChatNamespace('/realchat'))


