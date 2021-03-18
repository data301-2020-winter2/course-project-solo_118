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

def load_and_process4(data_file):
    df = (
    data.dropna(axis = 0)
    .drop(columns='target')
    .rename(columns = {"city_development_index": "city_index"})
    .sort_values("city_index", ascending= True)
    .loc[:, ["enrollee_id", "city_index", "company_type", "training_hours"]]
)
    
df = load_and_process(data)
df['training_hours'].plot(kind='hist', facecolor='green')
df.boxplot('training_hours')
corr = df.corr()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))

