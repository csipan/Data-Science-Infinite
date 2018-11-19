from selenium import webdriver
import pymongo


MONGO_URI = 'mongodb://ec2-35-158-191-40.eu-central-1.compute.amazonaws.com:27017/'
MONGO_DATABASE = 'beer'

client = pymongo.MongoClient(MONGO_URI)

database = client[MONGO_DATABASE]

driver = webdriver.Chrome()
driver.get("http://kapucinus-sor.hu/termekeink/")
assert "Kapucinus Sörfőzde" in driver.title


beer_names = driver.find_elements_by_tag_name("h2")
alcohols_ballings = driver.find_elements_by_css_selector('ul.info li em')
types_ingreds_descripts = driver.find_elements_by_css_selector("ul.description li")

types_ingreds_descripts = [element.text.replace("A balatonszárszói Lutherfesztivál részére gyártva", "").replace
                           ("A Kapucinus Sörfőzde ELSŐ felsőerjesztésű söre!", "")
                           for element in types_ingreds_descripts]

all_beers = []

for i in range(len(beer_names)):
    item = {}
    item["beer_name"] = beer_names[i].text
    item["alcohol_vol"] = alcohols_ballings[i * 2].text
    # item["balling"] = alcohols_ballings[i * 2 + 1].text
    if types_ingreds_descripts[i] and i == 10:
        item["beer_type"] = types_ingreds_descripts[i * 3 + 1]
        item["ingredients"] = types_ingreds_descripts[i * 3 + 2]
        item["description"] = types_ingreds_descripts[i * 3 + 3]
    elif types_ingreds_descripts[i] and i == 11:
        item["beer_type"] = types_ingreds_descripts[i * 3 + 2]
        item["ingredients"] = types_ingreds_descripts[i * 3 + 3]
    elif types_ingreds_descripts[i] and i == 12:
        item["beer_type"] = types_ingreds_descripts[i * 3 + 1]
        item["ingredients"] = types_ingreds_descripts[i * 3 + 2]
    else:
        item["beer_type"] = types_ingreds_descripts[i * 3]
        item["ingredients"] = types_ingreds_descripts[i * 3 + 1]
        item["description"] = types_ingreds_descripts[i * 3 + 2]
    database["scrapy_items"].insert_one(item)

client.close()
driver.close()
