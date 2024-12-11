from pydantic import BaseModel, Field, field_validator, model_validator


class RequestGoodsModel(BaseModel):
    
    min_pice: int = Field(alias='min_pice')
    max_pice: int = Field(alias='max_pice')
    category: str = Field(alias='category')
    currency: int = Field(alias='currency') 


    @classmethod
    @model_validator(mode='before')
    def check_parameters(cls, values: dict) -> dict:
        if not values['price']:
            raise ValueError('The price is a required parameter')
        if not values['goods_name']:
            raise ValueError('The goods_name is a required parameter')
    