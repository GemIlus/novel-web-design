# newpro/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db
import os
from .models import db, Truyen, Chuong
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = os.urandom(24)

    # Initialize the database with the Flask app
    db.init_app(app)

    # Import and register your Blueprints after initializing the app
    from newpro.views import main_bp
    from newpro.auth import auth

    app.register_blueprint(main_bp)
    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()

    return app

def insert_data_from_folders(data_folder):

    app=create_app()

    with app.app_context():
        for truyen_folder in os.listdir(data_folder):
            truyen_path = os.path.join(data_folder, truyen_folder)
            if os.path.isdir(truyen_path):
            # Check if Truyen with the same name already exists
                existing_truyen = Truyen.query.filter_by(Truyen_ten=truyen_folder).first()

                if not existing_truyen:
                    truyen_info = {
                    "Truyen_ten": truyen_folder,
                    # Add other Truyen attributes as needed
                }


                    truyen = Truyen(**truyen_info)
                    db.session.add(truyen)
                    db.session.commit()  # Commit the changes to get the Truyen_id

                    for chapter_file in os.listdir(truyen_path):
                        if chapter_file.endswith(".txt"):
                            chapter_info = {
                                "Chuong_so": int(''.join(filter(str.isdigit, chapter_file.split('.')[0]))),
                                "Chuong_ten": chapter_file.split('.')[0],  # You might need to adjust this based on your data
                                "Chuong_noidung": read_chapter_content(os.path.join(truyen_path, chapter_file)),  # Initialize with an empty string
                                "truyen_id": truyen.Truyen_id
                            }

                            chapter_file_path = os.path.join(truyen_path, chapter_file)
                            with open(chapter_file_path, 'r', encoding='utf-8') as file:
                                chapter_info["Chuong_noidung"] = file.read()

                            chuong = Chuong(**chapter_info)
                            db.session.add(chuong)
        db.session.commit()

def read_chapter_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"Error reading content from {file_path}: {e}")
        return "Unknown"
# Replace 'your_data_folder' with the actual path to your folder containing novels
insert_data_from_folders(r'D:/web/newpro/data/truyen_chu')


# app = Flask(__name__)
# app.secret_key = os.urandom(24)
# app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///user.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
# app.register_blueprint(auth, url_prefix='/')
# db=SQLAlchemy()
# def create_app():
#     app = Flask(__name__)
#     app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     app.secret_key = os.urandom(24)
#     # Initialize the database with the Flask app
#     db.init_app(app)

#     # Import and register your blueprints here if you have any

#     return app
    
# class User(db.Model):
#     user_id=db.Column(db.Integer, primary_key= True)
#     Username =db.Column(db.String(100))
#     Password=db.Column(db.String(100))

#     def __init__(self,Username, Password):
#         self.Username = Username
#         self.Password = Password 

# #Create the database tables
# with app.app_context():
#     db.create_all()

# @app.route('/')
# def index():
#     user= session.get('user')
#     return render_template('index.html', user=user)
# @app.route('/catalog')
# def catalog():
#     # Add any logic if needed
#     return render_template('catalog.html')

# @app.route('/tienhiep')
# def tienhiep():
#     # Add any logic if needed
#     return render_template('tienhiep.html')
# @app.route('/tien_nghich_chuong_1')
# def tien_nghich_chuong_1():
#     # Add any logic if needed
#     return render_template('tien_nghich_chuong_1.html')
# @app.route('/huyenhuyen')
# def huyenhuyen():
#     # Add any logic if needed
#     return render_template('huyenhuyen.html')
# @app.route('/linhdi')
# def linhdi():
#     # Add any logic if needed
#     return render_template('linhdi.html')

# @app.route('/author')
# def author():
#     # Add any logic if needed
#     return render_template('author.html')

# @app.route('/rank')
# def rank():
#     # Add any logic if needed
#     return render_template('rank.html')

# @app.route('/tiennghich')
# def tiennghich():
#     return render_template('tiennghich.html')

# @app.route('/phamnhantutien')
# def phamnhantutien():
#     return render_template('phamnhantutien.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['login-username']
#         password = request.form['login-password']
        
#         # Check if the provided credentials are valid using the database
#         user = User.query.filter_by(Username=username, Password=password).first()
#         if user:
#             # Redirect to the home page or any other page after successful login
#             session['user'] = username
#             return redirect(url_for('index'))
#         else:
#             flash('Wrong password or username!', 'error')
            
#     # Render the login page if it's a GET request or if the login fails
#     return render_template('login.html')

# #log-out
# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     return redirect(url_for('index'))

# #create-account
# @app.route('/createaccount', methods=['GET', 'POST'])
# def createaccount():
#     if request.method == 'POST':
#         # Process the form data for creating an account
#         # Add your logic here for creating a new account
#         username = request.form['create-username']
#         password = request.form['create-password']

#         # Check if the username is already taken
#         existing_user = User.query.filter_by(Username=username).first()
#         if existing_user:
#             flash('Username already taken!', 'error')
#         else:
#             # Create a new user and add it to the database
#             new_user = User(Username=username, Password=password)
#             db.session.add(new_user)
#             db.session.commit()
#             flash('Create account successfully!')

#         # For now, let's just redirect to the login page after account creation
#         return redirect(url_for('login'))

#     # Render the create account page if it's a GET request
#     return render_template('createaccount.html')



# if __name__ == '__main__':
#     app.run(debug= True)


