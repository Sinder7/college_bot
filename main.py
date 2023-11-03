from aiogram import Bot, Dispatcher
import asyncio
import logging

from routers import user, admin

from settings import settings

async def main() -> None:

    logging.basicConfig(level=logging.DEBUG)


    dp = Dispatcher()
    bot = Bot(token=settings.bot.token)

    dp.include_routers(user.router)
    dp.include_routers(admin.router)

    try:
        await dp.start_polling(bot)
    except:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())