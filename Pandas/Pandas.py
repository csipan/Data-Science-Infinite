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
# converting to 0 the "Varies with devic"
df["Size_Numeric_Part"] = df["Size_Numeric_Part"].replace("Varies with devic", 0)
df["Size_Numeric_Part"] = df["Size_Numeric_Part"].astype(float)
print(df["Size_Numeric_Part"].dtypes)

# Separating the last character from Size column
df["Size_Last_Character"] = df["Size"].str[-1:]
# print(df["Size_Last_Character"].head())

# Convert "k" and "M" to relevant values
df["Size_Letter_Replace"] = df["Size_Last_Character"].replace("k", 1024)
df["Size_Letter_Replace"] = df["Size_Letter_Replace"].replace("M", 1048576)
df["Size_Letter_Replace"] = df["Size_Letter_Replace"].replace("e", 0)
df["Size_Letter_Replace"] = df["Size_Letter_Replace"].astype(float)

# Finally adding up the separated parts to one number
df["Size"] = df["Size_Numeric_Part"] * df["Size_Letter_Replace"]
# Replacing the 0 which was "Varies with device" to "NaN" to ignore from the calculations
df["Size"] = df["Size"].replace(0.0, np.nan)

print(df["Size"].mean())
print(df["Size"].median())
print(df["Size"].mode())

header("6. Most popular Genres")
print(df.groupby("Genres").size().head())

header("7. Convert the Last Updated column to YYYYY-MM-DD format and insert it as an extra column next to "
       "Last Updated, with the name Last Updated Readable")
df["Last_Updated_Readable"] = pd.to_datetime(df["Last_Updated"]).dt.strftime("%Y/%m/%d")
new_df = df[['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type',
       'Price', 'Content_Rating', 'Genres', 'Last_Updated', 'Last_Updated_Readable', 'Current_Ver',
       'Android_Ver']]
print(new_df.head())
new_df.to_csv("googleplaystore last updated readable.csv")

header("8. Create a new, separate CSV that has all rows of data in reverse.")
reversed_df = new_df.iloc[::-1]
print(reversed_df.head())
reversed_df.to_csv("googleplaystore reversed.csv")
