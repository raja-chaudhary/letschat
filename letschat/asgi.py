import os


from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import OriginValidator


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'letschat.settings')
django_asgi_app = get_asgi_application()

import chat.routing
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": OriginValidator(
	AuthMiddlewareStack(
        	URLRouter(
            	chat.routing.websocket_urlpatterns
        	)
	),
	[".herokuapp.com",],
    ),
})
