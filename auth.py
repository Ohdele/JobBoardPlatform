from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask import Blueprint, request, jsonify

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # Implement user registration logic here (e.g., save user to database)
    return jsonify(message="User registered successfully"), 201

@auth.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # Implement user authentication here
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@auth.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="Protected endpoint")
