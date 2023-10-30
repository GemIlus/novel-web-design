from flask import Flask, render_template, request, redirect, url_for ,session ,flash,get_flashed_messages,Blueprint
from os import path
import os
from flask_sqlalchemy import SQLAlchemy 
from .models import db, Truyen, Chuong, ReadingHistory, User,FollowedTruyen
from sqlalchemy import asc
from flask_login import current_user,login_required
from datetime import datetime  

main_bp = Blueprint('main', __name__)


def get_current_user():
    user_id = session.get('user_id')

    if user_id:
        return User.query.get(user_id)

    return None
def get_chapter_info(truyen_id, chuong_so):
    chuong = Chuong.query.filter_by(truyen_id=truyen_id, Chuong_so=chuong_so).first()

    if chuong:
        chuong_content = chuong.Chuong_noidung
        prev_chuong = Chuong.query.filter_by(truyen_id=truyen_id, Chuong_so=chuong_so - 1).first()
        next_chuong = Chuong.query.filter_by(truyen_id=truyen_id, Chuong_so=chuong_so + 1).first()
        truyen = Truyen.query.filter_by(Truyen_id=truyen_id).first()

        return truyen, chuong_content, prev_chuong, next_chuong
    else:
        return None, "Chapter not found", None, None

@main_bp.route('/')
def index():
    user= session.get('user')
    
    return render_template('index.html',user=user)
@main_bp.route('/catalog')
def catalog():
    # Add any logic if needed
    return render_template('catalog.html')

@main_bp.route('/tienhiep')
def tienhiep():
    # Add any logic if needed
    return render_template('tienhiep.html')

@main_bp.route('/read_story/<int:truyen_id>/<int:chuong_id>', methods=['GET', 'POST'])
@login_required
def read_story(truyen_id, chuong_id):
    
    if request.method == 'POST':
            # Record reading history
        reading_history = ReadingHistory(
            user_id=current_user.id,
            truyen_id=truyen_id,
            chuong_id=chuong_id
            )
        reading_history=request.form['history-form']
        db.session.add(reading_history)
        db.session.commit()

        # Retrieve and display the chapter
    
    user = session.get('user')
    return render_template('User.html',user=user)

@main_bp.route('/update_reading_history/<int:history_id>', methods=['POST'])
@login_required
def update_reading_history(history_id):
    history = ReadingHistory.query.get(history_id)

    if history and history.user_id == current_user.id:
        # Handle logic for marking the chapter as read
        # For example, update a 'read' field in the ReadingHistory model
        history.read = True
        db.session.commit()

        flash('Chapter marked as read!', 'success')
    else:
        flash('Invalid request!', 'danger')

    return redirect(url_for('main.User'))
@main_bp.route('/User_history')
@login_required
def User_history():
    User_reading_history=current_user.reading_history.order_by(ReadingHistory.timestamp.desc()).all()

    return render_template('User.html',User_reading_history=User_reading_history)

@main_bp.route('/tien-nghich/<int:truyen_id>/chuong/<int:chuong_so>')
def tien_nghich_chuong(truyen_id, chuong_so):
    truyen, chuong_content, prev_chuong, next_chuong = get_chapter_info(truyen_id, chuong_so)
    chuong = Chuong.query.filter_by(truyen_id=truyen_id, Chuong_so=chuong_so).first()
    user= session.get('user')
    
    return render_template('tien_nghich_chuong.html', truyen=truyen,chuong=chuong, chuong_content=chuong_content, prev_chuong=prev_chuong, next_chuong=next_chuong, user=user)

@main_bp.route('/cau-ma/<int:truyen_id>/chuong/<int:chuong_so>')
def cau_ma_chuong(truyen_id, chuong_so):
    
    truyen, chuong_content, prev_chuong, next_chuong = get_chapter_info(truyen_id, chuong_so)
    chuong = Chuong.query.filter_by(truyen_id=truyen_id, Chuong_so=chuong_so).first()
    user= session.get('user')
    return render_template('cau_ma_chuong.html', truyen=truyen,chuong=chuong, chuong_content=chuong_content, prev_chuong=prev_chuong, next_chuong=next_chuong, user=user)

@main_bp.route('/huyenhuyen')
def huyenhuyen():
    # Add any logic if needed
    return render_template('huyenhuyen.html')
@main_bp.route('/linhdi')
def linhdi():
    # Add any logic if needed
    return render_template('linhdi.html')

@main_bp.route('/author')
def author():
    # Add any logic if needed
    return render_template('author.html')

@main_bp.route('/rank')
def rank():
    # Add any logic if needed
    return render_template('rank.html')

@main_bp.route('/tiennghich')
def tiennghich():
    
    truyen = Truyen.query.get(9)  # Thay 1 bằng Truyen_id mong muốn

    if not truyen:
        return "Truyen not found", 404

    chuong_list = Chuong.query.filter_by(truyen_id=truyen.Truyen_id).order_by(asc(Chuong.Chuong_so)).all()
    user= session.get('user')
    return render_template('tiennghich.html', truyen=truyen, chuong_list=chuong_list,user=user)

@main_bp.route('/cauma')
def cauma():
    truyen = Truyen.query.get(1)  # Thay 1 bằng Truyen_id mong muốn
    
    

    if not truyen:
        return "Truyen not found", 404

    chuong_list = Chuong.query.filter_by(truyen_id=truyen.Truyen_id).order_by(asc(Chuong.Chuong_so)).all()
    user= session.get('user')
    return render_template('cauma.html', truyen=truyen ,chuong_list=chuong_list,user=user)

@main_bp.route('/phamnhantutien')
def phamnhantutien():
    truyen = Truyen.query.get(7)  # Thay 1 bằng Truyen_id mong muốn
    
    

    if not truyen:
        return "Truyen not found", 404

    chuong_list = Chuong.query.filter_by(truyen_id=truyen.Truyen_id).order_by(asc(Chuong.Chuong_so)).all()
    user= session.get('user')
    return render_template('phamnhantutien.html')

@main_bp.route('/User')
def User():

    user= session.get('user')
    return render_template('User.html',user=user)

#followed truyen



@main_bp.route('/follow_truyen/<route_name>/<int:truyen_id>', methods=['POST'])
@login_required
def follow_truyen(route_name, truyen_id):
    truyen = Truyen.query.get(truyen_id)
    if truyen:
        followed_truyen = FollowedTruyen.query.filter_by(user=current_user, truyen=truyen).first()
        if not followed_truyen:
            current_user.followed_truyens.append(FollowedTruyen(truyen=truyen, route_name=route_name))
            db.session.commit()
    return redirect(url_for(f'main.{route_name}', truyen_id=truyen_id))

@main_bp.route('/unfollow_truyen/<route_name>/<int:truyen_id>', methods=['POST'])
@login_required
def unfollow_truyen(route_name, truyen_id):
    truyen = Truyen.query.get(truyen_id)
    if truyen:
        followed_truyen = FollowedTruyen.query.filter_by(user=current_user, truyen=truyen).first()
        if followed_truyen:
            db.session.delete(followed_truyen)
            db.session.commit()
    return redirect(url_for(f'main.{route_name}', truyen_id=truyen_id))