import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from Fraud_Detection.Logger import logging


class ModelEvaluation:

    def __init__(self,test_path, transformation_path, model_path, model):
        self.test_path = test_path
        self.transformation_path = transformation_path
        self.model_path = model_path
        self.model = model


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
            # print("New_f1 Score: ", new_f1)
            # print("Previous f1 score: ", prev_f1)

            if new_f1 > prev_f1:
                try:
                    logging.info("Started Model Saving")
                    joblib.dump(rf_model, self.model_path)
                    logging.info("Saving Completed")
                except Exception as e:
                    logging.error("Error at Model Saving ", e)
            logging.info("Model Evaluation Completed")

        except Exception as e:
            logging.error("Error at Model Evaluation ", e)


