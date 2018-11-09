from monitor import api, socketio
from monitor.apps.monitor_app.views import World, Memory

api.add_resource(World, '/hello')
socketio.on_namespace(Memory('/test'))
