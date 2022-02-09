import pandas as pd
import datetime as dt
import numpy as np

def proc_stock(path, index="timestamp", nan_col=["JEC", "BBT"]):
    """Function that processes raw stock file
    Parameters:
        path(Windows path):Path to csv file
        index(str): Column to set as index
    
    Returns:
        raw_df(Pandas.Dataframe)"""

    raw_df = pd.read_csv(path, sep=";")
    raw_df.rename(columns={"Unnamed: 0": index}, inplace=True)
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
    df.set_index(index, inplace=True)

    return df


def flatten(tab):
    """Function that flattens list of list"""
    return [item for subtab in tab for item in subtab]
    

def select_stock(stock_df, carbon_df, best=5, dropfinance=True):
    """ 
    function that selects stock for each sector 
    according to best carbon footprint.
    Parameters:
        stock_df(Pandas.Dataframe):dataframe with stock data
        carbon_df(Pandas.Dataframe):dataframe with carbon data
        best(int): best of category to choose
        
        Returns:
            stock_df: selelected stock
            out_dic: dictionary with the choosed assets by category
    """
    out_dic = {}
    out_tab = []
    if dropfinance:
        carbon_df.drop(columns="Finance")
        
    for i, sector in enumerate(carbon_df["sector_name"].unique()):

        out_tab.append(carbon_df.loc[carbon_df["sector_name"] == sector].nsmallest(5, "intensity").index.tolist())
        out_dic[sector] = carbon_df.loc[carbon_df["sector_name"] == sector].nsmallest(5, "intensity").index.tolist()

    out_tab = flatten(out_tab)
    
    return stock_df[out_tab], out_dic