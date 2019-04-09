import pandas as pd
import numpy as np
df = pd.read_csv("./Minimum Wage Data.csv", encoding="latin")
df.to_csv("./minwage.csv", encoding="utf-8")

df = pd.read_csv("./minwage.csv")
print(df.head(25))
df.shape
gb = df.groupby("State")
gb.get_group("Alaska").set_index("Year").head()

act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index(
            "Year")[["Low.2018"]].rename(columns={"Low.2018": name})
    else:
        act_min_wage = act_min_wage.join(group.set_index(
            "Year")[["Low.2018"]].rename(columns={"Low.2018": name}))
act_min_wage.head()
act_min_wage.describe()
act_min_wage.corr().head()

idf = df[df["Low.2018"] == 0.0]
print(idf.head())
# idf['State'].unique()


grouped_issues = idf.groupby("State")
# grouped_issues.get_gr

for state, data in grouped_issues:
    if data["Low.2018"].sum() != 0.0:
        print('you done fuked up')

min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()

for prob in idf["State"].unique():
    if prob in min_wage_corr.columns:
        # data['Low.2018'].sum() != 0.0:
        print('you done fuked up')
