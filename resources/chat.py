from flask_restful import Resource, reqparse
from models.chat import ChatModel
from flask_jwt_extended import jwt_required, get_jwt_identity

class FullDateChat(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('date_YMD',
                        type=str,
                        required=True,
                        help="Field named 'date_YMD' cannot be blank."
                        )
    parser.add_argument('date_YMDHMS',
                        type=str,
                        required=True,
                        help="Field named 'date_YMDHMS' cannot be blank."
                        )
    parser.add_argument('direction',
                        type=str,
                        required=True,
                        help="Field named 'direction' cannot be blank."
                        )
    parser.add_argument('utterance',
                        type=str,
                        required=True,
                        help="Field named 'utterance' cannot be blank."
                        )
    @jwt_required
    def get(self, date):
        user_id = get_jwt_identity()
        chat = ChatModel.find_by_fulldate_with_user_id(user_id,date)
        if chat:
            return chat.json(), 200
        return {'message': 'There is no chattings...'}, 404

    @jwt_required
    def post(self,date):
        user_id = get_jwt_identity()
        data = ChatModel.parser.parse_args()

        if ChatModel.find_by_fulldate_with_user_id(user_id,date):
            return {'message': "A chat with date '{}' already exists.".format(date)}, 400

        chat = ChatModel(user_id, **data)

        try:
            chat.save_to_db()
        except Exception as e:
            return {"message": "An error occurred creating the chat."}, 500

        return chat.json(), 201

    @jwt_required
    def delete(self, date):
        user_id = get_jwt_identity()
        chat = ChatModel.find_by_fulldate_with_user_id(user_id,date)
        if chat:
            chat.delete_from_db()

        return {'message': 'Chat deleted'}, 200

class AllChatList(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        chats = [chat.json() for chat in ChatModel.find_all_by_user_id(user_id)]
        return {'chats': chats}

class YMDChatList(Resource):
    @jwt_required
    def get(self,date):
        user_id = get_jwt_identity()
        chats = [chat.json() for chat in ChatModel.find_all_by_dateYMD_with_user_id(user_id,date)]
        return {'chats': chats}