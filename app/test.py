import joblib
import json
from flower_iris import GetFlowerIrisClassRequest
from flower_iris import FlowerIrisResponseData

pkl_filename = "model/pipple_model.pkl"
with open(pkl_filename, 'rb') as file:
 model = joblib.load(file)

request_filename = "model/request.json"
with open(request_filename, 'rb') as file:
 data = json.load(file)
print(data)
flowerIrisRequest = GetFlowerIrisClassRequest(**data)
print(flowerIrisRequest)

responseData = FlowerIrisResponseData(FlowerID="00001", ReturnCode="0", IrisClass="jadieja")
result = {
    'FlowerIrisResponseData': responseData.dict()
}
print(result)

prediction = model.predict([[7, 3.2, 4.7, 1.4]])
print(prediction[0])