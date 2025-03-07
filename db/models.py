from sqlalchemy import select, Text, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from db import Base, db
from db.utils import CreatedModel

"""

    Diagram version in DrawSQL:

    => https://drawsql.app/teams/ixtiyorova-zilola/diagrams/exam-bot

"""


# Users

class User(CreatedModel):
    username: Mapped[str]

    def __repr__(self):
        return f"User(id={self.id},username={self.username})"


# Category
class Category(CreatedModel):
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"Category(id={self.id},name={self.name})"


# Menu
class Menu(CreatedModel):
    name: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str]
    desc: Mapped[str] = mapped_column(Text)
    category_id: Mapped[int] = ForeignKey("categories.id")

    def __repr__(self):
        return f"Menu(id={self.id},name={self.name})"

#
# class Category(CreatedModel):
#     __tablename__ = "categories"
#     name: Mapped[str]
#
#     def __repr__(self):
#         return f"Category(id={self.id},name={self.name})"
#

#
# class Movie(CreatedModel):
#     movie_title: Mapped[str]
#
#
# class Product(CreatedModel):
#     name : Mapped[str] = mapped_column(Text)
#
#     @classmethod
#     async def get_by_name(cls, name):
#         query = select(cls).where(cls.name.icontains(name))
#         objects = await db.execute(query)
#         result = []
#         for i in objects.all():
#             result.append(i[0])
#         return result
#
#     def __repr__(self):
#         return f"Product(id={self.id},name={self.name})"

metadata = Base.metadata