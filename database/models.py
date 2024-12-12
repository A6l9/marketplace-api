from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base
from sqlalchemy import Integer, String, Float, Date


class Goods(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    goods_name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    category: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    currency: Mapped[str] = mapped_column(String)
    date_of_adding: Mapped[Date] = mapped_column(Date)
    date_of_updating: Mapped[Date] = mapped_column(Date)
    

    def __str__(self):
        return (
            f"""
        id: {self.id}
        goods_name: {self.goods_name}
        description: {self.description}
        category: {self.category}
        price: {self.price}
        currency: {self.currency}
        date_of_adding: {self.date_of_adding}
        date_of_updating: {self.date_of_updating}
        """
        )

    def get_data(self):
        return {
            'id': self.id,
            'goods_name': self.goods_name.title(),
            'description': self.description.title(),
            'category': self.category.title(),
            'price': self.price,
            'currency': self.currency,
            'date_of_adding': str(self.date_of_adding),
            'date_of_updating': str(self.date_of_updating)
        }