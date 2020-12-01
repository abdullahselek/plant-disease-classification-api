#!/usr/bin/env python

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class ImageItem(BaseModel):
    data: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/classify")
def read_item(image: ImageItem):
    return {"data": image.data}
