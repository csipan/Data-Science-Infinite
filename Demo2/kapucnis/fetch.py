from pymongo import MongoClient
import pandas as pd


client = MongoClient(
    'ec2-35-158-191-40.eu-central-1.compute.amazonaws.com', 27017)

pd.set_option("display.width", None)


def dump_into_df(db_name):
    db = client[db_name]
    collection = db.scrapy_items
    return pd.DataFrame(list(collection.find({})))


df = dump_into_df("newbeer")
print(df)
