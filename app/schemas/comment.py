from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional,Annotated

#请求模型
class CommentCreate(BaseModel):
    #创建评论
    article_id: Annotated[int, Field(alias="articleid")]
    parent_id:Annotated[int,Field(alias="parentid",default=None)]
    content:Annotated[str,Field(min_length=1,max_length=2000)]


class CommentUpdate(BaseModel):
    #更新评论（仅作者可操作)
    content:Annotated[str,Field(min_length=1,max_length=2000)]

#响应模型
class CommentBase(BaseModel):
    #基础评论
    id:int
    content:str
    created_at:datetime
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )
class UserSummary(BaseModel):
    #用户摘要
    id:int
    username:str
    avatar:Optional[str]=None
class CommentResponse(CommentBase):
    user: UserSummary  # ← 关联用户信息
    parent_user:Optional[UserSummary] = None
    reply_count:int=0
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )

class CommentWithReplies(CommentResponse):
    """用于“展开回复”时返回"""
    replies: List['CommentResponse'] = []  # ← 只嵌套一层！
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )

class CommentAdmin(CommentResponse):
    #用于后台管理
    status: str  # "pending", "approved", "rejected"
    article_id: int
    parent_id: Annotated[int,Field(alias="parentId",default=None)]
    views_count: int
    root_id: Optional[int]

#用于确保模型已经生成！
CommentWithReplies.model_rebuild()