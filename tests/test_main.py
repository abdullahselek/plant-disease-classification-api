#!/usr/bin/env python

import pytest
import asyncio
import base64
import json

from fastapi.testclient import TestClient
from httpx import AsyncClient
from plant_disease_classification_api.main import app


def test_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.content == """
    <html>
        <head>
            <title>Plant Disease Classification API</title>
        </head>
        <body>
            <h1>Welcome to Plant Disease Classification API</h1>
            <h2><a href="/docs">Documentation</a></h2>
        </body>
    </html>
    """.encode()


@pytest.mark.asyncio
async def test_classify_succeed():
    with open("testdata/916fef78f494c6132246b40eac15f30e.jpg", "rb") as f:
        data = f.read()
        image_data = base64.b64encode(data).decode("utf-8")
    payload = {"modelName": "model_1.pt", "data": image_data}
    json_payload = json.dumps(payload)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/classify", data=json_payload)
    assert response.status_code == 200
    assert response.json() == {"result": "c_35"}


@pytest.mark.asyncio
async def test_classify_fails_with_wrong_model_name():
    with open("testdata/916fef78f494c6132246b40eac15f30e.jpg", "rb") as f:
        data = f.read()
        image_data = base64.b64encode(data).decode("utf-8")
    payload = {"modelName": "model.pt", "data": image_data}
    json_payload = json.dumps(payload)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/classify", data=json_payload)
    assert response.status_code == 200
    assert response.json() == {"error": "ML Model not found!"}


@pytest.mark.asyncio
async def test_classify_fails_with_missing_model_name():
    with open("testdata/916fef78f494c6132246b40eac15f30e.jpg", "rb") as f:
        data = f.read()
        image_data = base64.b64encode(data).decode("utf-8")
    payload = {"modelName": "", "data": image_data}
    json_payload = json.dumps(payload)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/classify", data=json_payload)
    assert response.status_code == 200
    assert response.json() == {"error": "Please provide name of model you want to use."}


@pytest.mark.asyncio
async def test_classify_fails_with_missing_data():
    payload = {"modelName": "model_1.pt", "data": ""}
    json_payload = json.dumps(payload)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/classify", data=json_payload)
    assert response.status_code == 200
    assert response.json() == {"error": "Please provide Base64 encoded image data."}


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_classify())
    loop.close()
