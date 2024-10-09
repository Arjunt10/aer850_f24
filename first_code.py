import pandas as pd

file_name = "data/housing.csv"
df = pd.read_csv(file_name)

# print dataframe column info
print(df.columns)

#how to access dataframe columns individually
x = df["population"]

#how to access dataframe rows?

third_row = df.loc[2]

