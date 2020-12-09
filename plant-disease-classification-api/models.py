#!/usr/bin/env python

from pydantic import BaseModel


class ImageItem(BaseModel):
    data: str
