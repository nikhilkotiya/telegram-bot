import telegram # this is from python-telegram-bot package
 
from django.conf import settings
from django.template.loader import render_to_string
 
def post_event_on_telegram(event):
    message_html = render_to_string('telegram_message.html', {
        'event': event
    })
    telegram_settings = settings.TELEGRAM
    bot = telegram.Bot(token=telegram_settings['bot_token'])
    bot.send_message(chat_id="@%s" % telegram_settings['channel_name'],
        text=message_html, parse_mode=telegram.ParseMode.HTML)