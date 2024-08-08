import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://jobboard_user:StrongPass!2024@localhost:3306/jobboard')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
