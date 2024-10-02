from Fraud_Detection.Util.util import read_yaml_file
from Fraud_Detection.Logger import logging
from Fraud_Detection.components.data_ingestion import DataIngestion
from Fraud_Detection.components.data_transformation import DataTransformation
from Fraud_Detection.components.model_trainer import ModelTrainer
from Fraud_Detection.components.model_evaluation import ModelEvaluation
from Fraud_Detection.Configuration.configuration import Config



class Pipeline:

    def __init__(self, yaml_file_path):
        try:
            logging.info("Started Reading Yaml file")
            self.yaml_file_path = yaml_file_path

            self.yaml_content = read_yaml_file(self.yaml_file_path)
            self.config = Config(self.yaml_content)

            self.data_ingestion_config = self.config.data_ingestion()
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
                    self.train_data_path, self.test_data_path = self.data_ingestion.split_data_train_test()
                    logging.info("Data Ingestion Pipeline Completed")
                except Exception as e:
                    logging.error("Error at Data Ingestion Pipeline ", e)
            start_data_ingestion()

            def start_data_transformation():
                try:
                    logging.info("Started Data Transformation Pipeline")
                    self.data_transformation = DataTransformation(self.data_ingestion_config, self.data_transformation_config)
                    self.transformed_path, self.X_train_scaled, self.y_train_resampled = self.data_transformation.data_tranformation()
                    logging.info("Data Transformation Pipeline Completed")
                except Exception as e:
                    logging.error("Error at Data Transformation Pipeline ", e)

            start_data_transformation()

            # def start_model_trainer():
            #     try:
            #         logging.info("Started Model Training Pipeline")
            #         self.model_trainer = ModelTrainer(self.data_ingestion_config, self.data_transformation_config, self.model_trainer_config)
            #         self.model_path, self.model = self.model_trainer.model_trainer()
            #         logging.info("Model Training Pipeline Completed")
            #     except Exception as e:
            #         logging.error("Error at Model Training Pipeline ", e)

            # start_model_trainer()

            def start_model_evaluation():
                try:
                    logging.info("Started Model Evaluation Pipeline")
                    self.model_eval = ModelEvaluation(self.data_ingestion_config, self.data_transformation_config, self.model_trainer_config)
                    self.model_eval.model_evaluation()
                    logging.info("Model Evaluation Pipeline Completed")
                except Exception as e:
                    logging.error("Error at Model Evaluation Pipeline ", e)

            start_model_evaluation()

            logging.info("Pipeline Completed")

        except Exception as e:
            logging.error("Error at Pipeline ", e)



