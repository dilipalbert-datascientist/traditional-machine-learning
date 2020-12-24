import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

from json_config_expander import expand_configs


CLASSIFIER_MAPPINGS = {
    "random_forest": RandomForestClassifier,
    "logistic_regression": LogisticRegression,
    "": KNeighborsClassifier,
    "": SVC
    "": GaussianNB
    "xgboost": XGBClassifier
}


models = [
          ('RF', RandomForestClassifier()),
          ('LogReg', LogisticRegression())
          ('KNN', KNeighborsClassifier()),
          ('SVM', SVC()), 
          ('GNB', GaussianNB()),
          ('XGB', XGBClassifier())
        ]


BASE_CONFIG = {"classifier*": [
   {
    "name": "random_forest",
    "parameters": {"max_depth*": [3, 5],
                   "n_estimators*": [50, 100, 200]}
   },
   {
    "name": "logistic_regression",
    "parameters": {"max_iter*": [10, 100, 1000],
                   "C*": [0.1, 0.5, 1]}
   },
   {
    "name": "xgboost",
    "parameters": {"max_depth*": [3, 4, 5],
                   "n_estimators*": [50, 100, 200],
                   "learning_rate*": [0.01, 0.05, 0.1]}
   }]
}