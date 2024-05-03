import asyncio #позволит запускать асинхронные функции

from aiogram import Bot, Dispatcher

from handlers.default_handlers import start_command, help_command, menu_option
from callbacks import login_and_moove_callbacks, earn_write_skillcoins, back
from config_data.config_reader import BOT_TOKEN
from middleware.role_middleware import RoleMiddleware

async def main():
    bot = Bot(BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    dp.include_routers(
        start_command.router,
        help_command.router,
        menu_option.router,
        login_and_moove_callbacks.login.router,
        earn_write_skillcoins.earn_callback.router,
        back.router
    )
    dp.message.middleware.register(
        RoleMiddleware()
    )

    # Чтобы если вдруг бот будет выключенном состоянии и ему отправят 30000 соощений start
    # - бот их не выводил и поэтому применяем bot.delete_webhook
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())