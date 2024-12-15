import aiohttp
import asyncio
from loguru import logger
import json
from misc.initial import tmp_storage


class Parser:

    def __init__(self):
        self.url: str = 'https://www.cbr-xml-daily.ru/daily_json.js'
    
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

            logger.info(f'Going to sleep for {1} hour')
            await asyncio.sleep(3600)


async def main():
    parser = Parser()
    await parser.start()
