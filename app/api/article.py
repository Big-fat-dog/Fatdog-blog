#文章路由
from fastapi import APIRouter
router = APIRouter(
    prefix="/article",
    tags=["article"],
    responses={404: {"description": "Not found"}}
)

#获取文章信息
