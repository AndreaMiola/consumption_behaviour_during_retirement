.. _introduction:


************
Introduction
************

I decided to split the code in different folders and modules because I believe that any changes might be made more efficient to be implemented, since
every step of our work is well divided and recognizable.

The work is divided as follow:
- Original Data: I stored raw data from SHARE - Survey of Health, Ageing and Retirement
in Europe in the "original_data" folder. There are 3 type of .dta files repeated
for 7 waves. They contain information about employment and pension status, consumption
and demographics characteristics. Only one data file regards the education ISCED
index.
- Data management: I merged the different data files in one dataframes called
share_final. This is a panel data index by individual id and wave time. Since it
was a huge workflow I decided to split the cleaning part, where I prepare the dataset
for the regression.
- Analysis: This is the core work of the project, it contains the regression estimation
and also the visualization part for the heterogeneity analysis.
- Paper: I wrote a paper with the motivation, description of the dataset, comments
and results of the regressions.

The output of the code is stored in the bld.out folder where:

    1. **data_management** → **OUT_DATA**
    2. **analysis.regression** → **OUT_TABLES** and → **OUT_DATA**
    3. **analysis.visualizing_data** → **OUT_FIGURES**

The final paper is store in the bld.src folder.
