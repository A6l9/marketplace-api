from misc.initial import tmp_storage


async def data_conversion(data: dict, valute: str) -> dict:
    if valute != data['currency']:
        if valute == 'USD':
            data['price'] /= tmp_storage.valute_value
            data['price'] = round(data['price'], 2)
            data['currency'] = 'USD'
        elif valute == 'RUB':
            data['price'] *= tmp_storage.valute_value
            data['price'] = round(data['price'], 2)
            data['currency'] = 'RUB'
    data['date_of_adding'] = str(data['date_of_adding'])
    data['date_of_updating'] = str(data['date_of_updating'])
    return data
