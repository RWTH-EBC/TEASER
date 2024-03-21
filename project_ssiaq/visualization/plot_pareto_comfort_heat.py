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

def plot_comfort_violations_heat_demand_diff_building_type(df):
    hue_order = ["EFH","MFH","GMFH","RH","Schule","Hotel","Büro"]

    ax = sns.scatterplot(data=df, y="Specific heat demand - Diff", x="Comfort violations - Diff",
                         hue="Building type", hue_order=hue_order)
    sns.set_style("white")

    plt.legend(loc='upper right')

    plt.xlabel("Komfortverletzungen in Kh/a", fontweight='bold')
    plt.ylabel("Spezifischer Wärmebedarf in kWh/m2*a", fontweight='bold')
    plt.title("Differenz zwischen Referenz und Bedarfsgerechter Regelung", fontweight='bold')
    plt.tight_layout()
    plt.savefig("Komfortverletzungen_Wärmebedarf_Pareto_Gebäudetyp")
    plt.show()

def plot_comfort_violations_heat_demand_diff_building_age(df):
    hue_order = ["Altbau","Zwischenbau","Neubau"]

    ax = sns.scatterplot(data=df, y="Specific heat demand - Diff", x="Comfort violations - Diff",
                         hue="Baualtersklasse", hue_order=hue_order)
    sns.set_style("white")

    plt.legend(loc='upper right')

    plt.xlabel("Komfortverletzungen in Kh/a", fontweight='bold')
    plt.ylabel("Spezifischer Wärmebedarf in kWh/m2*a", fontweight='bold')
    plt.title("Differenz zwischen Referenz und Bedarfsgerechter Regelung", fontweight='bold')
    plt.tight_layout()
    plt.savefig("Komfortverletzungen_Wärmebedarf_Pareto_Baualtersklasse")
    plt.show()

def plot_comfort_violations_heat_demand_diff_combined(df):

    df["HUE"] = df["Building type"] + ' ' + df["Baualtersklasse"]
    hue_order = ["EFH Altbau","EFH Zwischenbau","EFH Neubau",
                 "MFH Altbau","MFH Zwischenbau","MFH Neubau",
                 "GMFH Altbau","GMFH Zwischenbau","GMFH Neubau",
                 "RH Altbau", "RH Zwischenbau","RH Neubau",
                 "Schule Altbau","Schule Zwischenbau","Schule Neubau",
                 "Hotel Altbau","Hotel Zwischenbau","Hotel Neubau",
                 "Büro Altbau", "Büro Zwischenbau","Büro Neubau"]

    ax = sns.scatterplot(data=df, y="Specific heat demand - Diff", x="Comfort violations - Diff",
                         hue="HUE", hue_order=hue_order, style="HUE")
    sns.set_style("white")

    plt.legend(loc='upper right',bbox_to_anchor = (1.45, 0.95))

    plt.xlabel("Komfortverletzungen in Kh/a", fontweight='bold')
    plt.ylabel("Spezifischer Wärmebedarf in kWh/m2*a", fontweight='bold')
    plt.title("Differenz zwischen Referenz und bedarfsgerechter Regelung", fontweight='bold')
    plt.tight_layout()
    plt.savefig("Komfortverletzungen_Wärmebedarf_Pareto")
    plt.show()


if __name__ == '__main__':

    setup_name_1 = "20230802_referenz_rand"
    basepath_1 = Path(r'R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten\01_Referenzszenarien').joinpath(
        setup_name_1, "sim_results")

    setup_name_2 = "20230803_ddc_rand"
    basepath_2 = Path(r'R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten\02_Bedarfsorientierte_Regelung').joinpath(
        setup_name_2, "sim_results")

    df1 = pd.read_pickle(basepath_1.joinpath('dataframe_heat_comfort_total.pkl'))
    df2 = pd.read_pickle(basepath_2.joinpath('dataframe_heat_comfort_total.pkl'))

    df2.rename(columns={"Specific heat demand": "Specific heat demand - DD"}, inplace=True)
    df2["Specific heat demand - Ref"] = df1["Specific heat demand"]
    df2["Specific heat demand - Diff"] = df2["Specific heat demand - Ref"] - df2["Specific heat demand - DD"]

    df2.rename(columns={"Comfort violations": "Comfort violations - DD"}, inplace=True)
    df2["Comfort violations - Ref"] = df1["Comfort violations"]
    df2["Comfort violations - Diff"] = df2["Comfort violations - Ref"] - df2["Comfort violations - DD"]

    df2.rename(columns={"Construction year": "Baualtersklasse"}, inplace=True)
    df2 = df2.replace([1960, 1978, 1996, 2020], ["Altbau", "Altbau", "Zwischenbau", "Neubau"])
    df2 = df2.replace(["multi_family_house", "single_family_house", "apartment_block", "terraced_house",
                       "school", "hotel", "office"], ["MFH", "EFH", "GMFH", "RH",
                       "Schule", "Hotel", "Büro"])

    # select plot functions
    #plot_comfort_violations_heat_demand_diff_building_type(df2)
    #plot_comfort_violations_heat_demand_diff_building_age(df2)
    plot_comfort_violations_heat_demand_diff_combined(df2)