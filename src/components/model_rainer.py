# #model trainer class
# import os
# import sys
# from dataclasses import dataclass

# from sklearn.metrics import r2_score
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.model_selection import GridSearchCV

# from src.exception import CustomException
# from src.logger import logging
# import pandas as pd

# from src.components.data_ingestion import DataIngestion
# from src.components.data_transformation import DataTransformation
# from src.components.model_trainer import ModelTrainer
# from src.components.model_evaluation import ModelEvaluation
# from src.components.data_ingestion import DataIngestion
# from src.components.data_transformation import DataTransformation
# from src.components.model_trainer import ModelTrainer
# from src.components.model_evaluation import ModelEvaluation


# @dataclass
# class ModelTrainerConfig:
#     trained_model_file_path = os.path.join("artifacts", "model.pkl")

# class ModelTrainer:
#     def __init__(self):
#         self.model_trainer_config = ModelTrainerConfig()

#     def initiate_model_trainer(self):
#         try:
#             train_array = pd.read_csv('train.csv')
#             test_array = pd.read_csv('test.csv')
#             target_column_name = 'math_score'
#             input_feature_train_df = train_array.drop(columns=[target_column_name], axis=1)
#             target_feature_train_df = train_array[target_column_name]
#             input_feature_test_df = test_array.drop(columns=[target_column_name], axis=1)
#             target_feature_test_df = test_array[target_column_name]
#             model = RandomForestRegressor()
#             model.fit(input_feature_train_df, target_feature_train_df)
#             y_train_pred = model.predict(input_feature_train_df)    