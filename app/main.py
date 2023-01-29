import joblib
from fastapi import FastAPI
from flower_iris import GetFlowerIrisClassRequest
from flower_iris import FlowerIrisResponseData

# create api
app = FastAPI()

# loading pipple model
pkl_filename = "model/pipple_model.pkl"
with open(pkl_filename, 'rb') as file:
 model = joblib.load(file)

# create post /GetFlowerIrisClass method
@app.post('/GetFlowerIrisClass')
def predict_species(data: GetFlowerIrisClassRequest):
    prediction = model.predict([[
        data.FlowerIrisRequestData.SepalLength,
        data.FlowerIrisRequestData.SepalWidth,
        data.FlowerIrisRequestData.PetalLength,
        data.FlowerIrisRequestData.PetalWidth
        ]])

    irisClass = ""
    if prediction[0] == 0: 
        irisClass = "Setosa"
    if prediction[0] == 1:
        irisClass = "Versicolor"
    if prediction[0] == 2:
        irisClass = "Virginica"          

    responseData = FlowerIrisResponseData(
        FlowerID=data.FlowerIrisRequestData.FlowerID,
        ReturnCode=0,
        IrisClass=irisClass
    )
      
    return {
        'FlowerIrisResponseData': responseData.dict(),
    }
