"""Plotting graphs for sub_sample data pointing out the interval confidence
of the different year classes for the expected retirment (exret) and for
actual retirment event (dummy variable job_Retired) coefficients.
"""
import pandas as pd
from matplotlib import pyplot as plt
from regression import years_classes

from bld.project_paths import project_paths_join as ppj

# Import each dataFrame of sub_regression_

for indep in ["exret", "job_Retired"]:
    coefs = []
    deviations = []
    labels = []
    for years in years_classes:
        sub_par = pd.read_pickle(
            ppj(
                "OUT_DATA",
                "sub_regression_"
                + indep
                + "_"
                + str(years[0])
                + "_"
                + str(years[1])
                + "_par.pkl",
            )
        )
        sub_std = pd.read_pickle(
            ppj(
                "OUT_DATA",
                "sub_regression_"
                + indep
                + "_"
                + str(years[0])
                + "_"
                + str(years[1])
                + "_std.pkl",
            )
        )
        coef = sub_par[1]
        dev = sub_std[1] * 1.96
        labels.append("From " + str(years[0]) + " to " + str(years[1]))
        coefs.append(coef)
        deviations.append(dev)
    df_plot = pd.DataFrame([coefs, deviations, labels])
    exp_name = "CI_" + indep + ".pdf"
    plt.figure()
    x = range(1, len(df_plot.index) + 1)
    y = df_plot.iloc[0]
    yerr = df_plot.iloc[1]

    plt.errorbar(x, y, fmt="bo", yerr=yerr, uplims=True, lolims=True)
    plt.xticks(range(1, len(df_plot.index) + 1), df_plot.iloc[2], size="small")
    plt.title(
        "Confidence intervals of " + indep + " per years classes",
        fontsize=10,
        weight="bold",
        wrap="True",
    )
    plt.savefig(ppj("OUT_FIGURES", exp_name))
