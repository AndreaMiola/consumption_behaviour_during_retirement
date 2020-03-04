import pandas as pd
import statsmodels.api as sm
from linearmodels import PanelOLS


# Setting parameters

years_classes = [[1923, 1939], [1940, 1955], [1956, 1978]]

indep_1 = [
    "job_Retired",
    "educ_year",
    "yrbirth",
    "hhsize",
    "gender_Female",
    "int_year",
    "country",
]

indep_2 = [
    "exret",
    "educ_year",
    "yrbirth",
    "hhsize",
    "gender_Female",
    "int_year",
    "country",
]

indeps = [indep_1, indep_2]

# Importing input

raw = pd.read_csv("../original_data/share_final.csv")

# Define function generating categorical variable


def gen_categ(low=0, up=0):
    """
    Docstring
    """
    share_final = raw.copy()
    if low == 0:
        time = pd.Categorical(share_final.time)
        share_final.set_index(["mergeid", "time"], inplace=True)
        share_final["time"] = time

        country = pd.Categorical(share_final.country)
        share_final["country"] = country
        return share_final
    else:
        a = raw.loc[(raw["yrbirth"] >= low) & (raw["yrbirth"] <= up)]
        time = pd.Categorical(a.time)
        a.set_index(["mergeid", "time"], inplace=True)
        a["time"] = time

        country = pd.Categorical(a.country)
        a["country"] = country

        subsample = a.copy()

        return subsample


# Define function for Panel regression


def panel_reg(dataframe, indep, low=0, up=0):
    """
    Docstring
    """
    if low == 0:
        exog = sm.add_constant(dataframe[indep])
        mod = PanelOLS(dataframe.consumption_homefood, exog, time_effects=True)
        fe_res = mod.fit(
            use_lsdv=True, cov_type="clustered", cluster_entity=True, cluster_time=True
        )
        # Setting output name
        name = "main_regression_" + indep[0]
        # Exporting summary table in latex
        summary_table = fe_res.summary
        f = open((name + ".tex"), "w")
        f.write(summary_table.as_latex())
        f.close()
    else:
        exog = sm.add_constant(dataframe[indep])
        mod = PanelOLS(dataframe.consumption_homefood, exog, time_effects=True)
        fe_res = mod.fit(
            use_lsdv=True, cov_type="clustered", cluster_entity=True, cluster_time=True
        )
        # Setting output name
        name = "sub_regression_" + indep[0] + "_" + str(low) + "_" + str(up)
        # Exporting summary table in latex
        summary_table = fe_res.summary
        f = open((name + ".tex"), "w")
        f.write(summary_table.as_latex())
        f.close()
        # Exporting subregression output for plotting
        fe_res.std_errors.to_pickle(name + "_std" + ".pkl")
        fe_res.params.to_pickle(name + "_par" + ".pkl")


# Main regression

for indep in indeps:
    panel_reg(gen_categ(), indep)
    # Subsample (by year) regression
    for y in years_classes:
        panel_reg(gen_categ(y[0], y[1]), indep, y[0], y[1])
