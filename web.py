import requests
from bs4 import BeautifulSoup
import telegram
import time

bot_token = '6530567542:AAGrU4WX3IuY8hiZXRunhHYY8MB3hT5LMk8'
bot_chat_id = '788123983'
bot = telegram.Bot(token=bot_token)

async def send_message_to_telegram_channel():

    url = 'https://www.fanabc.com/archives/category/localnews'
    response = requests.get(url)
   
    s = BeautifulSoup(response.text, 'html.parser')
    sss = s.find_all(class_='item-inner clearfix')
    title = s.find_all(class_='title')
    post = s.find_all(class_='post-summary')
   
    for i in range(6):
       
        message = ''
        message = title[i + 4].text + '\n' + post[i].text
       
        await bot.send_message(chat_id=bot_chat_id, text=message)
        time.sleep(10)
import asyncio

asyncio.run(send_message_to_telegram_channel())


