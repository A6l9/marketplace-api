import uvicorn 
from api.routes import get_products
from preload import *


if __name__ == "__main__":
    uvicorn.run(root_app, host='127.0.01', port=8080)
