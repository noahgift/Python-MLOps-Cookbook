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

def scale_output(val):
    pass