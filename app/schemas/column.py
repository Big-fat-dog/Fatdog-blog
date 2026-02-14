from pydantic import BaseModel, ConfigDict


#请求模型
class ColumnGet(BaseModel):
    id:int
#响应模型
class ColumnResponse(BaseModel):
    id:int
    name:str
    order:int
    slug:str
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )
