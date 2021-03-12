"""MLOps Library"""

import numpy as np
import pandas as pd
import joblib

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
    

def scale_input():
    pass

def scale_output():
    pass