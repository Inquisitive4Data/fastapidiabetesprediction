import pandas as pd
import numpy as np
import pickle
df = pd.read_csv('diabetes.csv')
features = ['Pregnancies','PlasmaGlucose','DiastolicBloodPressure','TricepsThickness','SerumInsulin','BMI','DiabetesPedigree','Age']
label = 'Diabetic'
X, y = df[features].values, df[label].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
from sklearn.svm import SVC
sv = SVC(kernel='linear').fit(X_train,y_train)
pickle.dump(sv, open('diabetes.pkl', 'wb'))