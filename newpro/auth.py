from flask import Flask, render_template, request, redirect, url_for, session, flash, Blueprint
from flask_login import login_user, login_required, logout_user
from newpro.models import User, db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['login-username']
        password = request.form['login-password']

        # Check if the provided credentials are valid using the database
        user = User.query.filter_by(Username=username, Password=password).first()
        if user:
            # Use Flask-Login's login_user function to log in the user
            login_user(user)

            # Redirect to the home page or any other page after successful login
            session['user'] = username
            return redirect(url_for('main.index'))
        else:
            flash('Wrong password or username!', 'error')

    # Render the login page if it's a GET request or if the login fails
    return render_template('login.html')

# Log out
@auth.route('/logout')
@login_required  # Ensure that only logged-in users can access this route
def logout():
    # Use Flask-Login's logout_user function to log out the user
    logout_user()

    # Clear the 'user' session variable
    session.pop('user', None)

    # Redirect to the home page or any other page after logout
    return redirect(url_for('main.index'))

# Create account
@auth.route('/createaccount', methods=['GET', 'POST'])
def createaccount():
    if request.method == 'POST':
        # Process the form data for creating an account
        # Add your logic here for creating a new account
        username = request.form['create-username']
        password = request.form['create-password']

        # Check if the username is already taken
        existing_user = User.query.filter_by(Username=username).first()
        if existing_user:
            flash('Username already taken!', 'error')
        else:
            # Create a new user and add it to the database
            new_user = User(Username=username, Password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Create account successfully!')

        # For now, let's just redirect to the login page after account creation
        return redirect(url_for('auth.login'))

    # Render the create account page if it's a GET request
    return render_template('createaccount.html')
