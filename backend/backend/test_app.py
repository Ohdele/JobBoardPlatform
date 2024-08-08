import pytest
from app import app, db, Job

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def get_jwt_token(client):
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    return response.json['access_token']

def test_create_job(client):
    token = get_jwt_token(client)
    headers = {'Authorization': f'Bearer {token}'}
    response = client.post('/jobs', json={
        'title': 'Test Job',
        'description': 'Test Description',
        'company': 'Test Company'
    }, headers=headers)
    assert response.status_code == 201
    assert b'Test Job' in response.data

def test_get_jobs(client):
    token = get_jwt_token(client)
    headers = {'Authorization': f'Bearer {token}'}
    client.post('/jobs', json={
        'title': 'Test Job',
        'description': 'Test Description',
        'company': 'Test Company'
    }, headers=headers)
    response = client.get('/jobs', headers=headers)
    assert response.status_code == 200
    assert b'Test Job' in response.data
