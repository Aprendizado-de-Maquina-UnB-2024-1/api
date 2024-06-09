from fastapi import FastAPI, HTTPException
from predictionModel import PredictionModel
import pickle
import os

app = FastAPI()

# Load the model at startup
if os.path.exists('model.pkl'):
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
else:
    model = None


@app.get("/")
def read_root():
    return {"message": "Welcome to the ML model API"}

@app.post("/predict")
def get_prediction(predictionModel: PredictionModel):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    try:
        prediction_input = [[
            predictionModel.age,
            predictionModel.trtbps,
            predictionModel.chol,
            predictionModel.thalachh,
            predictionModel.oldpeak,
            int(predictionModel.sex_1),
            int(predictionModel.exng_1),
            int(predictionModel.caa_1),
            int(predictionModel.caa_2),
            int(predictionModel.caa_3),
            int(predictionModel.caa_4),
            int(predictionModel.cp_1),
            int(predictionModel.cp_2),
            int(predictionModel.cp_3),
            int(predictionModel.fbs_1),
            int(predictionModel.restecg_1),
            int(predictionModel.restecg_2),
            int(predictionModel.slp_1),
            int(predictionModel.slp_2),
            int(predictionModel.thall_1),
            int(predictionModel.thall_2),
            int(predictionModel.thall_3)
        ]]
        prediction = model.predict(prediction_input) 
        if(prediction[0] == [1]):
            return {"prediction": "Tem risco de sofrer ataque cardíaco"}
        return {"prediction": "Tem pouco risco de sofrer ataque cardíaco"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
