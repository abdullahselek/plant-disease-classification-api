#!/usr/bin/env python

import pytest
import asyncio
import base64
import json

from httpx import AsyncClient
from plant_disease_classification_api.main import app


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


@pytest.mark.asyncio
async def test_classify():
    with open("testdata/916fef78f494c6132246b40eac15f30e.jpg", "rb") as f:
        data = f.read()
        image_data = base64.b64encode(data).decode("utf-8")
    payload = {"modelName": "model_1.pt", "data": image_data}
    json_payload = json.dumps(payload)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/classify", data=json_payload)
    assert response.status_code == 200
    assert response.json() == {"result": "c_35"}


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_classify())
    loop.close()
