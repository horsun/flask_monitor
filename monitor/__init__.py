from flask import Flask, render_template
from flask_restful import Api
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

# init app

app = Flask(__name__, static_folder='./statics/', static_url_path='/static/')
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/monitor'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init others ,like url、database
db = SQLAlchemy(app)
api = Api(app)
socketio = SocketIO(app)
import monitor.apps.monitor_app.models
import monitor.apps.monitor_app.views
import monitor.apps.monitor_app.urls

db.create_all()
if __name__ == '__main__':
    socketio.run(app, debug=True)
