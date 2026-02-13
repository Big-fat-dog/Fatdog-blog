from pydantic import BaseModel, Field, ConfigDict
from typing import Optional,Annotated

#请求模型
class Categorycreate(BaseModel):
    #创建分类
    name:Annotated[str,Field(max_length=50,min_length=1)]
    order:Annotated[int,Field(ge=0)]

class CategoryUpdate(BaseModel):
    """更新分类（字段可选）"""
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    order: Optional[int] = Field(None, ge=0)

#响应模型
class CategoryResponse(BaseModel):
    """分类详情（返回给前端）"""
    id: int
    name: str
    order: int
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )