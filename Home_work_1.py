import pandas as pd

df = pd.read_csv('World Population by country 2024.csv')

df.fillna(0, inplace=True)


print(df.head())
print(df.tail())
print(df.info())
print(df.describe())