try:
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from flask_jwt_extended import JWTManager
    from backend.config import Config  # Adjust path if needed
    from backend.auth import auth  # Adjust path if needed
    print("All imports are successful.")
except ImportError as e:
    print(f"ImportError: {e}")
