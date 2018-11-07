from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# init app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/monitor'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init others ,like url database
db = SQLAlchemy(app)
api = Api(app)

import monitor.apps.monitor_app.urls
import monitor.apps.monitor_app.models

db.create_all()
