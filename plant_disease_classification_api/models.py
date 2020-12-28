#!/usr/bin/env python

from pydantic import BaseModel


class ClassficationRequestItem(BaseModel):
    """Request entity of classifcation item which has model path, name and image data.
    `modelName` is the name for model which is used for classification.
    `data` is a Base64 encoded image string."""

    modelName: str
    data: str
