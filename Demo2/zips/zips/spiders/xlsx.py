import pandas as pd
import xlrd

df = pd.read_excel("C:/Users/Csipan/Desktop/Kapucinus.xlsx", sheet_name="Sheet1")
print(df)
df.to_json("kapucinus.json")
