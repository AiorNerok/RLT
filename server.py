import json
from aiogram import Bot, Dispatcher, executor, types

from tools import MongoDBTools
from schemas import MessageSchemas
from utils import aggregate_data
from config import Settings


class ServerBot:
    __bot = Bot(token=Settings.TELEGRAM_API_KEY)
    __dp = Dispatcher(bot=__bot)

    def __call__(self):
        return self.__dp

    @staticmethod
    @__dp.message_handler()
    async def cmd(message: types.Message):
        t = json.loads(message.text)
        msg = MessageSchemas(**t)
        r = MongoDBTools.select_range_collection(msg.dt_from, msg.dt_upto)
        result = [*r]

        answer = aggregate_data(msg.group_type, result)

        await message.answer(str(answer))


if __name__ == "__main__":
    try:
        dispatcher = ServerBot()
        executor.start_polling(dispatcher=dispatcher())
    except:
        dispatcher = ServerBot()
        executor.start_polling(dispatcher=dispatcher())
