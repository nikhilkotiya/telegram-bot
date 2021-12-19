
from channels.generic.websocket import WebsocketConsumer,SyncConsumer
from asgiref.sync import async_to_sync
import json
# 2146792885:AAHJ3rF1CyX4Bx71V6cZmNrowT74T1s6E6M
from telethon import TelegramClient, events, sync

# api_id = 9857679
# api_hash = '1c7e9eb033428357a77320a94bb02d3b'
# from channels.consumer import AsyncConsumer

# class ChatConsumer(AsyncConsumer):
#     # async def websocket_connect(self, event):
#     client = TelegramClient('anon', api_id, api_hash)
#     @client.on(events.NewMessage(chats='nikhil121ddd1_bot'))
#     async def my_event_handler(event):
#         print(event.raw_text)

from telethon import TelegramClient, events, sync

# Remember to use your own values from my.telegram.org!
api_id = '9857679'
api_hash = '1c7e9eb033428357a77320a94bb02d3b'
class ChattyBotConsumer(WebsocketConsumer):
    def connect(self):
        self.username = "Anonymous"
        print(self.username)
        client = TelegramClient('anon', api_id, api_hash)
        @client.on(events.NewMessage(chats='nikhil121ddd1_bot'))
        async def my_event_handler(event):
            print(event.raw_text)
    def receive(self):
        pass
    def disconnect(self):
        pass

    # client.start()
    # client.run_until_disconnected()


# ChatConsumer()