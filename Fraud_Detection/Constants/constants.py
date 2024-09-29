import os
from datetime import datetime


def get_current_time_stamp():
    return str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    # return str(datetime.now())

ROOT_DIR = os.getcwd()
CONFIG_FILE_YAML_KEY = "config_file_yaml"
CONFIG_FILE_NAME = "config_file_name"
CONFIG_FOLDER_NAME = "config_folder_name"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_FOLDER_NAME, CONFIG_FILE_NAME)

# Data Ingestion Related Variables
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATASET_FOLDER_NAME_CONFIG_KEY = "dataset_folder_name"
DATASET_FILE_NAME_CONFIG_KEY = "dataset_file_name"
NEW_DATASET_FOLDER_CONFIG_KEY = "new_dataset_folder_name"
TRAIN_TEST_DATA_CONFIG_KEY = "train_test_data"
TRAIN_DIR_CONFIG_KEY = "train_dir"
TEST_DIR_CONFIG_KEY = "test_dir"

# Data Validation Related Variables
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_REPORT_FILE_NAME_CONFIG_KEY = "report_file_name"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME_CONFIG_KEY = "report_page_file_name"
DATA_VALIDATION_FOLDER_CONFIG_KEY = "data_validation_folder"

ARTIFACT_CONFIG_KEY = "artifactory"
ARTIFACT_DIR_CONFIG_KEY = "artifact"

