import pandas as pd
import numpy as np
def load_and_process(url_or_path_to_csv_file):
    df1=(
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={'age':'Age','sex':'Sex','bmi':'BMI','children':'Children','smoker':'Smoker','region':'Region','charges':'Insurance Premium'})
        .dropna())
    return df1

# this is to import the data
# then to rename the columns with the first letter capitalized
# and to drop the Nan values
