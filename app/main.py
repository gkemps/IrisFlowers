import joblib
import logging
from fastapi import FastAPI
from flower_iris import GetFlowerIrisClassRequest
from flower_iris import FlowerIrisResponseData

# create api
app = FastAPI()

# loading pipple model
pkl_filename = "model/pipple_model.pkl"
with open(pkl_filename, 'rb') as file:
 model = joblib.load(file)

#logger
logger = logging.getLogger("uvicorn") 
logger.setLevel(logging.INFO)

# create post /GetFlowerIrisClass method
@app.post('/GetFlowerIrisClass')
def predict_species(data: GetFlowerIrisClassRequest):
    prediction = model.predict([[
        data.FlowerIrisRequestData.SepalLength,
        data.FlowerIrisRequestData.SepalWidth,
        data.FlowerIrisRequestData.PetalLength,
        data.FlowerIrisRequestData.PetalWidth
        ]])

    if prediction.size < 1 or prediction[0] < 0 or prediction[0] > 2:
        logger.error(
            "FlowerId: %s SepalLength: %.2f SepalWidth: %.2f PedalLength: %.2f PedalWidth: %.2f; Prediction: %s",
            data.FlowerIrisRequestData.FlowerID,
            data.FlowerIrisRequestData.SepalLength,
            data.FlowerIrisRequestData.SepalWidth,
            data.FlowerIrisRequestData.PetalLength,
            data.FlowerIrisRequestData.PetalWidth,
            prediction
        )  

        return {
            'FlowerIrisResponseData': {
                'FlowerID': data.FlowerIrisRequestData.FlowerID,
                'ReturnCode': 1,
                'ErrorMessage': 'something went wrong'
            },
        }

    irisClass = ""
    if prediction[0] == 0: 
        irisClass = "Setosa"
    if prediction[0] == 1:
        irisClass = "Versicolor"
    if prediction[0] == 2:
        irisClass = "Virginica"    

    logger.info(
        "FlowerId: %s SepalLength: %.2f SepalWidth: %.2f PedalLength: %.2f PedalWidth: %.2f; Prediction: %s = %s",
        data.FlowerIrisRequestData.FlowerID,
        data.FlowerIrisRequestData.SepalLength,
        data.FlowerIrisRequestData.SepalWidth,
        data.FlowerIrisRequestData.PetalLength,
        data.FlowerIrisRequestData.PetalWidth,
        prediction,
        irisClass
    )          

    responseData = FlowerIrisResponseData(
        FlowerID=data.FlowerIrisRequestData.FlowerID,
        ReturnCode=0,
        IrisClass=irisClass
    )
      
    return {
        'FlowerIrisResponseData': responseData.dict(),
    }
