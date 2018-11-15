from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import html
from conifers.items import ConifersItem


class ConiferSpider(CrawlSpider):
    name = "conifers"
    start_urls = ["https://www.greatplantpicks.org/plantlists/by_plant_type/conifer"]
    rules = [
      Rule(
        LinkExtractor(
          allow_domains=["greatplantpicks.org"],
          allow=[".*"],
        ),
        callback="parse",
        follow=True
      )
    ]

    def parse(self, response):
        doc = html.fromstring(response.text)
        item = ConifersItem()
        item["common_name"] = doc.xpath("//tbody/tr/td[contains(@class, 'common_name')]/p").text()
        item["latin_name"] = doc.xpath("//tobdy/tr/td[contains(@class, 'plantname')]/a/"
                                       "span[contains(@class, 'genus', 'species')].text()")
        yield item
