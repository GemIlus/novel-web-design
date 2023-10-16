from flask import Flask, render_template, request, redirect, url_for ,session ,flash,get_flashed_messages,Blueprint
from os import path
import os
from flask_sqlalchemy import SQLAlchemy 
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
@main_bp.route('/tien_nghich_chuong_1')
def tien_nghich_chuong_1():
    # Add any logic if needed
    return render_template('tien_nghich_chuong_1.html')
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
    return render_template('tiennghich.html')

@main_bp.route('/phamnhantutien')
def phamnhantutien():
    return render_template('phamnhantutien.html')

# @main_bp.route('/login', methods=['GET', 'POST'])
# def login():
    # if request.method == 'POST':
    #     username = request.form['login-username']
    #     password = request.form['login-password']
        
    #     # Check if the provided credentials are valid using the database
    #     user = User.query.filter_by(Username=username, Password=password).first()
    #     if user:
    #         # Redirect to the home page or any other page after successful login
    #         session['user'] = username
    #         return redirect(url_for('index'))
    #     else:
    #         flash('Wrong password or username!', 'error')
            
    # Render the login page if it's a GET request or if the login fails
    # return render_template('login.html')

# log-out
# @main_bp.route('/logout')
# def logout():
#     session.pop('user', None)
#     return redirect(url_for('index'))

#create-account
# @main_bp.route('/createaccount', methods=['GET', 'POST'])
# def createaccount():
    # if request.method == 'POST':
    #     # Process the form data for creating an account
    #     # Add your logic here for creating a new account
    #     username = request.form['create-username']
    #     password = request.form['create-password']

    #     # Check if the username is already taken
    #     existing_user = User.query.filter_by(Username=username).first()
    #     if existing_user:
    #         flash('Username already taken!', 'error')
    #     else:
    #         # Create a new user and add it to the database
    #         new_user = User(Username=username, Password=password)
    #         db.session.add(new_user)
    #         db.session.commit()
    #         flash('Create account successfully!')

    #     # For now, let's just redirect to the login page after account creation
        # return redirect(url_for('login'))

    # Render the create account page if it's a GET request
    # return render_template('createaccount.html')