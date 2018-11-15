import scrapy


class HorizontsorokCrawler(scrapy.Spider):
    name = "horizont"
    start_urls = [
        "http://www.horizontsorok.hu/"
    ]

    def parse(self, response):
        beer_names = response.css("h3.s-component-content p::text").extract()
        beer_types = response.css("div.s-component-content.s-font-body p::text").extract()
        print(beer_names)
