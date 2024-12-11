from pydantic import Field, ConfigDict
from database.models import Goods
from typing import Optional
from fastapi_filter.contrib.sqlalchemy import Filter



class GoodsFilter(Filter):
    
    goods_name__like: Optional[str] = Field(default=None)
    price__gte: Optional[float] = Field(default=None)
    price__lte: Optional[float] = Field(default=None)
    category__like: Optional[str] = Field(default=None)
    currency: Optional[str] = Field(default=None)

    model_config = ConfigDict(extra='ignore')

    class Constants(Filter.Constants):
        model = Goods
    