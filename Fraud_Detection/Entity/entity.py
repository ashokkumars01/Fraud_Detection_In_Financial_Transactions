from collections import namedtuple

# Config File

ConfigFile = namedtuple("ConfigFile",["config_file_name", "config_folder_name"])


# Data Ingestion
DataIngestionConfig = namedtuple("DataIngestionConfig", ['dataset_file_name', 'dataset_folder_name', 'new_dataset_folder_name', 'train_test_data', 'train_dir', 'test_dir'])

DataValidationConfig = namedtuple("DataValidationConfig", ["report_file_name", "report_page_file_name", "data_validation_folder"])

Artifactory = namedtuple("Artifactory",['artifact_dir'])


