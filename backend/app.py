from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from backend.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/data', methods=['GET'])
def get_data():
    # Example query
    result = db.session.execute('SELECT * FROM your_table_name').fetchall()
    # Convert result to a list of dictionaries
    data = [{'id': row[0], 'column_name': row[1]} for row in result]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
