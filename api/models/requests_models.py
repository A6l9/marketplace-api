from pydantic import BaseModel, Field, field_validator


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
    