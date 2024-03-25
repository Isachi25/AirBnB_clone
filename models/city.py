#!/usr/bin/python3

from models.base_model import BaseModel

class City(BaseModel):
    """City class that inherits from BaseModel."""
    state_id = ""  # it will be the State.id
    name = ""
