import os
import django
    
from channels.routing import ProtocolTypeRouter , URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot.settings')
from app.consumer import ChattyBotConsumer
from django.urls import path
django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter([
        # url(r"^chat/admin/$", AdminChatConsumer.as_asgi()),
        path("", ChattyBotConsumer.as_asgi()),
    ]),
})

# import os
# import django
# # from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# # import chat.routing
# from channels.http import AsgiHandler
# from django.urls import path
# from app.consumer import ChatConsumer
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bot.settings")
# # django.setup()
# django_asgi_app = get_asgi_application()
# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     "websocket": URLRouter([
#         # url(r"^chat/admin/$", AdminChatConsumer.as_asgi()),
#         path("chat/", ChatConsumer.as_asgi()),
#     ]),

#     # "telegram": ChattyBotConsumer.as_asgi(),
# })