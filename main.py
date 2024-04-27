import asyncio #позволит запускать асинхронные функции

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode


bot = Bot('7183072253:AAF6GrqsebhJU-9W6TE3rXyic1iSiOo70AQ', parse_mode=ParseMode.HTML)
dp = Dispatcher()

async def main():
    # Чтобы если вдруг бот будет выключенном состоянии и ему отправят 30000 соощений start
    # - бот их не выводил и поэтому применяем bot.delete_webhook
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())