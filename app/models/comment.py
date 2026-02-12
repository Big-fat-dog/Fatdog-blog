from base import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from typing import Optional
from datetime import datetime
from sqlalchemy import Integer,ForeignKey,String,Text,DateTime
class Comment(Base):
    __tablename__ = "comments"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True,index=True)
    user_id:Mapped[int]=mapped_column(Integer,ForeignKey("users.id"),index=True,nullable=False)
    content:Mapped[str] = mapped_column(Text, nullable=False)
    create_time:Mapped[datetime] = mapped_column(DateTime,nullable=False,default=datetime.now)
    status:Mapped[str] = mapped_column(String(50),default="pending",nullable=False)
    article_id:Mapped[int] = mapped_column(Integer,ForeignKey('articles.id'),nullable=False)
    parent_id:Mapped[Optional[int]] = mapped_column(Integer,ForeignKey('comments.id'),nullable=True)
    views_count:Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    # 深层设计优化查询
    depth:Mapped[int] = mapped_column(Integer,default=0)#0,1,2,3表示评论深度
    path: Mapped[str] = mapped_column(String(500), index=True,nullable=True)
    #关系字段
    article:Mapped["Article"]=relationship("Article",back_populates="comments")
    parent:Mapped["Comment"]=relationship("Comment",remote_side=[id],back_populates="replies",foreign_keys=[parent_id],post_update=True)
    replies:Mapped[list["Comment"]]=relationship("Comment",back_populates="parent",cascade="all, delete")
    user:Mapped["User"]=relationship("User",back_populates="comments")
    def __repr__(self):
        return f"Comment<id={self.id} user_id={self.user_id} status={self.status} path={self.path}>"