from fastapi import FastAPI
from pydantic.main import BaseModel

app = FastAPI()


class Request(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/api/sentry/webhook")
async def root(request: Request):
    return request
