from datetime import datetime
from sqlalchemy.orm import mapped_column,Mapped
from base import Base
from sqlalchemy import Integer,String,DateTime,Text

class Article(Base):
    __tablename__ = 'articles'
    id:Mapped[int] = mapped_column(Integer,primary_key=True,nullable=False,unique=True,index=True,autoincrement=True)
    author:Mapped[str] = mapped_column(String(50),nullable=False)
    category_id:Mapped[int] = mapped_column(Integer,ForeignKey='category.id',nullable=False)
    title:Mapped[str] = mapped_column(String(225),index=True)
    tags:Mapped[str] = mapped_column(String(500),nullable=False)
    md_html:Mapped[str] = mapped_column(Text, nullable=False)
    md:Mapped[str] = mapped_column(Text, nullable=False)
    published:Mapped[datetime] = mapped_column(DateTime,default=datetime.now,nullable=False)
    updated:Mapped[datetime] = mapped_column(DateTime,onupdate=datetime.now,nullable=False)
    image:Mapped[str] = mapped_column(Text, nullable=False)
    def __repr__(self):
        return (f"Atticle<id={self.id},title={self.title},category_id={self.category_id}"
                f"tag={self.tags},md_html={self.md_html},published={self.published},updated={self.updated},image={self.image}")