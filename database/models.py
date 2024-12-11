from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base
from sqlalchemy import Integer, String, Float, Date


class Goods(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    goods_name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=True)
    currency: Mapped[str] = mapped_column(String, nullable=True)
    date_of_adding: Mapped[Date] = mapped_column(Date, nullable=True)
    

    def __str__(self):
        return (
            f"""
        id: {self.id}
        goods_name: {self.goods_name}
        price: {self.price}
        currency: {self.currency}
        date_of_adding: {self.date_of_adding}
        """
        )

    def get_data(self):
        return {
            'id': self.id,
            'goods_name': self.goods_name,
            'price': self.price,
            'currency': self.currency,
            'date_of_adding': self.date_of_adding
        }