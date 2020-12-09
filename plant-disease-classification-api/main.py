#!/usr/bin/env python

from fastapi import FastAPI
from .models import ImageItem


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/classify")
def read_item(image: ImageItem):
    return {"data": image.data}
