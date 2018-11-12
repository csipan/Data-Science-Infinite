from Starcraft.items import StarcraftItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import html


class StarcraftSpider(CrawlSpider):
    name = "starcraft"
    start_urls = ["http://www.nemzetisport.hu"]
    rules = [
        Rule(
            LinkExtractor(
                allow_domains=["nemzetisport.hu"],
                allow=['.*'],
            ),
            callback='parse_unit',
            follow=True
        )
    ]

    def parse_unit(self, response):
        doc = html.fromstring(response.text)
        iterm_to_ret = StarcraftItem()
        iterm_to_ret["url"] = response.url
        iterm_to_ret["header"] = doc.xpath("//h1")[0].text
        paragraphs = doc.xpath("//div[contains(@class, 'cikkbody clearfix')]//p")
        text_all = ''
        for par in paragraphs:
            if par.text is not None and par.text is not "":
                text_all += str(par.text)
        iterm_to_ret["content"] = text_all
        if iterm_to_ret["content"] is not "":
            yield iterm_to_ret
