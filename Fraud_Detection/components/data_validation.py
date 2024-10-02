from Fraud_Detection.Entity.entity import DataIngestionConfig, DataValidationConfig
from Fraud_Detection.Logger import logging
import sys, os, shutil
from Fraud_Detection.Constants.constants import *
import pandas as pd
from Fraud_Detection.components.data_ingestion import DataIngestion
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import json

class DataValidation:

    def __init__(self, data_validation_config, data_ingestion_config):
        self.data_validation_config = data_validation_config
        self.data_ingestion_config = data_ingestion_config

        self.data_ingestion = DataIngestion(self.data_ingestion_config)
        self.train_path, self.test_path = self.data_ingestion.split_data_train_test()

    def get_train_test_data(self):
        train_df = pd.read_csv(self.train_path)
        test_df = pd.read_csv(self.test_path)

        return train_df, test_df
    
    # def get_and_save_data_drift_report(self):
    #     profile = Profile(sections=[DataDriftProfileSection()])

    #     train_df, test_df = self.get_train_test_data()

    #     report = json.loads(profile.json())

    #     report_file_path = self.data_validation_config.report_file_path
    #     report_dir = os.path.dirname(report_file_path)
    #     os.makedirs(report_dir, exist_ok=True)

    #     with open(report_file_path, "w") as report_file:
    #         json.dump(report, report_file, indent=6)

    #     return report
    
    def save_data_drift_report_page(self):
        report = Report(metrics=[DataDriftPreset()])
        train_df, test_df = self.get_train_test_data()
        report.run(reference_data = train_df, current_data = test_df)

        root_dir = ROOT_DIR
        artifact_dir = ARTIFACT_DIR_CONFIG_KEY
        data_validation_artifact_dir = self.data_validation_config.data_validation_folder
        time_stamp = get_current_time_stamp()
        
        html_file = self.data_validation_config.report_page_file_name

        
        folder_path = os.path.join(root_dir, artifact_dir,data_validation_artifact_dir,time_stamp)
        os.makedirs(folder_path, exist_ok=True)
        path = os.path.join(folder_path, html_file)
        report.save_html(path)

        return path

        


