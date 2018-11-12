import scrapy
from scrapy import spider


class ConiferSpider(spider.scrapy):
    name = "conifers"
    allowed_domain = ["greatplantpicks.org"]
    start_urls = ["https://www.greatplantpicks.org/plantlists/by_plant_type/conifer"]

    def parse(self, response):
        filename = response.url.split("/")[-2] + ".html"
        # filename = 'conifer-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        # self.log('Saved file %s' % filename)
