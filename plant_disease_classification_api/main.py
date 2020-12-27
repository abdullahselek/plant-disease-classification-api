#!/usr/bin/env python

import os
import base64

from fastapi import FastAPI
from plant_disease_classification_api.models import ClassficationRequestItem
from plant_disease_classification_api.ml.plant_disease_classifier import PlantDiseaseClassifier


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/classify")
async def classify(requestItem: ClassficationRequestItem):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir_path, requestItem.modelPath)
    plant_disease_classifier = PlantDiseaseClassifier(model_path=path)
    image_data = base64.b64decode(requestItem.data)
    result = plant_disease_classifier.classify(image_data=image_data)
    return {"result": result}
