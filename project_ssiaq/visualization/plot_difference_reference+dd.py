from pathlib import Path
from ebcpy import TimeSeriesData, preprocessing
import datetime
import matplotlib.pyplot as plt

import numpy as np
import pathlib
import os
import re
import seaborn as sns
import pickle
import pandas as pd
from evaluation import get_bldg_type_from_filename

def plot_heat_demand_difference(df):


    ax = sns.stripplot(data=df, x="Building type", y="Specific heat demand - Diff", hue="Construction year")
    sns.set_style("white")
    #labels = ax.get_xticklabels()
    ax.set_xticklabels(["","MFH"," ", "EFH","",  "GMFH","", "RH","", "Schule","", "Hotel","", "Büro",""])

    plt.xlabel("Gebäudetyp")
    plt.ylabel("Differenz Spezifischer Wärmebedarf in kWh/m2")
    plt.show()


if __name__ == '__main__':

    setup_name_1 = "20230802_referenz_rand"
    basepath_1 = Path(r'R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten\01_Referenzszenarien').joinpath(
        setup_name_1, "sim_results")

    setup_name_2 = "20230803_ddc_rand"
    basepath_2 = Path(r'R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten\02_Bedarfsorientierte_Regelung').joinpath(
        setup_name_2, "sim_results")

    df1 = pd.read_pickle(basepath_1.joinpath('dataframe_heat_demand_total.pkl'))
    df2 = pd.read_pickle(basepath_2.joinpath('dataframe_heat_demand_total.pkl'))

    df1 = df1.replace(["multi_family_house", "single_family_house", "apartment_block", "terraced_house",
                       "school", "hotel", "office"], range(1,8))
    df2 = df2.replace(["multi_family_house", "single_family_house", "apartment_block", "terraced_house",
                       "school", "hotel", "office"], range(1,8))

    df2.rename(columns= {"Specific heat demand": "Specific heat demand - DD"},inplace=True)
    df2["Specific heat demand - Ref"] = df1["Specific heat demand"]
    df2["Specific heat demand - Diff"] = df2["Specific heat demand - Ref"] - df2["Specific heat demand - DD"]
    plot_heat_demand_difference(df2)