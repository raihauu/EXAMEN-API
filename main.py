from typing import List
from fastapi import FastAPI
from fastapi.exception_handlers import http_exception_handler
from pip._internal.utils import datetime
from pydantic import BaseModel
from starlette import status
from starlette.requests import Request
from starlette.responses import Response, JSONResponse, HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app=FastAPI()
#Q1
@app.get("/ping")

def ping():
    return Response(content="pong", media_type="text/plain", status_code=200)

#Q2
@app.get("/home", response_class=HTMLResponse)
def home():
    html_content = "<h1>Welcome home!</h1>"
    return HTMLResponse(content=html_content, status_code=200)

#Q3
@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return HTMLResponse(content="<h1>404 NOT FOUND</h1>", status_code=404)
    return await http_exception_handler(request, exc)

#Q4
posts_db = []


class post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

@app.post("/POST")


def add_post(posts: List[post]):
    for student in posts:
        posts_db.append(student)


    return JSONResponse(content=[s.dict() for s in posts_db], status_code=201)