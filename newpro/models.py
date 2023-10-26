from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  
from sqlalchemy import asc

from flask_login import UserMixin

db = SQLAlchemy()



class User(UserMixin, db.Model):
    User_id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100))
    Password = db.Column(db.String(100))
    reading_history = db.relationship('ReadingHistory', backref='user', lazy='dynamic')
    followed_truyens = db.relationship('FollowedTruyen', backref='user', lazy='dynamic')

    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password

    def get_id(self):
        return str(self.User_id)


class Truyen(db.Model):
    Truyen_id = db.Column(db.Integer, primary_key=True)
    # Truyen_ma = db.Column(db.String(50))
    Truyen_ten = db.Column(db.String(1000))
    # Truyen_theloai = db.Column(db.String(50))
    # Truyen_tacgia = db.Column(db.String(50))
    # Truyen_hinhdaidien = db.Column(db.String(100))
    # followed_truyens = db.relationship('FollowedTruyen', backref='Truyen', lazy=True)
    chuoongs = db.relationship('Chuong', backref='truyen', lazy=True)  # Add this line
    reading_history = db.relationship('ReadingHistory', backref='truyen', lazy=True)
    followed_users = db.relationship('FollowedTruyen', backref='truyen', lazy=True)

    def __init__(self,Truyen_ten):
        # self.Truyen_ma=Truyen_ma
        # self.Truyen_tacgia=Truyen_tacgia
        self.Truyen_ten=Truyen_ten
        # self.Truyen_theloai=Truyen_theloai
        # self.Truyen_hinhdaidien=Truyen_hinhdaidien

class Chuong(db.Model):
    Chuong_id=db.Column(db.Integer,primary_key=True)
    Chuong_so=db.Column(db.Integer)
    Chuong_ten= db.Column(db.String(1000))
    _Chuong_noidung = db.Column(db.Text)
    Chuong_noidung = db.column_property(_Chuong_noidung)
    Chuong_tieude = db.Column(db.String(100))
    truyen_id = db.Column(db.Integer, db.ForeignKey('truyen.Truyen_id'), nullable=False)
    reading_history = db.relationship('ReadingHistory', backref='chuong', lazy=True)

    def __init__(self, truyen_id, Chuong_so,Chuong_ten,Chuong_noidung,Chuong_tieude):
        self.Chuong_so=Chuong_so
        self.Chuong_noidung=Chuong_noidung
        self.Chuong_ten=Chuong_ten
        self.truyen_id = truyen_id
        self.Chuong_tieude=Chuong_tieude



class ReadingHistory(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.User_id'), nullable=False)
    truyen_id = db.Column(db.Integer, db.ForeignKey('truyen.Truyen_id'), nullable=False)
    chuong_id = db.Column(db.Integer, db.ForeignKey('chuong.Chuong_id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<ReadingHistory {self.user_id}, {self.truyen_id}, {self.chuong_id}>"

    
class FollowedTruyen(db.Model):
    fl_id=db.Column(db.Integer, primary_key=True)

    user_fl_id=db.Column(db.Integer, db.ForeignKey('user.User_id'), nullable=False)
    truyen_fl_id = db.Column(db.Integer, db.ForeignKey('truyen.Truyen_id'), nullable=False)

    