#这是文章板块的分类
from sqlalchemy.orm import Mapped,mapped_column,relationship

from base import Base
from sqlalchemy import Integer,String

class Category(Base):
    __tablename__ = 'categories'
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True,comment="分类id",index=True)
    name:Mapped[str]=mapped_column(String(50),nullable=False,unique=True,comment="板块名称",index=True)
    order:Mapped[int]=mapped_column(Integer,nullable=False,comment="排序")

    article:Mapped[list["Article"]]=relationship("Article",back_populates="category",cascade="all, delete-orphan",order_by="Article.published_time")
    def __repr__(self):
        return f"<Category id={self.id} name={self.name} order={self.order}>"