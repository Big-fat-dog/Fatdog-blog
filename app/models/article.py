from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from base import Base
from sqlalchemy import Integer,String,DateTime,Text,ForeignKey
class Article(Base):
    __tablename__ = 'articles'
    id:Mapped[int] = mapped_column(Integer,primary_key=True,nullable=False,unique=True,index=True,autoincrement=True)
    author:Mapped[str] = mapped_column(String(50),nullable=True,default="大胖狗")
    category_id:Mapped[int] = mapped_column(Integer,ForeignKey("categories.id"),nullable=False)
    title:Mapped[str] = mapped_column(String(225),index=True)
    tags:Mapped[str] = mapped_column(String(500),nullable=False)
    md_html:Mapped[str] = mapped_column(Text, nullable=False)
    md:Mapped[str] = mapped_column(Text, nullable=False)
    published_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.now,nullable=False)
    updated_at:Mapped[datetime] = mapped_column(DateTime,onupdate=datetime.now,nullable=False)
    image:Mapped[str] = mapped_column(Text, nullable=False)
    #关系模型
    category:Mapped["Category"]=relationship("Category",back_populates="articles")
    comments:Mapped[list["Comment"]]=relationship("Comment",back_populates="article",cascade="all, delete-orphan",order_by="Comment.created_at")
    def __repr__(self):
        return f"Atticle<id={self.id},title={self.title},category_id={self.category_id}"