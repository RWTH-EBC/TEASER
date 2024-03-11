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

def plot_heat_demand_reference(df):
    sns.set_style("white")
    ax = sns.stripplot(data=df, x="Building type", y="Specific heat demand", hue="Construction year")
    #labels = ax.get_xticklabels()
    ax.set_xticklabels(["","MFH"," ", "EFH","",  "GMFH","", "RH","", "Schule","", "Hotel","", "Büro",""])

    plt.xlabel("Gebäudetyp")
    plt.ylabel("Spezifischer Wärmebedarf in kWh/m2")
    plt.show()


if __name__ == '__main__':
    """
    setup_name = "20230803_ddc_rand"
    basepath = Path(r'R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten\02_Bedarfsorientierte_Regelung').joinpath(
        setup_name, "sim_results")
    """
    setup_name = "20230802_referenz_rand"
    basepath = Path(r'R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten\01_Referenzszenarien').joinpath(
        setup_name, "sim_results")

    df = pd.read_pickle(basepath.joinpath('dataframe_heat_demand_total.pkl'))
    #df['Building type'] = df['Building type'].astype('string')
    df = df.replace(["multi_family_house", "single_family_house", "apartment_block", "terraced_house", "school", "hotel", "office"], range(1,8))
    plot_heat_demand_reference(df)