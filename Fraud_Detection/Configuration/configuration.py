from Fraud_Detection.Logger import logging
from Fraud_Detection.Constants.constants import *
from Fraud_Detection.Util.util import read_yaml_file
from Fraud_Detection.Entity.entity import *
from Fraud_Detection.Logger import logging


class Config:

    def __init__(self, config_info):
        self.config_info = config_info
        # self.config_info = read_yaml_file(self.config_file_path)


    def data_ingestion(self):
        try: 
            logging.info("Started Data Ingestion Configuration")
            raw_dataset_file_name = self.config_info[DATA_INGESTION_CONFIG_KEY][DATASET_FILE_NAME_CONFIG_KEY]
            raw_dataset_folder_name = self.config_info[DATA_INGESTION_CONFIG_KEY][DATASET_FOLDER_NAME_CONFIG_KEY]
            dataset_folder_name = self.config_info[DATA_INGESTION_CONFIG_KEY][NEW_DATASET_FOLDER_CONFIG_KEY]
            train_test_data = self.config_info[DATA_INGESTION_CONFIG_KEY][TRAIN_TEST_DATA_CONFIG_KEY]
            train_dir = self.config_info[DATA_INGESTION_CONFIG_KEY][TRAIN_DIR_CONFIG_KEY]
            test_dir = self.config_info[DATA_INGESTION_CONFIG_KEY][TEST_DIR_CONFIG_KEY]

            data_ingestion_config = DataIngestionConfig(dataset_file_name = raw_dataset_file_name, dataset_folder_name = raw_dataset_folder_name, new_dataset_folder_name = dataset_folder_name,
                                                        train_test_data = train_test_data, train_dir=train_dir, test_dir=test_dir)
            
            logging.info("Data Ingestion Configuration Completed")

            return data_ingestion_config
        except Exception as e:
            logging.error("Error at Data Ingestion Configuration ", e)
    
    def data_validation(self):
        try:
            logging.info("Started Data Validation Configuration")
            data_validation_folder = self.config_info[DATA_VALIDATION_CONFIG_KEY][DATA_VALIDATION_FOLDER_CONFIG_KEY]
            report_file_name = self.config_info[DATA_VALIDATION_CONFIG_KEY][DATA_VALIDATION_REPORT_FILE_NAME_CONFIG_KEY]
            report_page_file_name = self.config_info[DATA_VALIDATION_CONFIG_KEY][DATA_VALIDATION_REPORT_PAGE_FILE_NAME_CONFIG_KEY]

            data_validation_config = DataValidationConfig(report_file_name=report_file_name, report_page_file_name=report_page_file_name, data_validation_folder=data_validation_folder)

            logging.info("Data Validation Configuration Completed")

            return data_validation_config
        except Exception as e:
            logging.error("Error at Data Validation Configuration ", e)

    
    def data_transformation(self):
        try:
            logging.info("Started Data Transformation Configuration")
            data_transformation_preprocessed_dir_name = self.config_info[DATA_TRANSFORMATION_CONFIG_KEY][DATA_TRANSFORMAATION_PREPROCESSED_DIR_CONFIG_KEY]
            data_transformation_preprocessed_file_name = self.config_info[DATA_TRANSFORMATION_CONFIG_KEY][DATA_TRANSFORMATION_PREPROCESSED_OBJECT_FILE_NAME]
            data_transformation_artifact = self.config_info[DATA_TRANSFORMATION_CONFIG_KEY][DATA_TRANSFORMATION_ARTIFACT_DIR_CONFIG_KEY]

            data_transformation_config = DataTransformationConfig(preprocessing_dir = data_transformation_preprocessed_dir_name, preprocessed_object_file_name = data_transformation_preprocessed_file_name, 
                                                                data_transformation_artifact_dir = data_transformation_artifact)
            
            logging.info("Data Transformation Configuration Completed")

            return data_transformation_config
        except Exception as e:
            logging.error("Error at Data Transformation Configuration ", e)
    
    def Model_Trainer(self):
        try:
            logging.info("Started Model Training Configuration")
            model_trainer_artifact_dir = self.config_info[MODEL_TRAINER_CONFIG_KEY][MODEL_TRAINER_ARTIFACT_DIR_CONFIG_KEY]
            model_trainer_dir = self.config_info[MODEL_TRAINER_CONFIG_KEY][MODEL_TRAINER_DIR_CONFIG_KEY]
            model_trainer_file_name = self.config_info[MODEL_TRAINER_CONFIG_KEY][MODEL_TRAINER_OBJECT_FILE_NAME]

            model_trainer_config = ModelTrainerConfig(model_trainer_artifact_dir = model_trainer_artifact_dir, model_dir = model_trainer_dir,  model_trainer_object_file_name = model_trainer_file_name)

            logging.info("Model Training Configuration Completed")
            return model_trainer_config
        except Exception as e:
            logging.error("Error at Model Training Configuration ", e)
        
