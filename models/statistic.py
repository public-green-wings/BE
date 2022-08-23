from db import db
from . import and_
import json

init_emotion={
    "불만":0, "중립":0, "당혹":0, "기쁨":0, "걱정":0, "질투":0, "슬픔":0, "죄책감":0, "연민":0
}

class StatisticModel(db.Model):
    __tablename__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    mtype = db.Column(db.String(80)) #0-day, 1-week 2-month, 3-year
    start_date = db.Column(db.String(80))
    end_date = db.Column(db.String(80))#day - YYYY-MM-DD ,week - YYYY-MM-DD(start), month - YYYY-MM , year - YYYY
    emotions = db.Column(db.String(80))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, mtype,start_date,end_date,user_id):
        self.mtype = mtype
        self.start_date = start_date
        self.end_date = end_date
        self.emotions = json.dumps(init_emotion)

        self.user_id = user_id

    def json(self):
        return {'info':{'type': self.type, 'start_date': self.start_date,'end_date':self.end_date},
                'emotions': json.loads(self.emotions)}

    #1. day인 경우, month를 받으면 해당월에 관련된 모든 day 통계 표출
    #2. day인 경우, start와 end를 받으면 해당 기간에 관련된 모든 day 통계 표출
    #3. week인 경우, month를 받으면 해당 월과 관련된 모든 week 통계 표출
    #4. week인 경우, start를 받으면 해당 기간에 관련된 week 표출
    #5. month인 경우, month를 받으면 해당 월과 관련된 month 통계 표출


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    ##week, day는 시작 날짜, 양식은 YYYYMMDD
    ##month면 start_date 양식은 YYYYMM
    @classmethod
    def find_by_user_id_and_type_and_sdate(cls, user_id,mtype,start_date):
        return cls.query.filter(and_(cls.mtype == mtype, cls.user_id == user_id, cls.start_date == start_date)).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
