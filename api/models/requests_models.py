from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional


class RequestGoodsByIdModel(BaseModel):
    
    id: int = Field(alias='id')
    currency: str = Field(alias='currency') 

    
    @field_validator('currency', mode='before')
    @classmethod
    def check_currency(cls, value: str) -> str:
        if value.upper() not in ['USD', 'RUB']:
            raise ValueError('The currency must be either USD or RUB')
        return value.upper()


class RequestAddGoodsModel(BaseModel):

    name: str = Field(alias='name')
    description: str = Field(alias='description')
    category: str = Field(alias='category')
    price :float = Field(alias='price')   
    currency: str = Field(alias='currency') 

    
    @field_validator('currency', mode='before')
    @classmethod
    def check_currency(cls, value: str) -> str:
        if value.upper() not in ['USD', 'RUB']:
            raise ValueError('The currency must be either USD or RUB')
        return value.upper()


class RequestUpdateGoodsModel(BaseModel):

    name: str = Field(alias='name')
    description: str = Field(alias='description')
    category: str = Field(alias='category')
    price :float = Field(alias='price')   
    currency: str = Field(alias='currency') 

    
    @field_validator('currency', mode='before')
    @classmethod
    def check_currency(cls, value: str) -> str:
        if value.upper() not in ['USD', 'RUB']:
            raise ValueError('The currency must be either USD or RUB')
        return value.upper()
    

class CurrencyModel(BaseModel):
    currency: str = Field(alias='currency')
    price_min: Optional[float] = Field(alias='price_min')
    price_max: Optional[float] = Field(alias='price_max') 

    
    @model_validator(mode='before')
    @classmethod
    def check_prices(cls, values: dict) -> dict:
        if values.get('price_min') and values.get('price_max'):
            if values['price_min'] > values['price_max']:
                raise ValueError('The price_min must be less than or equal to price_max')
        elif ((values.get('price_min') is None and values.get('price_max')) or 
              (values.get('price_min') and values.get('price_max') is None)):
            raise ValueError('Please fill in the price_min and price_max fields')
        return values

    @field_validator('currency', mode='before')
    @classmethod
    def check_currency(cls, value: str) -> str:
        if value.upper() not in ['USD', 'RUB']:
            raise ValueError('The currency must be either USD or RUB')
        return value.upper()
    
    @field_validator("price_min", mode='before')
    @classmethod
    def check_price_min(cls, value: Optional[float]) -> Optional[float]:
        if value:
            if value < 0:
                raise ValueError('The price_min must be a non-negative number')
        return value
    