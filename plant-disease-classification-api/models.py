#!/usr/bin/env python

from pydantic import BaseModel


class ImageItem(BaseModel):
    """Request entity of image classification endpoint.
       `data` is a Base64 encoded image string."""

    data: str
