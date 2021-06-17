from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisismysecretapp'
app.config['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)


@app.route('/user', methods=['GET'])
def get_all_users():
    return jsonify([
      {'user': 'user 1'},
      {'user': 'user 2'},
      {'user': 'user 3'},
    ])


if __name__ == '__main__':
    app.run(debug=True)
