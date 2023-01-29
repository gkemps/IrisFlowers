from pydantic import BaseModel

class FlowerIrisRequestData(BaseModel):
    FlowerID: str
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