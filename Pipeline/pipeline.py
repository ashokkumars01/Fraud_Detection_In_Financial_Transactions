from Fraud_Detection.Util.util import read_yaml_file
from Fraud_Detection.Logger import logging
from Fraud_Detection.components.data_ingestion import DataIngestion
from Fraud_Detection.components.data_transformation import DataTransformation
from Fraud_Detection.components.model_trainer import ModelTrainer
from Fraud_Detection.components.model_evaluation import ModelEvaluation
from Fraud_Detection.Configuration.configuration import Config
from Fraud_Detection.Constants.constants import *
from Fraud_Detection.Util.util import get_latest_folder
from Fraud_Detection.components.data_validation import DataValidation



class Pipeline:

    def __init__(self, yaml_file_path):
        try:
            logging.info("Started Reading Yaml file")
            self.yaml_file_path = yaml_file_path
            self.yaml_content = read_yaml_file(self.yaml_file_path)
            self.config = Config(self.yaml_content)
            self.data_ingestion_config = self.config.data_ingestion()
            self.data_validation_config = self.config.data_validation()
            self.data_transformation_config = self.config.data_transformation()
            self.model_trainer_config = self.config.Model_Trainer()
            logging.info("Read Yaml File Successful")

        except Exception as e:
            logging.error("Error at Reading Yaml File ", e)


    def pipeline(self):
        try:
            logging.info("Started Pipeline")
            def start_data_ingestion():
                try:
                    logging.info("Started Data Ingestion Pipeline")
                    self.data_ingestion = DataIngestion(self.data_ingestion_config)
                    self.dataset_path = self.data_ingestion.download_dataset()
                    self.train_data_path, self.test_data_path = self.data_ingestion.split_data_train_test(self.dataset_path )
                    logging.info("Data Ingestion Pipeline Completed")
                except Exception as e:
                    logging.error("Error at Data Ingestion Pipeline ", e)
            start_data_ingestion()


            def artifactory_path():
                try:
                    logging.info("Initializing Artifactory Path")
                    self.root_dir = ROOT_DIR
                    self.artifact_dir = ARTIFACT_DIR_CONFIG_KEY
                    self.train_test_dir = self.data_ingestion_config.train_test_data
                    dir_path = os.path.join(self.root_dir, self.artifact_dir, self.train_test_dir)
                    self.latest_dir = get_latest_folder(dir_path)
                    self.train_dir = self.data_ingestion_config.train_dir
                    self.test_dir = self.data_ingestion_config.test_dir
                    self.train_data_name = "train.csv"
                    self.test_data_name = "test.csv"
                    self.train_path = os.path.join(dir_path, self.latest_dir, self.train_dir, self.train_data_name)
                    self.test_path = os.path.join(dir_path, self.latest_dir, self.test_dir, self.test_data_name)
                    logging.info("Initializing Artifactory Path Completed")
                except Exception as e:
                    logging.error("Error while Initializing Artifactory Path ", e)
            artifactory_path()


            def start_data_validation():
                try:
                    logging.info("Started Data Validation Pipeline")
                    self.data_validation = DataValidation(self.data_validation_config, self.train_path, self.test_path)
                    self.train_df, self.test_df = self.data_validation.get_train_test_data()
                    self.path = self.data_validation.save_data_drift_report_page()
                    logging.info("Data Validation Pipeline Completed")
                except Exception as e:
                    logging.error("Error at Data Validation Pipeline ", e)
            start_data_validation()


            def start_data_transformation():
                try:
                    logging.info("Started Data Transformation Pipeline")
                    self.data_transformation = DataTransformation(self.data_transformation_config, self.train_path, self.test_path)
                    self.transformed_path, self.X_train_scaled, self.y_train_resampled = self.data_transformation.data_tranformation()
                    logging.info("Data Transformation Pipeline Completed")
                except Exception as e:
                    logging.error("Error at Data Transformation Pipeline ", e)
            start_data_transformation()


            def start_model_trainer():
                try:
                    logging.info("Started Model Training Pipeline")
                    self.model_trainer = ModelTrainer(self.model_trainer_config, self.X_train_scaled, self.y_train_resampled)
                    self.model_path, self.model = self.model_trainer.model_trainer()
                    logging.info("Model Training Pipeline Completed")
                except Exception as e:
                    logging.error("Error at Model Training Pipeline ", e)
            start_model_trainer()


            def start_model_evaluation():
                try:
                    logging.info("Started Model Evaluation Pipeline")
                    self.model_eval = ModelEvaluation(self.test_path, self.transformed_path, self.model_path, self.model)
                    self.model_eval.model_evaluation()
                    logging.info("Model Evaluation Pipeline Completed")
                except Exception as e:
                    logging.error("Error at Model Evaluation Pipeline ", e)
            start_model_evaluation()

            logging.info("Pipeline Completed")

        except Exception as e:
            logging.error("Error at Pipeline ", e)



