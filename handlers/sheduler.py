import datetime
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from config import bot, ADMINS


async def send_message_date(bot: Bot):
    await bot.send_message(ADMINS[0], "happy 23 February!")


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone='Asia/Bishkek')

    scheduler.add_job(
        send_message_date,
        trigger=DateTrigger(
            run_date=datetime.datetime(year=2023, month=2, day=14, hour=00, minute=1)
        ),
        kwargs={"bot": bot},
    )

    scheduler.start()