from Fraud_Detection.Entity.entity import DataIngestionConfig, DataValidationConfig
from Fraud_Detection.Logger import logging
import sys, os, shutil
from Fraud_Detection.Constants.constants import *
import pandas as pd
from Fraud_Detection.components.data_ingestion import DataIngestion

class DataValidation:

    def __init__(self, data_validation_config):
        self.data_validation_config = data_validation_config

    def get_train_test_data(self):
        pass

