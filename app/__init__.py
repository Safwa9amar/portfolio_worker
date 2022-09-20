from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app = Flask(__name__)
app.config['SECRET_KEY'] = '64684779753957c2a5e4fa32327601da'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
cors = CORS(app, resources={r"/blogs": {"origins": "http://localhost:3000"}})

db = SQLAlchemy(app)
ma = Marshmallow(app)
from app import routes
