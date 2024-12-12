from pydantic import Field, BaseModel
from datetime import date
import json


class GoodsResponceModel(BaseModel):
    class Item(BaseModel):
        id: int = Field(alias='id')
        goods_name: str = Field(alias='goods_name')
        description: str = Field(alias='description')
        category: str = Field(alias='category')
        price: float = Field(alias='price')
        currency: str = Field(alias='currency')
        date_of_adding: str = Field(alias='date_of_adding')
        date_of_updating: str = Field(alias='date_of_updating')

    data: list[Item] | list[None]

class GoodsByIdResponceModel(BaseModel):
    class Item(BaseModel):
        id: int = Field(alias='id')
        goods_name: str = Field(alias='goods_name')
        description: str = Field(alias='description')
        category: str = Field(alias='category')
        price: float = Field(alias='price')
        currency: str = Field(alias='currency')
        date_of_adding: str = Field(alias='date_of_adding')
        date_of_updating: str = Field(alias='date_of_updating')

    class Error(BaseModel):
        error: str

    data: Item | dict | Error


class GoodsAddResponceModel(BaseModel):
    class Item(BaseModel):
        id: int = Field(alias='id')
        goods_name: str = Field(alias='goods_name')
        description: str = Field(alias='description')
        category: str = Field(alias='category')
        price: float = Field(alias='price')
        currency: str = Field(alias='currency')
        date_of_adding: str = Field(alias='date_of_adding')
        date_of_updating: str = Field(alias='date_of_updating')

    data: Item


class GoodsUpdateResponceModel(BaseModel):
    class Item(BaseModel):
        id: int = Field(alias='id')
        goods_name: str = Field(alias='goods_name')
        description: str = Field(alias='description')
        category: str = Field(alias='category')
        price: float = Field(alias='price')
        currency: str = Field(alias='currency')
        date_of_adding: str = Field(alias='date_of_adding')
        date_of_updating: str = Field(alias='date_of_updating')
    
    class Error(BaseModel):
        error: str

    data: Item | Error


class GoodsDeleteResponceModel(BaseModel):

    class Error(BaseModel):
        error: str

    data: Error | None