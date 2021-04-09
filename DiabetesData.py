
from pydantic import BaseModel

class DiabetesData(BaseModel):
    Pregnancies: float  
    PlasmaGlucose: float 
    DiastolicBloodPressure: float 
    TricepsThickness: float
    SerumInsulin: float
    BMI:float
    DiabetesPedigree:float
    Age:float
    

