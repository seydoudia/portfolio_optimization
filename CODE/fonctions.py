import pandas as pd
import datetime as dt
import numpy as np

def proc_stock(path, index="timestamp", nan_col=["JEC", "BBT"]):

    raw_df = pd.read_csv(path, sep=";")
    raw_df.rename(columns={"Unnamed: 0": index}, inplace=True)
    raw_cols = raw_df.columns
    raw_df.columns =  [x.lower() for x in raw_df.columns]

    if index == "timestamp":
        raw_df["timestamp"] = raw_df["timestamp"].apply(lambda x: dt.datetime.strptime(x,"%d/%m/%Y"))
        raw_df.set_index("timestamp", inplace=True)
    for n_col in nan_col:
        if n_col in raw_df.columns:
            raw_df[nan_col] = np.nan

    return raw_df

def read_file(path, sep=",", index="timestamp"):
	df = pd.read_csv(path, sep=",")
	if "timestamp" in df.columns:
		df["timestamp"] = df["timestamp"].apply(lambda x: dt.datetime.strptime(x,"%Y-%m-%d"))
		df.set_index("timestamp", inplace=True)
	df.set_index(index, inplace=True)
	return df

	