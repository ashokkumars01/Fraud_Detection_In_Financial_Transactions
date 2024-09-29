from Fraud_Detection.Logger import logging
import yaml


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