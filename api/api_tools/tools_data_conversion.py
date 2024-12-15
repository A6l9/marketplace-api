from misc.initial import tmp_storage


async def data_conversion(data: list, valute: str, price_min: float | None,
                          price_max: float | None) -> list:
    """
    Function for currency conversion and price selection
    """
    list_data = []
    for i_elem in data:
        i_elem = i_elem.get_data()
        if valute != i_elem['currency']:
            if valute == 'USD':
                i_elem['price'] /= tmp_storage.valute_value
                i_elem['price'] = round(i_elem['price'], 2)
                i_elem['currency'] = 'USD'
            elif valute == 'RUB':
                i_elem['price'] *= tmp_storage.valute_value
                i_elem['price'] = round(i_elem['price'], 2)
                i_elem['currency'] = 'RUB'
        if price_min is not None:
            if price_min <= i_elem['price'] <= price_max:
                list_data.append(i_elem)
            else:
                continue
        else:
            list_data.append(i_elem)
        i_elem['date_of_adding'] = str(i_elem['date_of_adding'])
        i_elem['date_of_updating'] = str(i_elem['date_of_updating'])
    return list_data
