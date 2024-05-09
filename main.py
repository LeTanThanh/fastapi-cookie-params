from fastapi import FastAPI
from fastapi import Response
from fastapi import Cookie
from uuid import uuid1

from typing import Annotated

app = FastAPI()

@app.post("/cookie/example")
async def create_example_cookie(response: Response):
  response.set_cookie(key = "example", value = uuid1())
  return {"success": True}

@app.get("/cookie/example")
async def read_example_cookie(example: Annotated[str | None, Cookie()] = None):
  return {"example": example}
