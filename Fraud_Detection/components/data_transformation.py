import pandas as pd
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import joblib
from Fraud_Detection.Constants.constants import *
from Fraud_Detection.Logger import logging


class DataTransformation:

    def __init__(self, data_transformation_config, train_path, test_path):
        self.data_transformation_config = data_transformation_config
        self.train_path = train_path
        self.test_path = test_path


    def data_tranformation(self):
        try:
            logging.info("Started Data Transformation")
            train_data = pd.read_csv(self.train_path)
            test_data = pd.read_csv(self.test_path)
            # Separate features and labels in training data
            X_train = train_data.drop(['Class'], axis=1)
            y_train = train_data['Class']
            # Separate features and labels in testing data
            X_test = test_data.drop(['Class'], axis=1)
            y_test = test_data['Class']
            # Handle imbalanced dataset in training data using SMOTE
            smote = SMOTE()
            X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
            # Scale the features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train_resampled)
            X_test_scaled = scaler.transform(X_test)

            root_dir = ROOT_DIR
            preprocessed_dir = self.data_transformation_config.preprocessing_dir
            data_transformation_file_name = self.data_transformation_config.preprocessed_object_file_name
            dir_path = os.path.join(root_dir, preprocessed_dir)
            os.makedirs(dir_path, exist_ok=True)
            path = os.path.join(dir_path, data_transformation_file_name)
            joblib.dump(scaler, path)
            logging.info("Data Transformation Completed")

            return path, X_train_scaled, y_train_resampled
        
        except Exception as e:
            logging.error("Error at Data Transformation ", e)



