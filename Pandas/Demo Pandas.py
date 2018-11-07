import pandas as pd
import numpy as np


def header(msg):
    print('-' * 50)
    print('[ ' + msg + ']')


header("1. Reading the file")
filename = "my_data.csv"
df = pd.read_csv(filename)
df["lead"].replace(["None", "[]"], ["NaN", "NaN"], inplace=True)

for space in range(len(df["lead"])):
    df["lead"][space] = str(df["lead"][space]).strip()

# print(df["lead"])
df.to_csv("good_data.csv", index=False)

filename_1 = "good_data.csv"
df1 = pd.read_csv(filename_1)

df1["lead"].fillna(value="NaN", inplace=True)

# for unique_characters in range(len(df1["lead"])):
#     df1["lead"][unique_characters] = str(df1["lead"][unique_characters]).strip("\\n")

df1.to_csv("good_data.csv", index=False)
print(df1["lead"][598])
# print(df["lead"])
