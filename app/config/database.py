from sqlalchemy.ext.asyncio import AsyncSession,async_sessionmaker,create_async_engine
#开发环境下
#数据库url
ASYNC_DATABASE_URL = "mysql+aiomysql://root:123456@localhost:3306/Fatdogblog/charset=utf8"
#创建异步引擎
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True,
    pool_size=10,
    max_overflow = 20
)
Asyncsessionloacl = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)
async def get_db():
    async with Asyncsessionloacl() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()