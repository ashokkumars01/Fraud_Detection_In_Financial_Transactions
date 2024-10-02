from Fraud_Detection.components.data_transformation import DataTransformation
from Fraud_Detection.Constants.constants import *
from sklearn.ensemble import RandomForestClassifier
import joblib
from Fraud_Detection.Logger import logging


class ModelTrainer:

    def __init__(self, data_ingestion_config, data_transformation_config, model_trainer_config):
        self.data_ingestion_config = data_ingestion_config
        self.data_transformation_config = data_transformation_config
        self.model_trainer_config = model_trainer_config

        self.data_transform = (DataTransformation(self.data_ingestion_config, self.data_transformation_config))
        _, self.X_train_scaled, self.y_train_resampled = self.data_transform.data_tranformation()

    def model_trainer(self):

        try:
            logging.info("Started Model Training")
            # Train a Random Forest model
            rf_model = RandomForestClassifier()
            rf_model.fit(self.X_train_scaled, self.y_train_resampled)

            root_dir = ROOT_DIR
            # artifact_dir = ARTIFACT_DIR_CONFIG_KEY
            # model_trainer_dir = self.model_trainer_config.model_trainer_artifact_dir
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