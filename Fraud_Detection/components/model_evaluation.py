import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from Fraud_Detection.components.data_ingestion import DataIngestion
from Fraud_Detection.components.model_trainer import ModelTrainer
from Fraud_Detection.components.data_transformation import DataTransformation
from Fraud_Detection.Logger import logging


class ModelEvaluation:

    def __init__(self, data_ingestion_config, data_transformation_config, model_trainer_config):
        self.data_ingestion_config = data_ingestion_config
        self.data_transformation_config = data_transformation_config
        self.model_trainer_config = model_trainer_config

        self.data_ingestion = DataIngestion(self.data_ingestion_config)
        self.data_transform = DataTransformation(self.data_ingestion_config, self.data_transformation_config)
        self.model_train = ModelTrainer(self.data_ingestion_config, self.data_transformation_config, self.model_trainer_config)

        

        self.train_path, self.test_path = self.data_ingestion.split_data_train_test()
        self.transformation_path, self.X_train_scaled, self.y_train_resampled = self.data_transform.data_tranformation()
        self.model_path, self.model = self.model_train.model_trainer()

    def model_evaluation(self):
        try:
            logging.info("Started Model Evaluation")
            df = pd.read_csv(self.test_path)

            X_test = df.drop(['Class'], axis=1)
            y_test = df['Class']

            # Load the saved model and scaler
            rf_model = joblib.load(self.model_path)
            scaler = joblib.load(self.transformation_path)

            # Scale new data (e.g., test data)
            X_test_scaled = scaler.transform(X_test)

            # Make predictions
            new_y_pred = self.model.predict(X_test_scaled)
            prev_y_pred = rf_model.predict(X_test_scaled)

            new_f1 = f1_score(y_test, new_y_pred)
            prev_f1 = f1_score(y_test, prev_y_pred)

            if new_f1 > prev_f1:
                try:
                    logging.info("Started Model Saving")
                    joblib.dump(rf_model, self.model_path)
                    logging.info("Saving Completed")
                except Exception as e:
                    logging.error("Error at Model Saving ", e)

            # accuracy = accuracy_score(y_test, y_pred)
            # precision = precision_score(y_test, y_pred)
            # recall = recall_score(y_test, y_pred)
            # conf_matrix = confusion_matrix(y_test, y_pred)
            # class_report = classification_report(y_test, y_pred)


            # print(f"New F1-Score: {new_f1:.4f}")
            # print(f" Previous F1-Score: {prev_f1:.4f}")
            logging.info("Model Evaluation Completed")
        except Exception as e:
            logging.error("Error at Model Evaluation ", e)


