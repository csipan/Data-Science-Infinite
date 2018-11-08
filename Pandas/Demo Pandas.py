import pandas as pd
import numpy as np


def header(msg):
    print('-' * 50)
    print('[ ' + msg + ']')


header("1. Reading the file")
filename = "my_data.csv"
df = pd.read_csv(filename)

header("2. Prettifying the data")
df.replace(["None", "[]"], ["NaN", "NaN"], inplace=True)
# Deleting the spaces from the fields
df_obj = df.select_dtypes(["object"])
df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
# print(df["lead"])

# for column in column_names:
#     df["column"] = df["column"].str.strip()
# df["date"] = df["date"].str.strip()
# df["lead"] = df["lead"].str.strip()
# df["text"] = df["text"].str.strip()

# print(df["lead"])
df.to_csv("good_data.csv", index=False)

filename_1 = "good_data.csv"
df1 = pd.read_csv(filename_1)
# Filling the empty fields with NaN
df1.fillna(value="NaN", inplace=True)
df1.to_csv("good_data.csv", index=False)
# print(df1["lead"][598])
# print(df["lead"])
