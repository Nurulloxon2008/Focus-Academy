import asyncio
import logging

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.start import startRT
from handlers.keyboardHandler import keyboardHandlerRT
from handlers.echo import router  
from loader import bot

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(level=logging.INFO)
    logger.info("Starting bot")

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(startRT)
    dp.include_router(keyboardHandlerRT)
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")

