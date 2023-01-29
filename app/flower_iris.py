from pydantic import BaseModel, Field
from typing import Optional

class FlowerIrisRequestData(BaseModel):
    FlowerID: str = Field(
        title="Unique flower id", max_length=4
    )
    SepalLength: float = Field(ge=0.0)
    SepalWidth: float = Field(ge=0.0)
    PetalLength: float = Field(ge=0.0)
    PetalWidth: float = Field(ge=0.0)

class GetFlowerIrisClassRequest(BaseModel):
    FlowerIrisRequestData: FlowerIrisRequestData

class FlowerIrisResponseData(BaseModel):
    FlowerID: str
    ReturnCode: int
    IrisClass: str