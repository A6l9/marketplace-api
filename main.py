import uvicorn
from api.routes import (get_products, get_products_by_id, 
                       add_product, update_product, delete_product)
from preload import *


if __name__ == "__main__":
    uvicorn.run(app=root_app, host='0.0.0.0', port=5000)
