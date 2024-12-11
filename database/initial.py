from database.controller import BaseInterface
from database.database import DATABASE_URL


db = BaseInterface(DATABASE_URL)