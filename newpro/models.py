from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  

db = SQLAlchemy()

class User(db.Model):
    User_id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100))
    Password = db.Column(db.String(100))
    followed_truyens = db.relationship('Truyen', secondary='followed_truyens', backref=db.backref('followers', lazy=True))

    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password

class Truyen(db.Model):
    Truyen_id = db.Column(db.Integer, primary_key=True)
    Truyen_ma = db.Column(db.String(50))
    Truyen_ten = db.Column(db.String(1000))
    Truyen_theloai = db.Column(db.String(50))
    Truyen_tacgia = db.Column(db.String(50))
    Truyen_hinhdaidien = db.Column(db.String(100))
    followed_truyens = db.relationship('FollowedTruyen', backref='Truyen', lazy=True)
    chuoongs = db.relationship('Chuong', backref='truyen', lazy=True)  # Add this line

    def __init__(self,Truyen_id,Truyen_ma,Truyen_ten,Truyen_theloai,Truyen_tacgia,Truyen_hinhdaidien):
        self.Truyen_ma=Truyen_ma
        self.Truyen_tacgia=Truyen_tacgia
        self.Truyen_ten=Truyen_ten
        self.Truyen_theloai=Truyen_theloai
        self.Truyen_hinhdaidien=Truyen_hinhdaidien

class Chuong(db.Model):
    Chuong_id=db.Column(db.Integer,primary_key=True)
    Chuong_so=db.Column(db.Integer)
    Chuong_ten= db.Column(db.String(1000))
    Chuong_noidung=db.column(db.Text)
    truyen_id = db.Column(db.Integer, db.ForeignKey('truyen.Truyen_id'), nullable=False)

    def __init__(self, truyen_id, Chuong_so,Chuong_ten,Chuong_noidung):
        self.Chuong_so=Chuong_so
        self.Chuong_noidung=Chuong_noidung
        self.Chuong_ten=Chuong_ten
        self.truyen_id = truyen_id

class FollowedTruyen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.User_id'), nullable=False)
    truyen_id = db.Column(db.Integer, db.ForeignKey('truyen.Truyen_id'), nullable=False)
    followed_at = db.Column(db.DateTime, default=datetime.utcnow)







    