import asyncio

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from data.database import db_start

from handlers import user_commands, bot_messages

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        bot_messages.router
    )
    await db_start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
