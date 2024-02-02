import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage, RedisStorage2
from aioredis import Redis

from data import config
from utils.db_api.sqllite import Database

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
redis = RedisStorage2()

loop = asyncio.get_event_loop()
storage = MemoryStorage()
dp = Dispatcher(bot, storage=redis, loop=loop)
db = Database()
