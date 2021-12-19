    
from telethon import TelegramClient
from telethon.errors.rpcerrorlist import SessionPasswordNeededError

api_id = '9857679'
api_hash = '1c7e9eb033428357a77320a94bb02d3b'

phone = '+918920243444'
username = 'Nikhil_k12'

# (2) Create the client and connect
from telethon import TelegramClient, events, sync

# Remember to use your own values from my.telegram.org!
api_id = '9857679'
api_hash = '1c7e9eb033428357a77320a94bb02d3b'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats='nikhil121ddd1_bot'))
async def my_event_handler(event):
    print(event.raw_text)

client.start()
client.run_until_disconnected()