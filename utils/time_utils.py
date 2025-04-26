# utils/time_utils.py

import asyncio
import datetime

async def sleep_until_next_minute():
    """다음 0초가 될 때까지 대기한다."""
    now = datetime.datetime.now()
    next_minute = (now + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
    sleep_seconds = (next_minute - now).total_seconds()
    await asyncio.sleep(sleep_seconds)
