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

def scale_input():
    pass

def scale_output():
    pass