import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("./minwage.csv")

act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index(
            "Year")[["Low.2018"]].rename(columns={"Low.2018": name})
    else:
        act_min_wage = act_min_wage.join(group.set_index(
            "Year")[["Low.2018"]].rename(columns={"Low.2018": name}))
print(act_min_wage.head())
min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()

# plt.matshow(min_wage_corr)
# plt.show()

# labels = [c[:2] for c in min_wage_corr.columns]
# fig = plt.figure(figsize=(12, 2))
# ax = fig.add_subplot(111)
# # ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)
# # plt.matshow(min_wage_corr)

# ax.set_xticklabels(labels)
# ax.set_yticklabels(labels)
# ax.set_xticks(np.arange(len(labels)))
# ax.set_yticks(np.arange(len(labels)))

# plt.show()

dfs = pd.read_html(
    "https://www.infoplease.com/state-abbreviations-and-state-postal-codes")

# for df in dfs:
#     print(df.head())

state_ab = dfs[0]
# print(state_ab.head())

state_ab.to_csv("./state_ab.csv", index=False)
state_ab = pd.read_csv("./state_ab.csv", index_col=0)
print(state_ab.head())
n
ab_dict = state_ab[["Postal Code"]].to_dict()
ab_dict = ab_dict["Postal Code"]
print(ab_dict)


ab_dict["Federal"] = "FLSA"
ab_dict["Guam"] = "GU"
ab_dict["Puerto Rico"] = "PR"

labels = [ab_dict[c] for c in min_wage_corr.columns]
ab_dict["Federal"] = "FLSA"
# # labels = [c[:2] for c in min_wage_corr.columns]
fig = plt.figure(figsize=(12, 2))
ax = fig.add_subplot(111)
ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)
plt.matshow(min_wage_corr)

ax.set_xticklabels(labels)
ax.set_yticklabels(labels)
ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(labels)))
plt.show()
# ab_dict["Federal"] = "FLSA"
