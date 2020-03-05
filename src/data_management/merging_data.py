from functools import reduce

import numpy as np
import pandas as pd

from bld.project_paths import project_paths_join as ppj

# WAVE_1_2004

# Employment and pension status
ep1_df = pd.read_stata(ppj("IN_DATA", "sharew1_rel7-0-0_ep.dta"))

# Selecte from dataframe the columns of interest
ep1_df = ep1_df[["mergeid", "ep005_", "ep106_1"]]

# Restriction: each respondent have to be working at the first wave.
ep1_df = ep1_df[
    ep1_df["ep005_"]
    == "Employed or self-employed (including working for family business)"
]

# Restriction: keep only respondent who answer to the question about expected retirment
ep1_df = ep1_df[ep1_df.ep106_1.notnull()]


# Add education level data as Standard Classification of Education (ISCED)
edu1_df = pd.read_stata(ppj("IN_DATA", "sharew1_rel7-0-0_gv_isced.dta"))

# Selecte from dataframe the columns of interest
edu1_df = edu1_df[["mergeid", "isced1997y_r"]]

# Rename the column isced1997y_r as Year od Education
edu1_df = edu1_df.rename(columns={"isced1997y_r": "educ_year"})


# Consumption data
co1_df = pd.read_stata(ppj("IN_DATA", "sharew1_rel7-0-0_co.dta"))

# Selecte from dataframe the columns of interest
co1_df = co1_df[["mergeid", "co002e", "co003e"]]

# Replace strings values with NaN
strings = ["Don't know", "Refusal", "Other", "None"]
co1_df.replace(strings, np.nan, inplace=True)


# Coverscreen on individual level

cv1_df = pd.read_stata(ppj("IN_DATA", "sharew1_rel7-0-0_cv_r.dta"))

# Selecte from dataframe the columns of interest
cv1_df = cv1_df[
    ["mergeid", "country", "hhsize", "gender", "yrbirth", "int_year", "partnerinhh"]
]


# Merge dataframes of wave_1

# Define a list of first wave dataframe
wave1_df = [ep1_df, co1_df, cv1_df, edu1_df]

# Set mergeid as index
for x in wave1_df:
    x.set_index(["mergeid"], inplace=True)

# Merge the data
wave1_df = reduce(lambda left, right: pd.merge(left, right, on="mergeid"), wave1_df)


# Add column 'time' to indentify the wave
wave1_df.insert(0, "time", "2004")

wave1_df["co002e"] = wave1_df["co002e"].replace({0: np.nan})
wave1_df = wave1_df[wave1_df.co002e.notnull()]

# print(wave1_df)

wave1_df.reset_index(inplace=True)
key = wave1_df["mergeid"]
wave1_df.set_index(["mergeid"], inplace=True)


# Import data from WAVE_2_2006

# Employment and pension status

ep2_df = pd.read_stata(ppj("IN_DATA", "sharew2_rel7-0-0_ep.dta"))

# Selecte from dataframe the columns of interest
ep2_df = ep2_df[["mergeid", "ep005_"]]

# Consumption data

co2_df = pd.read_stata(ppj("IN_DATA", "sharew2_rel7-0-0_co.dta"))

# Selecte from dataframe the columns of interest
co2_df = co2_df[["mergeid", "co002e", "co003e"]]

# Replace strings values with NaN
strings = ["Don't know", "Refusal", "Other", "None"]
co2_df.replace(strings, np.nan, inplace=True)

# Coverscreen on individual level

cv2_df = pd.read_stata(ppj("IN_DATA", "sharew2_rel7-0-0_cv_r.dta"))

# Selecte from dataframe the columns of interest
cv2_df = cv2_df[
    ["mergeid", "country", "hhsize", "gender", "yrbirth", "int_year", "partnerinhh"]
]


# Merge dataframes of wave_2

# Define a list of first wave dataframe
wave2_df = [ep2_df, co2_df, cv2_df]

# Set mergeid as index
for x in wave2_df:
    x.set_index(["mergeid"], inplace=True)

# Merge the data
wave2_df = reduce(lambda left, right: pd.merge(left, right, on="mergeid"), wave2_df)

# Add column 'time' to indentify the wave
wave2_df.insert(0, "time", "2006")

# Import data from WAVE_4_2011

# Employment and pension status
ep4_df = pd.read_stata(ppj("IN_DATA", "sharew4_rel7-0-0_ep.dta"))

# Selecte from dataframe the columns of interest
ep4_df = ep4_df[["mergeid", "ep005_"]]

# Consumption data

co4_df = pd.read_stata(ppj("IN_DATA", "sharew4_rel7-0-0_co.dta"))

# Selecte from dataframe the columns of interest
co4_df = co4_df[["mergeid", "co002e", "co003e"]]

# Replace strings values with NaN
strings = ["Don't know", "Refusal", "Other", "None"]
co4_df.replace(strings, np.nan, inplace=True)

# Coverscreen on individual level

cv4_df = pd.read_stata(ppj("IN_DATA", "sharew4_rel7-0-0_cv_r.dta"))

# Selecte from dataframe the columns of interest
cv4_df = cv4_df[
    ["mergeid", "country", "hhsize", "gender", "yrbirth", "int_year", "partnerinhh"]
]

# Merge dataframes of wave_4

# Define a list of first wave dataframe
wave4_df = [ep4_df, co4_df, cv4_df]

# Set mergeid as index
for x in wave4_df:
    x.set_index(["mergeid"], inplace=True)

# Merge the data
wave4_df = reduce(lambda left, right: pd.merge(left, right, on="mergeid"), wave4_df)

# Add column 'time' to indentify the wave
wave4_df.insert(0, "time", "2011")

# Import data from WAVE_5_2013

# Employment and pension status
ep5_df = pd.read_stata(ppj("IN_DATA", "sharew5_rel7-0-0_ep.dta"))

# Selecte from dataframe the columns of interest
ep5_df = ep5_df[["mergeid", "ep005_"]]

# Consumption data

co5_df = pd.read_stata(ppj("IN_DATA", "sharew5_rel7-0-0_co.dta"))

# Selecte from dataframe the columns of interest
co5_df = co5_df[["mergeid", "co002e", "co003e"]]

# Replace strings values with NaN
strings = ["Don't know", "Refusal", "Other", "None"]
co5_df.replace(strings, np.nan, inplace=True)

# Coverscreen on individual level

cv5_df = pd.read_stata(ppj("IN_DATA", "sharew5_rel7-0-0_cv_r.dta"))

# Selecte from dataframe the columns of interest
cv5_df = cv5_df[
    ["mergeid", "country", "hhsize", "gender", "yrbirth", "int_year", "partnerinhh"]
]


# Merge dataframes of wave_5

# Define a list of first wave dataframe
wave5_df = [ep5_df, co5_df, cv5_df]

# Set mergeid as index
for x in wave5_df:
    x.set_index(["mergeid"], inplace=True)

# Merge the data
wave5_df = reduce(lambda left, right: pd.merge(left, right, on="mergeid"), wave5_df)

# Add column 'time' to indentify the wave
wave5_df.insert(0, "time", "2013")

# Import data from WAVE_6_2015

# Employment and pension status

ep6_df = pd.read_stata(ppj("IN_DATA", "sharew6_rel7-0-0_ep.dta"))

# Selecte from dataframe the columns of interest
ep6_df = ep6_df[["mergeid", "ep005_"]]


# Consumption data

co6_df = pd.read_stata(ppj("IN_DATA", "sharew6_rel7-0-0_co.dta"))

# Selecte from dataframe the columns of interest
co6_df = co6_df[["mergeid", "co002e", "co003e"]]

# Replace strings values with NaN
strings = ["Don't know", "Refusal", "Other", "None"]
co6_df.replace(strings, np.nan, inplace=True)

# Coverscreen on individual level

cv6_df = pd.read_stata(ppj("IN_DATA", "sharew6_rel7-0-0_cv_r.dta"))

# Selecte from dataframe the columns of interest
cv6_df = cv6_df[
    ["mergeid", "country", "hhsize", "gender", "yrbirth", "int_year", "partnerinhh"]
]


# Merge dataframes of wave_6

# Define a list of first wave dataframe
wave6_df = [ep6_df, co6_df, cv6_df]

# Set mergeid as index
for x in wave6_df:
    x.set_index(["mergeid"], inplace=True)

# Merge the data
wave6_df = reduce(lambda left, right: pd.merge(left, right, on="mergeid"), wave6_df)

# Add column 'time' to indentify the wave
wave6_df.insert(0, "time", "2015")

# Import data from WAVE_7_2017

# Employment and pension status

ep7_df = pd.read_stata(ppj("IN_DATA", "sharew7_rel7-0-0_ep.dta"))

# Selecte from dataframe the columns of interest
ep7_df = ep7_df[["mergeid", "ep005_"]]


# Consumption data

co7_df = pd.read_stata(ppj("IN_DATA", "sharew7_rel7-0-0_co.dta"))

# Selecte from dataframe the columns of interest
co7_df = co7_df[["mergeid", "co002e", "co003e"]]

# Replace strings values with NaN
strings = ["Don't know", "Refusal", "Other", "None"]
co7_df.replace(strings, np.nan, inplace=True)

# Coverscreen on individual level

cv7_df = pd.read_stata(ppj("IN_DATA", "sharew7_rel7-0-0_cv_r.dta"))

# Selecte from dataframe the columns of interest
cv7_df = cv7_df[
    ["mergeid", "country", "hhsize", "gender", "yrbirth", "int_year", "partnerinhh"]
]


# Merge dataframes of wave_7

# Define a list of first wave dataframe
wave7_df = [ep7_df, co7_df, cv7_df]

# Set mergeid as index
for x in wave7_df:
    x.set_index(["mergeid"], inplace=True)

# Merge the data
wave7_df = reduce(lambda left, right: pd.merge(left, right, on="mergeid"), wave7_df)

# Add column 'time' to indentify the wave
wave7_df.insert(0, "time", "2017")

# Append every waves together
share = wave1_df.append([wave2_df, wave4_df, wave5_df, wave6_df, wave7_df])
share = share.sort_values(["mergeid", "time"])

# Merge the share dataframes with the key column of mergeid
share_merged = pd.merge(share, key, on="mergeid").set_index(["mergeid", "time"])

# Export data in a pickle file
export_data = share_merged.to_pickle(ppj("OUT_DATA", "share_merged.pkl"))
