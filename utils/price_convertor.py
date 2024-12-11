import aiohttp
import pendulum
import asyncio
from loguru import logger
import json
from misc.initial import tmp_storage


class Parser:

    def __init__(self):
        self.url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    
    async def start(self):
        while True:
            for _ in range(5):
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(self.url) as response:
                            if response.status == 200:
                                response = await response.text()
                                data = json.loads(response)
                                tmp_storage.valute_value = data['Valute']['USD']['Value']
                                logger.info(f'Current value: {data['Valute']['USD']['Value']}. Data successfully stored in storage')
                                break
                            else:
                                logger.warning(f'Failed to fetch data. Status code: {response.status}')
                                continue
                except Exception as exc:
                    logger.exception(exc)

            today = pendulum.now(tz='UTC')
            collection_time = pendulum.datetime(year=today.year, 
                                                month=today.month, 
                                                day=today.day + 1,
                                                hour=9, 
                                                minute=0,
                                                second=0,
                                                microsecond=0,
                                                tz='UTC')
            sleep_duration = collection_time.diff(today)
            logger.info(f'Going to sleep for {sleep_duration.hours} hours')
            await asyncio.sleep(sleep_duration.seconds)


async def main():
    parser = Parser()
    await parser.start()
