from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
import csv
from unidecode import unidecode
import autoit
import random
import os
from datetime import timedelta, datetime
import time
from statistics import mean
import re
from textblob import TextBlob
from langdetect import detect
from progress.bar import IncrementalBar
import langid
from deep_translator import GoogleTranslator
from langdetect import detect
import string
import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import link
from typing import Optional
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified
import tracemalloc
API_TOKEN = '5937208538:AAFz8jc9ne-yycmFN71Gjq3Oo2XMJkTuCmU'
options = Options()
#options.add_argument('--proxy-server=176.9.119.170:1080	')
#options.add_argument("no-sandbox")
options.add_argument('--disable-logging')
options.add_argument('--incognito')
options.add_argument('--disable-infobars')
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")
#options.add_argument("--host-resolver-rules=MAP www.google-analytics.com 127.0.0.1")
options.add_argument("no-default-browser-check")
options.add_argument("no-first-run")
def check_exists(driver,way,name):
    try:
        driver.find_element(way,name)
    except Exception:
        return False
    return True
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", chrome_options=options
)
vote_cb = CallbackData('vote','action', 'stream_title','time_callback')
tracemalloc.start()
driver.get("https://stopgame.ru/live_schedule")
while check_exists(driver,'xpath','//div[@data-key]') == False:
    time.sleep(1)
all_streams = driver.find_elements('xpath','//div[@data-key]')
f = 1
for i in all_streams:
    #print(i.text)
    date_and_time = i.find_elements('xpath',"//div[@data-key]["+str(f)+"]//div[contains(@class, '_stream-info__item')]")
    
    date = date_and_time[0].text
    time1  = date_and_time[1].text
    # print(date)
    # print(time)
    name = i.find_element('xpath',"//div[@data-key]["+str(f)+"]//div[contains(@class, '_stream-content')]")
    title = name.text
    # print(title)
    
    members = i.find_element('xpath',"//div[@data-key]["+str(f)+"]//div[contains(@class, '_stream-streamers')]")
    members_names = members.text.split(":")[1]
    members_names = members_names.split("\n")
    members_names = members_names[1:]
    # print(members_names)
    members_links_web_elements=  i.find_elements('xpath',"//div[@data-key]["+str(f)+"]//div[contains(@class, '_stream-streamer')]//a")
    members_links = []
    for k in members_links_web_elements:
        
        members_links.append(k.get_attribute("href"))
    # print(members_links)
    # print(members.text)
    members_text =""
    k = 0
    for j in members_names:
        members_text = members_text + f'<a href = '+members_links[k]+'>'+j+'</a>'
        k+= 1
    print(members_text)
    try:
        image_source = i.find_element('xpath',"//div[@data-key]["+str(f)+"]//img[contains(@class, '_stream-poster')]").get_attribute("src")
    except:
        image_source = "https://sun9-81.userapi.com/impg/EEBK-5_stvYJKBk3H06exEnuPaDTwvEx9OLYww/ag7wJ0-Ptlk.jpg?size=1000x1000&quality=95&sign=9b89aeb45240e00ea28925b252173def&type=album"
    # print(image_source.get_attribute("src"))
    
    
    
    
    # print()
    f+=1
    
        
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def on_startup(dp): 
    asyncio.create_task(scheduler())
    print("ready")



    

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    inline_btn_1 = InlineKeyboardButton('Получить расписание', callback_data='raspisanie')
    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет я бот который поможет оставаться в курсе о стримах канала StopGame.ru", reply_markup=inline_kb1)
@dp.callback_query_handler(lambda c: c.data == 'raspisanie')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    
    
    f = 1
    for i in all_streams:
        date_and_time = i.find_elements('xpath',"//div[@data-key]["+str(f)+"]//div[contains(@class, '_stream-info__item')]")
        date = date_and_time[0].text
        time1 = date_and_time[1].text
        # print(date)
        # print(time)
        name = i.find_element('xpath',"//div[@data-key]["+str(f)+"]//div[contains(@class, '_stream-content')]")
        title = name.text
        # print(title)
        members = i.find_element('xpath',"//div[@data-key]["+str(f)+"]//div[contains(@class, '_stream-streamers')]")
        members_names = members.text.split(":")[1]
        members_names = members_names.split("\n")
        members_names = members_names[1:]
        # print(members_names)
        members_links_web_elements=  i.find_elements('xpath',"//div[@data-key]["+str(f)+"]//div[contains(@class, '_stream-streamer')]//a")
        members_links = []
        for k in members_links_web_elements:
        
            members_links.append(k.get_attribute("href"))
        # print(members_links)
        # print(members.text)
        try:
            image_source = i.find_element('xpath',"//div[@data-key]["+str(f)+"]//img[contains(@class, '_stream-poster')]").get_attribute("src")
        except:
            image_source = "https://sun9-81.userapi.com/impg/EEBK-5_stvYJKBk3H06exEnuPaDTwvEx9OLYww/ag7wJ0-Ptlk.jpg?size=1000x1000&quality=95&sign=9b89aeb45240e00ea28925b252173def&type=album"
        # print(image_source.get_attribute("src"))
        f+=1
        members_text ="Участники: \n" 
        k = 0
        for j in members_names:
            members_text = members_text +'<a href="'+members_links[k]+'">'+j+'</a>' +"\n"
            k+= 1
        msg = str(title + "\n"+ "\n" + members_text +"\n" + date + "\n" + time1)
        image = image_source
        
        
        
        keyboard = types.InlineKeyboardMarkup(row_width=2).add(types.InlineKeyboardButton('Получить расписание', callback_data=vote_cb.new(action='raspisanie',stream_title=title[0:15],time_callback=0)))
        keyboard.add(types.InlineKeyboardButton('Поставить уведомление на '+title[0:15]+"...", callback_data=vote_cb.new(action='uvedomlenie', stream_title=title[0:15],time_callback = time1)))           
        
        
        
        
        
        # inline_btn_1 = InlineKeyboardButton('Получить расписание', callback_data='raspisanie')
        # inline_btn_12= InlineKeyboardButton('Поставить уведомление на '+title[0:15]+"...", callback_data='uvedomlenie' + title[0:15])
        # inline_kb1 = InlineKeyboardMarkup(row_width=1).add(inline_btn_12,inline_btn_1)
        await bot.send_photo(callback_query.from_user.id,photo =image, caption=msg,parse_mode="HTML",reply_markup=keyboard)
    f = 0

@dp.callback_query_handler(vote_cb.filter(action='raspisanie'))
async def raspisanie_from_raspisanie(query: types.CallbackQuery, callback_data: dict):


    f = 1
    for i in all_streams:
        date_and_time = i.find_elements('xpath',"//div[@data-key]["+str(f)+"]//div[contains(@class, '_stream-info__item')]")
        date = date_and_time[0].text
        time1 = date_and_time[1].text
        # print(date)
        # print(time)
        name = i.find_element('xpath',"//div[@data-key]["+str(f)+"]//div[contains(@class, '_stream-content')]")
        title = name.text
        # print(title)
        members = i.find_element('xpath',"//div[@data-key]["+str(f)+"]//div[contains(@class, '_stream-streamers')]")
        members_names = members.text.split(":")[1]
        members_names = members_names.split("\n")
        members_names = members_names[1:]
        # print(members_names)
        members_links_web_elements=  i.find_elements('xpath',"//div[@data-key]["+str(f)+"]//div[contains(@class, '_stream-streamer')]//a")
        members_links = []
        for k in members_links_web_elements:
        
            members_links.append(k.get_attribute("href"))
        # print(members_links)
        # print(members.text)
        try:
            image_source = i.find_element('xpath',"//div[@data-key]["+str(f)+"]//img[contains(@class, '_stream-poster')]").get_attribute("src")
        except:
            image_source = "https://sun9-81.userapi.com/impg/EEBK-5_stvYJKBk3H06exEnuPaDTwvEx9OLYww/ag7wJ0-Ptlk.jpg?size=1000x1000&quality=95&sign=9b89aeb45240e00ea28925b252173def&type=album"
        f+=1
        members_text ="Участники: \n" 
        k = 0
        for j in members_names:
            members_text = members_text +'<a href="'+members_links[k]+'">'+j+'</a>' +"\n"
            k+= 1
        msg = str(title + "\n"+ "\n" + members_text +"\n" + date + "\n" + time1)
        image = image_source
        
        
        
        keyboard = types.InlineKeyboardMarkup(row_width=2).add(types.InlineKeyboardButton('Получить расписание', callback_data=vote_cb.new(action='raspisanie',stream_title=title[0:15],time_callback=0)))
        keyboard.add(types.InlineKeyboardButton('Поставить уведомление на '+title[0:15]+"...", callback_data=vote_cb.new(action='uvedomlenie', stream_title=title[0:15],time_callback = time1)))           
        
        
        
        
        
    # inline_btn_1 = InlineKeyboardButton('Получить расписание', callback_data='raspisanie')
    # inline_btn_12= InlineKeyboardButton('Поставить уведомление на '+title[0:15]+"...", callback_data='uvedomlenie' + title[0:15])
    # inline_kb1 = InlineKeyboardMarkup(row_width=1).add(inline_btn_12,inline_btn_1)
        await bot.send_photo( query.from_user.id,photo =image, caption=msg,parse_mode="HTML",reply_markup=keyboard)
    
          
@dp.message_handler()
async def send_uved(id,title_func):
    await bot.send_message(chat_id = id, text = title_func)
    return schedule.CancelJob


@dp.callback_query_handler(vote_cb.filter(action='uvedomlenie'))
async def make_uved(query: types.CallbackQuery, callback_data: dict):
    logging.info(callback_data)
    strm_title = (callback_data['stream_title'])
    time_info = (callback_data['time_callback'])
    time_info = time_info.split("\n")[0]
    time_info = time_info.replace(".",":")
    print()
    print()
    print(time_info)
    print()
    print()
    schedule.every().day.at(time_info).do(send_uved(id = query.from_user.id,title_func = strm_title))
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)
    # schedule.every(20).seconds.do(job_that_executes_once(id = query.from_user.id,title_func = strm_title))
    # await bot.send_message(query.from_user.id, "132")
    # while True:
        # await aioschedule.run_pending()
        # await asyncio.sleep(1)
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


