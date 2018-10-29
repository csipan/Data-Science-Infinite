import pandas as pd
import numpy as np

df = pd.read_csv("googleplaystore.csv")
apps_by_reviews = df.sort_values("Reviews")
print(apps_by_reviews["App"])
# print(df["App", "Reviews"][df["Reviews"] == 995002])
# print(df["Rating"].max)

