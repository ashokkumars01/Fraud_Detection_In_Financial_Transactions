from Fraud_Detection.Logger import logging
import yaml
import os


def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
        logging.info("Reading Yaml file Successful")
    except Exception as e:
        logging.error("Error while reading Yaml file", e)


def get_latest_folder(directory):
    # Get all folders in the directory
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    if not folders:
        return None
    # Find the latest folder by modification time
    latest_folder = max(folders, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
    
    return latest_folder
