import scrapy


class HorizontsorokCrawler(scrapy.Spider):
    name = "horizont"
    start_urls = [
        "http://www.horizontsorok.hu/"
    ]

    def parse(self, response):
        beer_names = response.css("div.container div.s-repeatable-item div.s-item-title div.s-text")
        for item in beer_names:
            print(item.extract())
        # beer_types = response.css("div.s-component-content.s-font-body p::text").extract()
        # print(beer_names)

        # beer_names_test = response.xpath("//h3[contains(@class, 's-component-content') and contains(@class, 's-font-heading')]/p/text()").extract_first()
        # # print(beer_types)
        # print(beer_names)
        # print(beer_names_test)



