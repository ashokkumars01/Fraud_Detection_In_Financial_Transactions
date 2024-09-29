from Fraud_Detection.Logger import logging
from Fraud_Detection.Constants.constants import *
from Fraud_Detection.Util.util import read_yaml_file
from Fraud_Detection.Entity.entity import *


class Config:

    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config_info = read_yaml_file(self.config_file_path)


    def data_ingestion(self):
        # dataset_path = os.path.join(ROOT_DIR, self.config_info[DATA_INGESTION_CONFIG_KEY][DATASET_FOLDER_NAME_CONFIG_KEY], self.config_info[DATA_INGESTION_CONFIG_KEY][DATASET_FILE_NAME_CONFIG_KEY])
        
        # Create a new folde for new dataset
        # new_dataset_path = self.config_info[NEW_DATASET_FOLDER_CONFIG_KEY]
        # time_stamp = get_current_time_stamp()
        # new_dataset_path = os.path.join(new_dataset_path, time_stamp)
        # os.makedirs(new_dataset_path,exist_ok=True)

        raw_dataset_file_name = self.config_info[DATA_INGESTION_CONFIG_KEY][DATASET_FILE_NAME_CONFIG_KEY]
        raw_dataset_folder_name = self.config_info[DATA_INGESTION_CONFIG_KEY][DATASET_FOLDER_NAME_CONFIG_KEY]
        dataset_folder_name = self.config_info[DATA_INGESTION_CONFIG_KEY][NEW_DATASET_FOLDER_CONFIG_KEY]
        train_test_data = self.config_info[DATA_INGESTION_CONFIG_KEY][TRAIN_TEST_DATA_CONFIG_KEY]
        train_dir = self.config_info[DATA_INGESTION_CONFIG_KEY][TRAIN_DIR_CONFIG_KEY]
        test_dir = self.config_info[DATA_INGESTION_CONFIG_KEY][TEST_DIR_CONFIG_KEY]

        data_ingestion_config = DataIngestionConfig(dataset_file_name = raw_dataset_file_name, dataset_folder_name = raw_dataset_folder_name, new_dataset_folder_name = dataset_folder_name,
                                                    train_test_data = train_test_data, train_dir=train_dir, test_dir=test_dir)

        return data_ingestion_config
    
    def data_validation(self):

        data_validation_folder = self.config_info[DATA_VALIDATION_CONFIG_KEY][DATA_VALIDATION_FOLDER_CONFIG_KEY]
        report_file_name = self.config_info[DATA_VALIDATION_CONFIG_KEY][DATA_VALIDATION_REPORT_FILE_NAME_CONFIG_KEY]
        report_page_file_name = self.config_info[DATA_VALIDATION_CONFIG_KEY][DATA_VALIDATION_REPORT_PAGE_FILE_NAME_CONFIG_KEY]

        data_validation_config = DataValidationConfig(report_file_name=report_file_name, report_page_file_name=report_page_file_name, data_validation_folder=data_validation_folder)

        return data_validation_config
        
