from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, String, Boolean, DateTime
from base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = 'users'
    id:Mapped[int]=mapped_column(Integer,autoincrement=True,index=True,primary_key=True)
    username:Mapped[str] = mapped_column(String(50), nullable=False)
    password_hash:Mapped[str] = mapped_column(String(255), nullable=False)
    avatar:Mapped[str] = mapped_column(String(500), nullable=True,default="")
    created_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.now,nullable=False)
    is_admin:Mapped[bool]=mapped_column(Boolean,nullable=False,default=False)
    last_login:Mapped[Optional[datetime]] = mapped_column(DateTime,nullable=True)
    email:Mapped[str] = mapped_column(String(255), nullable=False,index=True)
    #关系
    comments:Mapped[list["Comment"]]=relationship("Comment",back_populates="user",cascade="all, delete")
    def __repr__(self):
        return f"<User username={self.username},id={self.id},admin={self.admin}>"