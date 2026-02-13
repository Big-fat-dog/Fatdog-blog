from fastapi import HTTPException, status,Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
import logging
#处理参数校验失败，http请求失败，兜底失败！
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("Errors")

#创建全局异常处理器
async def register_exception_handler(app):
    #Pydantic校验错误
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request:Request,exc:RequestValidationError):
        logging.warning(f"参数校验失败！————url:{request.url},错误是{exc.errors()}")
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={
                "code":422,
                "msg":"参数校验失败",
                "detail":jsonable_encoder(exc.errors())
            }
        )

    #HTTP错误
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request:Request,exc:HTTPException):
        logging.warning(f"业务异常！url:{request.url},错误是{exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "code":exc.status_code,
                "msg":exc.detail,
                "detail":None
            }
        )

    #处理404
    @app.exception_handler(404)
    async def the_404_exception_handler(request:Request,exc):
        logging.info(f"访问的接口不存在！{request.url}")
        return JSONResponse(
            status_code=404,
            content={
                'code':404,
                "msg":"不存在的接口",
                "detail":None
            }
        )
    #处理405
    @app.exception_handler(405)
    async def the_405_exception_handler(request: Request,exc):
        return JSONResponse(
            status_code=405,
            content={
                'code': 405,
                "msg": "请求方法错误！",
                "detail": None
            }
        )
    #处理401
    @app.exception_handler(401)
    async def unauthorized_handler(request: Request, exc):
        return JSONResponse(
            status_code=401,
            content={"code": 401, "msg": "未授权", "detail": None}
        )

    #数据库异常捕获
    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_error_handler(request: Request,exc: SQLAlchemyError):
        logger.error(f"数据库错误 | URL: {request.url} | 错误: {repr(exc)}")#不要返回str（exc），会泄露表结构！
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "code": 500,
                "msg": "数据服务异常，请稍后再试",
                "detail": None
            }
        )

    #所有捕获异常
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request,exc: Exception):
        logging.critical(f"未处理异常|{request.url}|,错误{repr(exc)}",exc_info=True)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "code": 500,
                "msg":"服务器开小差了捏，喊主人来修一修",
                "detail": None
            }
        )