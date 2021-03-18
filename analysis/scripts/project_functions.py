import pandas as pd

data = pd.read_csv("../../data/raw/aug_train.csv")

def load_and_process(data_file):
    df = (
    data.sort_values("city", ascending= True)
    .dropna()
    .drop(columns='target')
    .rename(columns = {"city_development_index": "city_index"})
    .loc[:, ["enrollee_id", "gender", "company_type", "company_type"]]
    )
    return df
load_and_process(data)
