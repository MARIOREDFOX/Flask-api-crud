from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
ma = Marshmallow(app)

from view import *
from app import db

db.init_app(app)

# Run Server
if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1')
