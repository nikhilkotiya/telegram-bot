from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializer import ContactSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import permissions
import requests
from .models import Contact
import requests  
from bottle import Bottle, response, request as bottle_request


class BotHandlerMixin:  
    BOT_URL = None

    def get_chat_id(self, data):
        """
        Method to extract chat id from telegram request.
        """
        chat_id = data['message']['chat']['id']

        return chat_id

    def get_message(self, data):
        """
        Method to extract message id from telegram request.
        """
        message_text = data['message']['text']

        return message_text

    def send_message(self, prepared_data):
        """
        Prepared data should be json which includes at least `chat_id` and `text`
        """       
        message_url = self.BOT_URL + 'sendMessage'
        requests.post(message_url, json=prepared_data)


class TelegramBot(BotHandlerMixin, Bottle):  
    BOT_URL = 'https://api.telegram.org/bot2146792885:AAHJ3rF1CyX4Bx71V6cZmNrowT74T1s6E6M/'

    def __init__(self, *args, **kwargs):
        super(TelegramBot, self).__init__()
        self.route('/', callback=self.post_handler, method="POST")

    def change_text_message(self, text):
        return text[::-1]

    def prepare_data_for_answer(self, data):
        message = self.get_message(data)
        answer = self.change_text_message(message)
        chat_id = self.get_chat_id(data)
        json_data = {
            "chat_id": chat_id,
            "text": answer,
        }

        return json_data

    def post_handler(self,data):
        # data = bottle_request.json
        answer_data = self.prepare_data_for_answer(data)
        self.send_message(answer_data)

#         return response
def prepare_data_for_answer(data):
    json_data = {
        "text": data,
    }
    return json_data
def send_message(prepared_data):
    """
    Prepared data should be json which includes at least `chat_id` and `text`
    """       
    BOT_URL = 'https://api.telegram.org/bot2146792885:AAHJ3rF1CyX4Bx71V6cZmNrowT74T1s6E6M/sendMessage?chat_id=1087126687/'
    print("D")
    message_url = BOT_URL
    print(prepared_data)
    requests.post(message_url, json=prepared_data)
    print("done")
def post_handler(data):
    # data = bottle_request.json
    answer_data = prepare_data_for_answer(data)
    send_message(answer_data)
class ContactCreateAPI(CreateAPIView):
    serializer_class=ContactSerializer
    # permission_classes =(permissions.IsAuthenticated)
    permission_classes = [IsAuthenticated]
    def perform_create(self,serializer):
        serializer.save()
        """
        Prepared data should be json which includes at least `chat_id` and `text`
        """       
        m = serializer.data['messages']
        f = serializer.data['first_name']
        l = serializer.data['last_name']
        p = serializer.data['phone']
        text={"First name":f,"last name":l,"phone number":p ,"Message":m}
        print(text)
        post_handler(text)       
# from telethon import TelegramClient, events, sync

# api_id = '9857679'
# api_hash = '1c7e9eb033428357a77320a94bb02d3b'

# client = TelegramClient('session_name', api_id, api_hash)
# client.start()
# channel_username = '@nikhil121ddd1_bot'# your channel
    
       
       
       

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # print(serializer.messages)
        # data={'username':'test','message':"This is a testing message"}
        # url="https://api.telegram.org/bot2146792885:AAHJ3rF1CyX4Bx71V6cZmNrowT74T1s6E6M/sendMessage?chat_id=1087126687&text='{data}'"
        # r = requests.post(url, data = data)
        # if r.status_code == 200:
        #     data = r.json()
        #     print(data)
        #     # return Response(data, status=status.HTTP_200_OK)

# def index(request):
def index(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        messages = request.POST.get('messages')
        contact = Contact(first_name=first_name, last_name=last_name, phone=phone, messages=messages)
        contact.save()
        print('Done')
        # messages.success(request, 'Your message has been sent!')
    # return render(request, 'contact.html')
    return render(request ,'index.html')



from telethon import TelegramClient, events, sync
import aiohttp
# Remember to use your own values from my.telegram.org!
async def apidata(request):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.telegram.org/bot2146792885:AAHJ3rF1CyX4Bx71V6cZmNrowT74T1s6E6M/getUpdates") as res:
            data = await res.json()
            print(data)
    return render(request,"index.html",{"data":data})


def apidata(request):
    response=requests.get("https://api.telegram.org/bot2146792885:AAHJ3rF1CyX4Bx71V6cZmNrowT74T1s6E6M/getUpdates").json()
    return render(request,'index.html',{"data":response})