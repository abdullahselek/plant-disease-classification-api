#!/usr/bin/env python

import os
import base64

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from plant_disease_classification_api.models import ClassficationRequestItem
from plant_disease_classification_api.ml.plant_disease_classifier import (
    PlantDiseaseClassifier,
)


app = FastAPI()


@app.get("/")
def read_root():
    html_content = """
    <html>
        <head>
            <title>Plant Disease Classification API</title>
        </head>
        <body>
            <h1>Welcome to Plant Disease Classification API</h1>
            <h2><a href="/docs">Documentation</a></h2>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/classify")
async def classify(requestItem: ClassficationRequestItem):
    if len(requestItem.modelName) == 0:
        return {"error": "Please provide name of model you want to use."}
    if len(requestItem.data) == 0:
        return {"error": "Please provide Base64 encoded image data."}

    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir_path, "models", requestItem.modelName)
    plant_disease_classifier = PlantDiseaseClassifier(model_path=path)
    image_data = base64.b64decode(requestItem.data)
    result = plant_disease_classifier.classify(image_data=image_data)
    return {"result": result}
