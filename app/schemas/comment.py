from datetime import datetime
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

class UserSummary(BaseModel):
    #用户摘要
    id:int
    username:str
    avatar:Optional[str]=None


class FlatCommentResponse(BaseModel):
    """扁平评论响应（B站风格）"""
    id: int
    content: str
    created_at: datetime

    # 发评论的人
    user: UserSummary

    # === 关系字段（核心！）===
    root_id: Optional[int]
    parent_id: Optional[int] = None  # 被回复的评论ID
    parent_user: Optional[UserSummary] = None  # 被回复的用户（用于显示“回复 @xxx”）

    # === 业务字段（前端需要）===
    is_main_floor: bool = False  # 是否主楼（parent_id is None）
    reply_count: int = 0  # 直接回复数（用于显示“X条回复”）

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )
class CommentAdmin(BaseModel):
    #用于后台管理
    status: str  # "pending", "approved", "rejected"
    article_id: int
    parent_id: Annotated[Optional[int],Field(alias="parentId",default=None)]
    views_count: int
    root_id: Optional[int]
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )
