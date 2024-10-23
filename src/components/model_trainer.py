#model training
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from src.utils import save_object,evaluate_models
import sys
import numpy as np
import pandas as pd
import os

@dataclass
#model trainer config class to save the trained model
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")
#model trainer class to train the model
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Linear Regression": LinearRegression(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "Gradient Boosting": GradientBoostingRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)

            #To get best model score from dict
            best_model_score = max(sorted(model_report.values()))
            #To get best model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            #To get best model
            best_model = models[best_model_name]

            if best_model_score < 0.6:
               raise Exception("No best model found we need to improve our model")
            logging.info("Best model found on both training and testing dataset")

            print(f"Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}")
            print(f"--------------------------")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            #Predicting on test data
            predicted = best_model.predict(X_test)
            #R2 score on test data
            r2_square = r2_score(y_test, predicted)
            return r2_square
        except Exception as e:
            raise CustomException(e,sys)

        