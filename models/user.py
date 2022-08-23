from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_subname = db.Column(db.String(80))
    password = db.Column(db.String(80))
    user_name = db.Column(db.String(80))

    chats = db.relationship('ChatModel', backref='users')
    statistics = db.relationship('StatisticModel', backref='users')

    def __init__(self, user_name,user_subname,password):
        self.user_subname = user_subname
        self.user_name = user_name
        self.password = password

    def json(self):
        return {"info":{'id':self.id,  'user_name':self.username,'user_subname':self.user_subname},"chats":[chat.json() for chat in self.chats]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, user_name):
        return cls.query.filter_by(user_name=user_name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
