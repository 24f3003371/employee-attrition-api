
from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("employee_attrition_model.pkl")


