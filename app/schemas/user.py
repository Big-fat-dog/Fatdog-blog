from datetime import datetime

from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional,Annotated
#请求模型
class UserCreate(BaseModel):
    #用于创建用户
    username:Annotated[str,Field(min_length=1,max_length=20)]
    password:Annotated[str,Field(min_length=8,max_length=25)]
    email:EmailStr
    avatar:Annotated[Optional[str],Field(max_length=250,default=None)]

#修改信息
class UserUpdate(BaseModel):
    username:Annotated[Optional[str],Field(min_length=1,max_length=20)]
    password:Annotated[Optional[str],Field(min_length=8,max_length=25)]
    avatar:Annotated[Optional[str],Field(max_length=250,default=None)]

#响应模型
class UserResponse(BaseModel):
    #返回用户信息
    id:int
    username: Annotated[str, Field(min_length=1, max_length=20)]
    avatar: Annotated[Optional[str], Field(max_length=250, default=None)]
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )

class UserAdmin(BaseModel):
    #管理用户
    id: int
    username: Annotated[str, Field(min_length=1, max_length=20)]
    avatar: Annotated[Optional[str], Field(max_length=250, default=None)]
    created_at:datetime
    is_admin: bool=False
    is_active: bool=True
    last_login: Optional[datetime]
    email: EmailStr
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )