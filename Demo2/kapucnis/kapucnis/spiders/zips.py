import scrapy


class ZipsCrawler(scrapy.Spider):
    name = "zips"

    start_urls = ["http://zips.hu/inni/"]

    def parse(self, response):
        beer_names = response.css("div.zBeersItemName::text").extract()
        beer_types = response.css("div.zBeersItemType::text").extract()
        alcohol_vol = response.css("div.zBeersItemVol::text").extract()
        bitterness = response.css("div.zBeersItemIbu::text").extract()
        ebc = response.css("div.zBeersItemEbc::text").extract()
        description = response.css("div.zBeersItemDescription::text").extract()
        group_type = response.css("div.zBeersItemGroupTitle::text").extract()

        for i in range(len(beer_names)):
            item = {}
            item["beer_name"] = beer_names[i]
            item["beer_type"] = beer_types[i]
            item["alcohol_vol"] = float(alcohol_vol[i].replace("%", ""))
            item["bitterness"] = int(bitterness[i])
            item["ebc"] = ebc[i]
            item["description"] = description[i]
            item["group_type"] = group_type[i]
            yield {
                item
            }
