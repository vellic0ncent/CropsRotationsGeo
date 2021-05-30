import re
import os
import pandas as pd
from functools import reduce


def get_data_files_list(path: str, data_batch: str):

    """ Parameters:
    path: files location in directory. String format;
    data_batch: train, validate or predict. String format.
    """

    pattern = {
        'train': re.compile(r'train_\d{4}.csv'),
        'validate': re.compile(r'test_\d{4}.csv'),
        'predict': re.compile(r'predict_\d{4}.csv'),
    }

    list_of_files = os.listdir(path)
    dataframes = []
    for file in list_of_files:
        if pattern[data_batch].match(file):
            dataframes.append(file)

    return dataframes


def get_data(path: str, data_batch: str):
    frames = []
    for file_name in get_data_files_list(path, data_batch):
        frame = pd.read_csv(f"{path}/{file_name}", sep=",")
        frames.append(frame)
    return frames
