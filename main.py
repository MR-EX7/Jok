#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 21081500, #get it from https://my.telegram.org/auth
    api_hash="e320c9fa51477b21b272d78f1ea85a9d", #get it from https://my.telegram.org/auth
    bot_token="6754293335:AAGH60DA16gre49vh6owdjHZsrDc402Ja-w", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        