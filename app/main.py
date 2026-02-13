from fastapi import FastAPI
from core.exceptions import register_exception_handler
app = FastAPI()

register_exception_handler(app)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
