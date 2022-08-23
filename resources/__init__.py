from packages.k_doll_ai_chatbot.transformer_models.aimodel import AIModel

main_ai = AIModel()
main_ai.model_loader()

def create_api(api):
    from .user import UserRegister, User, UserLogin
    from .chat import FullDateChat, AllChatList,YMDChatList


    api.add_resource(FullDateChat,'/chat/detail-date/<string:date>')
    api.add_resource(YMDChatList, '/chats/oneday-date/<string:date>')
    api.add_resource(AllChatList, '/chats/allday-date/<string:date>')
    api.add_resource(UserRegister, '/register')
    api.add_resource(User, '/user/<string:username>')
    api.add_resource(UserLogin, '/login')

def create_socketio(sock):
    from .chatnamespace import ChatNamespace
    sock.on_namespace(ChatNamespace('/realchat'))


