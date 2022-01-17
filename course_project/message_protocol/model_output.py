from typing import List
from pydantic import BaseModel
from simplestr import gen_str_repr


@gen_str_repr
class ModelOutput(BaseModel):
    predictions: List[int]

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, predictions: List[int]) -> None:
        super().__init__(predictions=predictions)
