import numpy as np
import pandas as pd

share_final = pd.read_csv("../original_data/share_merged.csv")

share_final.set_index(["mergeid", "time"], inplace=True)

# Replace strings values with NaN
strings = ["Don't know", "Refusal", "Other", "None"]
share_final.replace(strings, np.nan, inplace=True)

# Rename columns.
share_final = share_final.rename(
    columns={
        "co002e": "consumption_homefood",
        "co003e": "consumption_outhome",
        "ep005_": "job",
        "ep106_1": "exret",
    }
)

# share_final = share_final[share_final.consumption_homefood.notnull()]

# Get a dummy variable for the column gender

gender_dummies = pd.get_dummies(share_final["gender"]).rename(
    columns=lambda x: "gender_" + str(x)
)
share_final = pd.concat([share_final, gender_dummies], axis=1)

# Give numeric value to partnerinhh clomuns

share_final["partnerinhh"] = share_final["partnerinhh"].apply({"Yes": 1, "No": 0}.get)

# Get a dummy variable for the column job

job_dummies = pd.get_dummies(share_final["job"]).rename(
    columns=lambda x: "job_" + str(x)
)
share_final = pd.concat([share_final, job_dummies], axis=1)

# Get names of indexes for which column educ_year has value Still in school

indexEduc = share_final[share_final["educ_year"] == "Still in school"].index

# Delete this row indexes from dataFrame

share_final.drop(indexEduc, inplace=True)

# Fill NaN with previous values
# Based on assumption that education years do not change over time

share_final["educ_year"].fillna(method="ffill", inplace=True)

# Fill NaN with previus values

share_final["exret"].fillna(method="ffill", inplace=True)

# Deleting missing values and zeroes for consumption

share_final["consumption_homefood"] = share_final["consumption_homefood"].replace(
    {0: np.nan}
)

share_final = share_final[share_final.consumption_homefood.notnull()]

# share_final['educ_year'] = share_final['educ_year'].replace({np.nan:0})

# logcolumns = ['consumption_homefood']

share_final.loc[:, "consumption_homefood"] = np.log(share_final["consumption_homefood"])

# share_final = share_final[share_final.consumption_homefood.notnull()]

# share_final = share_final[share_final.job.notnull()]


# Export cleaned data

export_data = share_final.to_csv(r"../original_data/share_final.csv")
