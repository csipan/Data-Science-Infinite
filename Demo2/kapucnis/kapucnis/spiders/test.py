from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://kapucinus-sor.hu/termekeink/")
assert "Kapucinus Sörfőzde" in driver.title


beer_names = driver.find_elements_by_tag_name("h2")
alcohols_ballings = driver.find_elements_by_css_selector('ul.info li em')
types_ingreds_descripts = driver.find_elements_by_css_selector("ul.description li")
print(len(beer_names))
print(len(alcohols_ballings))
print(len(types_ingreds_descripts))

all_beers = []

for i in range(len(beer_names)):
    item = {}
    item["beer_name"] = beer_names[i].text
    item["beer_type"] = types_ingreds_descripts[i][0].text
    item["alcohol_vol"] = alcohols_ballings[i][0].text
    all_beers.append(item)
print(all_beers[1])

alcohols_ballings_len = len(alcohols_ballings)
for alcohol_balling in range(0, alcohols_ballings_len, 1):
    if alcohols_ballings_len % 2 == 0:
        alcohol = alcohols_ballings[alcohol_balling].text
        # print(alcohol)
    else:
        balling = alcohols_ballings[alcohol_balling].text
        # print(balling)

types_ingreds_descripts_len = len(types_ingreds_descripts)
for type_ingred_desc in range(0, types_ingreds_descripts_len, 1):
    if types_ingreds_descripts_len % 3 == 0:
        beer_type = types_ingreds_descripts[type_ingred_desc].text
        # print(beer_type)
    if (types_ingreds_descripts_len - 1) % 3 == 0:
        ingredients = types_ingreds_descripts[type_ingred_desc].text
        # print(ingredients)
    else:
        description = types_ingreds_descripts[type_ingred_desc].text
        # print(description)

driver.close()
