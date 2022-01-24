
import chat.routing
import os
import django

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application
django.setup()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'letschat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})
