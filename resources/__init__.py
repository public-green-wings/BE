from packages.pue_AI.aimodel import AIModel

main_ai = AIModel()
main_ai.model_loader()

def create_api(api):
    from .user import UserRegister, User, UserLogin
    from .chat import RangeChatList, AllChatList,YMDChatList,OneChat

    api.add_resource(RangeChatList, '/chats/sday/<string:sdate>/eday/<string:edate>')
    api.add_resource(YMDChatList, '/chats/day/<string:day>')
    api.add_resource(AllChatList, '/chats/allday')
    api.add_resource(OneChat, '/chat/<string:date>')
    api.add_resource(UserRegister, '/register')
    api.add_resource(User, '/user')
    api.add_resource(UserLogin, '/login')

def create_socketio(sock):
    from .chatnamespace import ChatNamespace
    sock.on_namespace(ChatNamespace('/realchat'))


