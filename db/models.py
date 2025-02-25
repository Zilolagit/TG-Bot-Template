from sqlalchemy import select, Text
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from db import Base, db
from db.utils import CreatedModel


class Category(CreatedModel):
    __tablename__ = "categories"
    name: Mapped[str]


class Movie(CreatedModel):
    movie_title: Mapped[str]


class Product(CreatedModel):
    name : Mapped[str] = mapped_column(Text)

    @classmethod
    async def get_by_name(cls, name):
        query = select(cls).where(cls.name.icontains(name))
        objects = await db.execute(query)
        result = []
        for i in objects.all():
            result.append(i[0])
        return result

    def __repr__(self):
        return f"Product(id={self.id},name={self.name})"

metadata = Base.metadata