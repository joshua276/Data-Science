#!/usr/bin/env python
import pandas as pd
import matplotlib as plt

# df = pd.read_csv("./avocado.csv")
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(df)

#
# print("NOWIS TIME***************************************************************************************")
# df["Date"] = pd.to_datetime(df["Date"])
# print(df)
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(df)


# alb_df = df[df["region"] == "Albany"]
# # alb_df.head()
# alb_df.set_index("Date", inplace=True)
# fig1 = alb_df["AveragePrice"].plot()
# # matplotlib.pyplot.show(fig1)
# # plt.pyplot.show(fig1)

# fig2 = alb_df['AveragePrice'].rolling(25).mean().plot()
# plt.pyplot.show(fig2)

# alb_df.sort_index(inplace=True)
# fig3 = alb_df['AveragePrice'].rolling(25).mean().plot()
# plt.pyplot.show(fig3)

# alb_df['price25ma'] = alb_df['AveragePrice'].rolling(25).mean()
# alb_df.dropna(inplace=True)
# alb_df.head()

# alb_df = df.copy()[df["region"] == "Albany"]
# list(set(df['region'].values.tolist()))
# df.shape
# df['region'].unique

# graph_df = pd.DataFrame()
# for region in df['region'].unique():
#     print(region)
#     region_df = df.copy([df['region'] == region])
#     region_df.set_index('Date', inplace=True)
#     region_df.sort_index(inplace=True)
#     region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(
#         25).mean()
#     df.head(100)
#     if graph_df.empty:
#         graph_df = region_df[[f"{region}_price25ma"]]
#     else:
#         graph_df = graph_df.join(region_df[f"{region}_price25ma"])


df = pd.read_csv("./avocado.csv")
df = df.copy()[df['type'] == 'organic']

df["Date"] = pd.to_datetime(df["Date"])

df.sort_values(by="Date", ascending=True, inplace=True)
print(df.head())

graph_df = pd.DataFrame()

for region in df['region'].unique():
    region_df = df.copy()[df['region'] == region]
    region_df.set_index('Date', inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"] = region_df["AveragePrice"].dropna().rolling(
        25).mean()

    if graph_df.empty:
        # note the double square brackets! (so df rather than series)
        graph_df = region_df[[f"{region}_price25ma"]].dropna()

    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])

print(graph_df.tail())
ax = graph_df.plot(figsize=(10, 10))
ax.legend(loc='right')
# graph_df.legend(loc='right')
plt.pyplot.show()
