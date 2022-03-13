# -*- coding: utf-8 -*-
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
    
    carbon_df = carbon_df.loc[stock_df.columns]
    
    if dropfinance:
        carbon_df = carbon_df[carbon_df["sector_name"] != "Financial"]
    
    
    for i, sector in enumerate(carbon_df["sector_name"].unique()):
    
        out_tab.append(carbon_df.loc[carbon_df["sector_name"] == sector].nsmallest(5, "intensity").index.tolist())
        out_dic[sector] = carbon_df.loc[carbon_df["sector_name"] == sector].nsmallest(5, "intensity").index.tolist()
    
    out_tab = flatten(out_tab)
    
    return stock_df[out_tab], out_dic

# Input: tableau stock déjà préselectioné 
# Output: tableau de rendement et tableau de risk 
def equally_weighted(df, weeks=12):
    """Function that computes return and risk over a given number of weeks
    Parameters;
        df(Pandas.Dataframe):dataframe with stock data
        weeks(int): number of weeks on which to compute return
        
        Returns:
            df_summary_mean: table with return
            df_summary_std: table with standard deviation 
    """
    no_assets = len(df.columns)
    weights = [1/no_assets for i in range(no_assets)]
    #ret est le tableau de rendement 
    ret = df.pct_change().dropna()
    
    #Commande pour trouver rendement 2 possibilités 
    #ret_mean = ret.mean(axis=1)
    ret_week = ret.mul(weights, axis="columns").sum(axis=1)
    
    # Find the average of each 12 weeks
    df_summary_mean = pd.DataFrame(index=range(len(ret_week)//weeks), columns=df.columns)
    df_summary_std = pd.DataFrame(index=range(len(ret_week)//weeks), columns=df.columns)
    out_tab_mean = [0]*(len(ret_week)//weeks)
    out_tab_std = [0]*(len(ret_week)//weeks)

    for i in range(len(ret_week)//weeks):
        out_tab_mean[i] = ret_week.iloc[i*weeks:(i+1)*weeks].mean() # Portofolio mean
        df_summary_mean.iloc[i] = ret.iloc[i*weeks : (i+1)*weeks].mean() # Stock mean
        out_tab_std[i] = ret_week.iloc[i*weeks:(i+1)*weeks].std()
        df_summary_std.iloc[i] = ret.iloc[i*weeks : (i+1)*weeks].std()
    df_summary_mean["ewp_rendement"] = out_tab_mean
    df_summary_std["ewp_risk"] = out_tab_std
    
    return df_summary_mean, df_summary_std 

