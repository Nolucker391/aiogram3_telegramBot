import asyncio #позволит запускать асинхронные функции

from aiogram import Bot, Dispatcher

from handlers.default_handlers import start_command
from callbacks.login_and_moove_callbacks import login
from config_data.config_reader import BOT_TOKEN

async def main():
    bot = Bot(BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    dp.include_routers(
        start_command.router,
        login.router
    )
    # Чтобы если вдруг бот будет выключенном состоянии и ему отправят 30000 соощений start
    # - бот их не выводил и поэтому применяем bot.delete_webhook
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())