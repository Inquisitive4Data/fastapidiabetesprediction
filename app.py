

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from DiabetesData import DiabetesData
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("diabetes.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, Check Ur diabetes'}



# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_diabetes(data:DiabetesData):
    data = data.dict()
    Pregnancies=data['Pregnancies']
    PlasmaGlucose=data['PlasmaGlucose']
    DiastolicBloodPressure=data['DiastolicBloodPressure']
    TricepsThickness=data['TricepsThickness']
    SerumInsulin=data['SerumInsulin']
    BMI=data['BMI']
    DiabetesPedigree=data['DiabetesPedigree']
    Age=data['Age']
    

   
    prediction = classifier.predict([[Pregnancies,PlasmaGlucose,DiastolicBloodPressure,TricepsThickness,SerumInsulin,BMI,DiabetesPedigree,Age]])
    if(prediction[0]==0):
        prediction="Not a Diabetic"
    else:
        prediction="You are a diabetic"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload