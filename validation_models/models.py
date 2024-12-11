from pydantic import Field, field_validator, BaseModel


class GoodsValidationModel(BaseModel):

    price: float = Field(name='price')
    current_currency: str = Field('current_currency')
    currency: str = Field(name='currency')
    
    @classmethod
    def convert_price(cls, price, currency, convert_currency) -> float:
        if currency != convert_currency:
            if currency == 'USD' and convert_currency == 'RUB':
                price *= 100
            elif currency == 'RUB' and convert_currency == 'USD':
                price /= 100
        return price    