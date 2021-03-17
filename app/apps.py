from django.apps import AppConfig
import pandas as pd
from joblib import load
import os
from sklearn.ensemble import RandomForestClassifier


# class ModelConfig(AppConfig):
#     name = 'app'
#     #CLASSIFIER_FOLDER = Path("classifier")
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     CLASSIFIER_FOLDER = os.path.join(BASE_DIR, 'app/classifier/')
#     #CLASSIFIER_FILE = CLASSIFIER_FOLDER / 'loan_model.pkl'
#     CLASSIFIER_FILE = os.path.join(CLASSIFIER_FOLDER, 'loan_model.pkl')
#     classifier = pd.read_pickle(CLASSIFIER_FILE)
