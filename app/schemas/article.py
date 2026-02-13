from pydantic import BaseModel,Field,ConfigDict
from typing import Optional,Annotated
from datetime import datetime
#请求模型！！
class Articlecreate(BaseModel):
    #创建文章
    title:Annotated[str,Field(min_length=1,max_length=255)]
    category_id:int
    tags:Annotated[str,Field(max_length=500)]
    md:Annotated[str,Field(min_length=1)]
    image:Annotated[str,Field(max_length=500)]

class Articleupdate(BaseModel):
    #更新文章
    title: Annotated[Optional[str], Field(min_length=1, max_length=255)]=None
    category_id: Optional[int]=None
    tags: Annotated[Optional[str], Field(max_length=500)]=None
    md: Annotated[Optional[str], Field(min_length=1)]=None
    image: Annotated[Optional[str], Field(max_length=500)]=None

#响应模型!!!
class Articleresponse(BaseModel):
    #文章响应模型
    id: int
    title: str
    author: str
    category_id: int
    category_name: str  # ← 从关联的 Category 拿 name（不是只返回 id）
    tags: str
    md_html: str  # ← 前端直接渲染这个！
    published_time: datetime
    updated_time: datetime
    image: str
    model_config=ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )
class ArticleSummary(BaseModel):
    #文章请求列表
    id: int
    title: str
    author: str
    category_name: str
    tags: str
    published_time: datetime
    image: str  # 封面图用于列表展示
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )