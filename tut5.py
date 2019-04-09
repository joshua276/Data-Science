import pandas as pd
import numpy as np

unemp_county = pd.read_csv("./unemployment-by-county-us/output.csv")

df = pd.read_csv("./minwage.csv")

act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index(
            "Year")[["Low.2018"]].rename(columns={"Low.2018": name})
    else:
        act_min_wage = act_min_wage.join(group.set_index(
            "Year")[["Low.2018"]].rename(columns={"Low.2018": name}))
act_min_wage = act_min_wage.replace(0, np.NaN).dropna(axis=1)

print(act_min_wage.head())
# print(unemp_county.head())
