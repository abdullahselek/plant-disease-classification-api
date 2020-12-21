#!/usr/bin/env python

from fastapi import FastAPI
from .models import ImageItem, MLModel


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("loadModel")
def load_model(model: MLModel):
    return {"path": model.path, "name": model.name}


@app.post("/classify")
def classify(image: ImageItem):
    return {"data": image.data}
