"""MLOps Library"""

import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

def load_model():
    """Grabs model from disk"""

    clf = joblib.load("model.joblib")
    return clf

def data():
    df = pd.read_csv("htwtmlb.csv")
    return df

def format_input(x):
    """Takes int and converts to numpy array"""
    
    val = np.array(x)
    feature = val.reshape(-1,1)
    return feature
    

def scale_input(val):
    """Scales input to training feature values""" 
    
    
    df = data()
    features = df["Weight"].values
    features = features.reshape(-1, 1)
    input_scaler = StandardScaler().fit(features)
    scaled_input = input_scaler.transform(val)
    return scaled_input

def scale_target(target):
    """Scales Target 'y' Value"""
    
    df = data()
    y = df['Height'].values #Target
    y = y.reshape(-1, 1)    #Reshape
    scaler = StandardScaler()
    y_scaler = scaler.fit(y)
    scaled_target = y_scaler.inverse_transform(target)
    return scaled_target

def height_human(float_inches):
    """Takes float inches and converts to human height in ft/inches"""
    
    feet = int(round(float_inches/12,2))    #round down
    inches_left = round(float_inches - feet*12)
    result = f"{feet} foot, {inches_left} inches"
    return result
    
def human_readable_payload(predict_value):
    """Takes numpy array and returns back human readable dictionary"""
    
    height_inches = float(np.round(predict_value, 2))
    result = {
        "height_inches": height_inches,
        "height_human_readable": height_human(height_inches)
    }
    return result

def predict(weight):
    """Takes weight and predicts height"""

    clf = load_model()  #loadmodel
    np_array_weight = format_input(weight)
    scaled_input_result = scale_input(np_array_weight) #scale feature input
    scaled_height_prediction = clf.predict(scaled_input_result) #scaled prediction
    height_predict = scale_target(scaled_height_prediction)
    payload = human_readable_payload(height_predict)
    predict_log_data = {"weight":weight, 
        "scaled_input_result": scaled_input_result,
        "scaled_height_prediction": scaled_height_prediction,
        "height_predict": height_predict,
        "human_readable_payload": payload
    }
    print(f"Prediction: {predict_log_data}")
    return payload

