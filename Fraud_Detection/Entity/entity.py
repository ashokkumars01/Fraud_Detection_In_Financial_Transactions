from collections import namedtuple

# Config File
ConfigFile = namedtuple("ConfigFile",["config_file_name", "config_folder_name"])

# Data Ingestion
DataIngestionConfig = namedtuple("DataIngestionConfig", ['dataset_file_name', 'dataset_folder_name', 'new_dataset_folder_name', 'train_test_data', 'train_dir', 'test_dir'])

# Data Validation
DataValidationConfig = namedtuple("DataValidationConfig", ["report_file_name", "report_page_file_name", "data_validation_folder"])

# Data Transformation
DataTransformationConfig = namedtuple("DataTransformationConfig",["preprocessing_dir", "preprocessed_object_file_name", "data_transformation_artifact_dir"])

# Model Training
ModelTrainerConfig = namedtuple("ModelTrainerConfig",["model_trainer_artifact_dir", "model_dir", "model_trainer_object_file_name"])

# Artifactory
Artifactory = namedtuple("Artifactory",['artifact_dir'])


