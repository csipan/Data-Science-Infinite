# -- coding: UTF-8 --
import pandas as pd
import numpy as np


# Make a Kaggle account and download the Google Play Store Apps Dataset: https://www.kaggle.com/lava18/google-play-store-apps
# Which app has the lowest number of reviews?
# What is the average, median and mode of the App ratings (Rating column)?
# What is the estimated average/median/mode file size?
# What are the most popular genres?
# Convert the Last Updated column to YYYYY-MM-DD format and insert it as an extra column next to Last Updated, with the name "Last Updated Readable" and save it as a new, separate CSV file.
# Create a new, separate CSV that has all rows of data in reverse.

# Formatting the text
def header(msg):
    print('-' * 50)
    print('[ ' + msg + ']')


# Import csv file
header("1. Read csv file")
# Data appearance format
pd.set_option('display.width', None)
# pd.set_option('display.max_rows', 15000)
filename = "googleplaystore.csv"
df = pd.read_csv(filename)
# print(df.shape)
# df.info()

# Which app has the lowest number of reviews?
header("2. Lowest number of reviews")
# First checking which is the lowest review
# print(df.sort_values("Reviews", ascending=True))
# After finding out that 0 is the lowest review, I am printing out this ones
# print(df[df.Reviews == 0].head())
# print(df.sort_values("Category", ascending=True))

header("3. Rename columns")
# Renaming columns for queries like below
# print(df.sort_values("Content Rating", ascending=True))
# print(df[df.Content_Rating == "Unrated"].head())
print(df.columns)
df.rename(columns = {"Content Rating": "Content_Rating", "Last Updated": "Last_Updated", "Current Ver": "Current_Ver", "Android Ver": "Android_Ver"}, inplace=True)
print(df.columns)

header("4. The average, median and mode of the App Ratings")
# First of all we have to handle the duplicates
df = df.drop_duplicates("App", keep="first")
# print(df.shape)
print(df["Rating"].describe().apply(lambda x: '%.3f' % x))  # f - float number
print(df["Rating"].mean())
print(df.Rating.median())
print(df["Rating"].mode())

header("5. Estimated average/median/mode for Size")
# First we have to convert the type of Size column from object to float
print(df["Size"].dtypes)
# print(df["Size"].str.replace("Varies with device", "NaN"))

# Separating everything from Size column except the last character
df["Size_Numeric_Part"] = [x[:-1] for x in df["Size"]]
df["Size_Numeric_Part"] = df["Size_Numeric_Part"].str.replace("Varies with devic", "NaN")
print(df["Size_Numeric_Part"].tail())

# Separating the last character from Size column
df["Size_Letter_Part"] = df["Size"].str.replace("k", 1024)
df["Size_Letter_Part"] = df["Size"].str.replace("M", 1048576)