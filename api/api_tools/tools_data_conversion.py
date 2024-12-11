from misc.initial import tmp_storage


async def data_conversion(data: dict, valute: str) -> dict:
    if valute != data['currency']:
        if valute == 'USD':
            data['price'] /= tmp_storage.valute_value
        elif valute == 'RUB':
            data['price'] *= tmp_storage.valute_value
    return data
