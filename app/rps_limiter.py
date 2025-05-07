import asyncio
from datetime import datetime, timedelta
from typing import Callable

from app.config import HHSettings

hh = HHSettings()


class RPSLimiter:
    
    def __init__(self):
        self.semaphore = asyncio.Semaphore(hh.RPS)
        self.last_request_time = datetime.now()
        self.interval = timedelta(seconds=(1 / hh.RPS))
        
    async def request(self, func: Callable, *args, **kwargs):
        
        async with self.semaphore:
            elapsed = datetime.now() - self.last_request_time
            
            if elapsed < self.interval:
                await asyncio.sleep(self.interval.total_seconds() - elapsed.total_seconds())
            
            self.last_request_time = datetime.now()
            return await func(*args, **kwargs)