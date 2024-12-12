import pendulum
from database.initial import db
from database.models import Goods
from pydantic_core import ValidationError
from starlette.responses import JSONResponse, Response
from api.filters.projects_filters import GoodsFilter
from api.initial import api_router
from fastapi_filter import FilterDepends
from api.api_tools.tools_data_conversion import data_conversion
from api.models.requests_models import RequestGoodsByIdModel, RequestAddGoodsModel, RequestUpdateGoodsModel
from api.models.response_models import GoodsResponceModel, GoodsByIdResponceModel, GoodsAddResponceModel, GoodsUpdateResponceModel



@api_router.get('/products', response_model=GoodsResponceModel, status_code=200)
async def get_products(product_filter: GoodsFilter=FilterDepends(GoodsFilter)) -> dict:
    currency = product_filter.currency
    goods = await db.get_goods_filter(product_filter)
    if goods:
        goods = {"data": [await data_conversion(i.get_data(), valute=currency) for i in goods]}
    else:
        goods = {"data": []}
    return JSONResponse(content=goods, status_code=200)


@api_router.get('/products/', response_model=GoodsByIdResponceModel, status_code=200)
async def get_products_by_id(id: int, currency: str) -> dict:
    try:
        data = RequestGoodsByIdModel(id=id, currency=currency)
    except ValidationError as e:
        return JSONResponse({"data": {'error': str(e)}}, status_code=400)
    result = await db.get_row(Goods, id=id)
    if result:
        response = {"data": await data_conversion(result.get_data(), valute=data.currency)}
    else:
        response = {"data": {}}
    return JSONResponse(content=response, status_code=200)


@api_router.post('/products', response_model= GoodsAddResponceModel, status_code=201)
async def add_product(product: RequestAddGoodsModel) -> dict:
    new_row = await db.add_row(Goods, goods_name=product.name, 
                              category=product.category, description=product.description, price=product.price,
                              currency=product.currency, date_of_adding=pendulum.today(),
                              date_of_updating=pendulum.today())
    result = await db.get_row(Goods, id=new_row.id)
    response = {"data": result.get_data()}
    return JSONResponse(content=response, status_code=201)


@api_router.put('/products/', response_model=GoodsUpdateResponceModel, status_code=200)
async def update_product(id: int, product: RequestUpdateGoodsModel) -> dict:
    row_exists = await db.get_row(Goods, id=id)
    if row_exists:
        await db.update_row(Goods, id=id, goods_name=product.name,
                            category=product.category, description=product.description, 
                            price=product.price, currency=product.currency,
                            date_of_updating=pendulum.today())
        updated_row = await db.get_row(Goods, id=id)
        response = {"data": updated_row.get_data()}
        return JSONResponse(content=response, status_code=200)
    else:
        return JSONResponse({"data": {'error': 'Product not found'}}, status_code=204)


@api_router.delete('/products/', status_code=204)
async def delete_product(id: int):
    result = await db.delete_row(Goods, id=id)
    return Response(status_code=204)
    