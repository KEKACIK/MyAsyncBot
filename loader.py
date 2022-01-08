from aiogram import Bot, Dispatcher
import logging

from data.config import TOKEN
from handlers.database.sql import create_pool

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = dp.loop.run_until_complete(create_pool())