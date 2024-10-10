from Fraud_Detection.Constants.constants import *
from sklearn.ensemble import RandomForestClassifier
import joblib
from Fraud_Detection.Logger import logging


class ModelTrainer:

    def __init__(self, model_trainer_config, X_train_scaled, y_train_resampled):
        self.model_trainer_config = model_trainer_config
        self.X_train_scaled = X_train_scaled
        self.y_train_resampled = y_train_resampled


    def model_trainer(self):

        try:
            logging.info("Started Model Training")
            # Train a Random Forest model
            rf_model = RandomForestClassifier()
            rf_model.fit(self.X_train_scaled, self.y_train_resampled)
            root_dir = ROOT_DIR
            model_dir = self.model_trainer_config.model_dir
            model_trainer_file_name = self.model_trainer_config.model_trainer_object_file_name
            dir_path = os.path.join(root_dir,model_dir)
            os.makedirs(dir_path, exist_ok=True)
            path = os.path.join(dir_path, model_trainer_file_name)
            # joblib.dump(rf_model, path)
            logging.info("Model Training Completed")

            return path, rf_model
        
        except Exception as e:
            logging.error("Error at Model Training ", e)