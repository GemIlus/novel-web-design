from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db
import os
from .models import db, Truyen, Chuong,User,ReadingHistory
from datetime import datetime
from flask_login import LoginManager,UserMixin


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = os.urandom(24)

    # Initialize the database with the Flask app
    db.init_app(app)

    login_manager = LoginManager(app)
    

    @login_manager.user_loader
    def load_user(User_id):
        return User.query.get(int(User_id))
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
                                "Chuong_ten": chapter_file.split('.')[0],  
                                "Chuong_noidung": read_chapter_content(os.path.join(truyen_path, chapter_file)),  # Initialize with an empty string
                                "truyen_id": truyen.Truyen_id,
                                "Chuong_tieude": ""
                            }

                            chapter_file_path = os.path.join(truyen_path, chapter_file)
                            with open(chapter_file_path, 'r', encoding='utf-8') as file:
                                content_lines = file.readlines()
                                if content_lines:
                                    chapter_info["Chuong_tieude"] = content_lines[0].strip()
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