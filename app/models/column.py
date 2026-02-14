from base import Base
from sqlalchemy import Integer,String
from sqlalchemy.orm import Mapped,mapped_column

class Column(Base):
    __tablename__="columns"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True,index=True)
    name:Mapped[str] = mapped_column(String(50),nullable=False)
    order:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    slug:Mapped[str] = mapped_column(String(50),nullable=False,unique=True,index=True)

    def __repr__(self):
        return "<Column(name='%s',order='%s')>" % (self.name, self.order)