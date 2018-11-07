from monitor import api, socketio
from monitor.apps.monitor_app.views import World, MyNamespace

api.add_resource(World, '/hello')
socketio.on_namespace(MyNamespace('/test'))
