try:
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from flask_jwt_extended import JWTManager
    from config import Config
    from auth import auth
    print("All imports are successful.")
except ImportError as e:
    print(f"ImportError: {e}")
