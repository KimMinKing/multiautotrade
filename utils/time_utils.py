# utils/time_utils.py

import asyncio
import datetime

async def sleep_until_next_minute():
    """다음 0초가 될 때까지 대기한다."""
    now = datetime.datetime.now()
    next_minute = (now + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
    sleep_seconds = (next_minute - now).total_seconds()
    await asyncio.sleep(sleep_seconds)

def should_execute_strategy(strategy, now):
    """현재 시간이 전략 실행 타이밍이면 True"""
    # 전략이 주기를 가지고 있다고 가정. (예: strategy.interval_minutes)
    interval = getattr(strategy, 'interval_minutes', 1)  # 기본 1분
    if interval == 1:
        return now.second == 0
    elif interval == 5:
        return now.minute % 5 == 0 and now.second == 0
    elif interval == 15:
        return now.minute % 15 == 0 and now.second == 0
    elif interval == 60:
        return now.minute == 0 and now.second == 0
    else:
        return False