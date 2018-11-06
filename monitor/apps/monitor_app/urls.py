from monitor import api
from monitor.apps.monitor_app.views import World

api.add_resource(World, '/hello')
