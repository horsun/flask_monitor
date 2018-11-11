from threading import Lock

from flask import jsonify, render_template
from flask_restful import Resource
from flask_socketio import emit, Namespace, disconnect
import json
from monitor import socketio, app
from monitor.utils.linux_status import memory

thread = None
thread_lock = Lock()


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(1)
        count += 1
        socketio.emit('my_response',
                      {'data': json.dumps(memory()), 'count': count},
                      namespace='/test')


class Memory(Namespace):
    def on_my_ping(self):
        emit('my_pong')

    def on_connect(self):
        global thread
        with thread_lock:
            if thread is None:
                thread = socketio.start_background_task(
                    target=background_thread)
        emit('my_response', {'data': json.dumps(memory()), 'count': 0})

    def on_disconnect_request(self):
        emit('my_response')
        print('socket _disconnect')
        disconnect()


#
# @app.route('/')
# def index():
#     return render_template('memory.html', async_mode=socketio.async_mode)


@app.route('/')
def mem():
    return render_template('echats_test.html')


class World(Resource):
    def get(self):
        return jsonify({"hell": 'world'})
