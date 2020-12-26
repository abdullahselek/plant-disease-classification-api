#!/usr/bin/env python

from pydantic import BaseModel


class ImageItem(BaseModel):
    """Request entity of image classification endpoint.
    `data` is a Base64 encoded image string."""

    data: str


class MLModel(BaseModel):
    """Request entity of ML model which is used for classification.
    `path` is the path for model which is used for classification.
    `name` is the name for model which is used for classification."""

    path: str
    name: str
