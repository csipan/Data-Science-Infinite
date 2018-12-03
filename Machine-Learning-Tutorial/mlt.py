import pandas as pd
import quandl

pd.set_option("display.width", None)
df = quandl.get("WIKI/GOOGL")
df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]
df["High-Low Percentage"] = (df["Adj. High"] - df["Adj. Close"]) / df["Adj. Close"] * 100.0
df["Percentage Change"] = (df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"] * 100.0
df = df[["Adj. Close", "High-Low Percentage", "Percentage Change", "Adj. Volume"]]
print(df.head())
