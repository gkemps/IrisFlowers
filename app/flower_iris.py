from pydantic import BaseModel, Field
from typing import Optional

class FlowerIrisRequestData(BaseModel):
    FlowerID: str = Field(
        title="Unique flower id", max_length=4
    )
    SepalLength: float
    SepalWidth: float
    PetalLength: float
    PetalWidth: float

class GetFlowerIrisClassRequest(BaseModel):
    FlowerIrisRequestData: FlowerIrisRequestData

class FlowerIrisResponseData(BaseModel):
    FlowerID: str
    ReturnCode: int
    IrisClass: str