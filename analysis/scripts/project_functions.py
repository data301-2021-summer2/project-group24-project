import pandas as pd
import numpy as np
def load_and_process(url_or_path_to_csv_file):
    df1=pd.read_csv(url_or_path_to_csv_file).rename(columns={'charges':'Insurance Premium'}).dropna()
    return df1

load_and_process('/Users/feisong/Desktop/DATA_301/project-group24-project/data/raw/Raw Data.csv')