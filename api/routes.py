from database.initial import db
from api.filters.projects_filters import GoodsFilter
from api.initial import api_router
from fastapi_filter import FilterDepends
from api.api_tools.tools_data_conversion import data_conversion
# from models.requests_models import RequestGoodsModel



@api_router.get('/products')
async def get_products(product_filter: GoodsFilter = FilterDepends(GoodsFilter)) -> list:
    await db.initial()
    goods = await db.get_goods_filter(product_filter)
    print(goods)
    if goods:
        goods = [await data_conversion(i.get_data(), valute=product_filter.currency) for i in goods]
    print(goods)
    return goods