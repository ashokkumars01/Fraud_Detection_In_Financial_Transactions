from Fraud_Detection.Entity.entity import DataIngestionConfig
from Fraud_Detection.Logger import logging
import sys, os, shutil
from Fraud_Detection.Constants.constants import *
from sklearn.model_selection import StratifiedShuffleSplit
import pandas as pd


class DataIngestion:

    def __init__(self, data_ingestion_config):
        self.data_ingestion_config = data_ingestion_config

    def download_dataset(self):
        root_dir = ROOT_DIR
        raw_dataset_folder = self.data_ingestion_config.dataset_folder_name
        raw_dataset_name = self.data_ingestion_config.dataset_file_name
        raw_dataset_path = os.path.join(root_dir, raw_dataset_folder, raw_dataset_name)

        time_stamp = get_current_time_stamp()

        artifact_dir = ARTIFACT_DIR_CONFIG_KEY

        new_dataset_folder = self.data_ingestion_config.new_dataset_folder_name

        new_dataset_path = os.path.join(root_dir, artifact_dir, new_dataset_folder, time_stamp)

        os.makedirs(new_dataset_path, exist_ok=True)

        shutil.copy(raw_dataset_path, new_dataset_path)

        new_dataset_path = os.path.join(new_dataset_path, "creditcard.csv")

        return new_dataset_path
    
    def split_data_train_test(self):
        df = pd.read_csv(self.download_dataset())

        X = df.drop(['Class', 'Time'], axis=1)
        y = df['Class']

        split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

        for train_index, test_index in split.split(X, y):
            X_train, X_test = X.iloc[train_index], X.iloc[test_index]
            y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        train_data = pd.concat([X_train, y_train], axis=1)
        test_data = pd.concat([X_test, y_test], axis=1)

        root_dir = ROOT_DIR
        artifact_dir = ARTIFACT_DIR_CONFIG_KEY
        train_test_dir = self.data_ingestion_config.train_test_data
        time_stamp = get_current_time_stamp()
        train_dir = self.data_ingestion_config.train_dir
        test_dir = self.data_ingestion_config.test_dir
        train = "train.csv"
        test = "test.csv"

        train_path = os.path.join(root_dir, artifact_dir, train_test_dir, time_stamp, train_dir)
        test_path = os.path.join(root_dir, artifact_dir, train_test_dir, time_stamp, test_dir)

        os.makedirs(train_path, exist_ok=True)
        os.makedirs(test_path, exist_ok=True)

        train_data_path = os.path.join(train_path, train)
        test_data_path = os.path.join(test_path, test)

        train_data.to_csv(train_data_path, index=False)
        test_data.to_csv(test_data_path, index=False)

        return train_data_path, test_data_path





