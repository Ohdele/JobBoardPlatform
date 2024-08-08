from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(100), nullable=False)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username != 'testuser' or password != 'testpassword':
        return jsonify({"msg": "Bad credentials"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/jobs', methods=['POST'])
@jwt_required()
def create_job():
    data = request.json
    new_job = Job(title=data['title'], description=data['description'], company=data['company'])
    db.session.add(new_job)
    db.session.commit()
    return jsonify(id=new_job.id, title=new_job.title, description=new_job.description, company=new_job.company), 201

@app.route('/jobs', methods=['GET'])
@jwt_required()
def get_jobs():
    jobs = Job.query.all()
    return jsonify([{'id': job.id, 'title': job.title, 'description': job.description, 'company': job.company} for job in jobs]), 200

@app.route('/jobs/<int:job_id>', methods=['PUT'])
@jwt_required()
def update_job(job_id):
    data = request.json
    job = Job.query.get_or_404(job_id)
    job.title = data['title']
    job.description = data['description']
    job.company = data['company']
    db.session.commit()
    return jsonify(id=job.id, title=job.title, description=job.description, company=job.company), 200

@app.route('/jobs/<int:job_id>', methods=['DELETE'])
@jwt_required()
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return jsonify(message="Job deleted"), 200

if __name__ == '__main__':
    app.run(debug=True)
