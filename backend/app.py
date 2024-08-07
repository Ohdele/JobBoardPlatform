from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from auth import auth

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from flask_jwt_extended import JWTManager
jwt = JWTManager(app)

@app.route('/')
def home():
    return 'Hello, Flask!'

app.register_blueprint(auth)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
