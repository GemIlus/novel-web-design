from flask import Flask, render_template, request, redirect, url_for ,session ,flash,get_flashed_messages,Blueprint
from os import path
import os
from flask_sqlalchemy import SQLAlchemy 
from .models import db, Truyen, Chuong
from sqlalchemy import asc
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    user= session.get('user')
    return render_template('index.html', user=user)
@main_bp.route('/catalog')
def catalog():
    # Add any logic if needed
    return render_template('catalog.html')

@main_bp.route('/tienhiep')
def tienhiep():
    # Add any logic if needed
    return render_template('tienhiep.html')
@main_bp.route('/truyen/<int:truyen_id>/chuong/<int:chuong_so>')
def tien_nghich_chuong(truyen_id, chuong_so):
    def get_chuong_content(truyen_id, chuong_so):
    
        chuong = Chuong.query.filter_by(truyen_id=truyen_id, Chuong_so=chuong_so).first()

        # Check if the chapter exists
        if chuong:
            return chuong.Chuong_noidung
        else:
            return "Chapter not found" 

    # Assuming you have a method to retrieve chapter content by truyen_id and chuong_so
    chuong_content = get_chuong_content(truyen_id, chuong_so)

    # Render the template with the chapter content
    return render_template('tien_nghich_chuong.html', chuong_content=chuong_content)
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
    truyen = Truyen.query.get(1)  # Thay 1 bằng Truyen_id mong muốn

    if not truyen:
        return "Truyen not found", 404

    chuong_list = Chuong.query.filter_by(truyen_id=truyen.Truyen_id).order_by(asc(Chuong.Chuong_so)).all()

    return render_template('tiennghich.html', truyen=truyen, chuong_list=chuong_list)

@main_bp.route('/phamnhantutien')
def phamnhantutien():
    return render_template('phamnhantutien.html')
@main_bp.route('/truyen/<int:truyen_id>/chuong/<int:chuong_so>')
def view_chuong(truyen_id, chuong_so):
    def get_chuong_content(truyen_id, chuong_so):
    # Assuming you have a model for Chuong and a corresponding column for content
        chuong = Chuong.query.filter_by(truyen_id=truyen_id, Chuong_so=chuong_so).first()

    # Check if the chapter exists
        if chuong:
            return chuong.Chuong_noidung
        else:
            return "Chapter not found" 
    # Assuming you have a method to retrieve chapter content by truyen_id and chuong_so
    chuong_content = get_chuong_content(truyen_id, chuong_so)

    # Render the template with the chapter content
    return render_template('chuong.html', chuong_content=chuong_content)

