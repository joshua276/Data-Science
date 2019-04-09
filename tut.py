import pandas as pd
import matplotlib as plt
import tkinter as Tk

df = pd.read_csv("/home/joshuareynold/Documents/Data Analysis/avocado.csv")

df.head(3)
# df["AveragePrice"].head()
df.AveragePrice.head()

alb_df = df[df['region'] == 'Albany']
alb_df.head()

alb_df.index

alb_df.set_index('Date')
alb_df.head()

# alb_df = alb_df.set_index('Date')
alb_df.set_index('Date', inplace=True)

alb_df.head()

alb_df['AveragePrice'].plot()
plt.pyplot.show()
