from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item

class AnjukeSpider(BaseSpider) :
    name = "anjuke"
    allowed_domains = ["hangzhou.anjuke.com"]
    start_urls = [
        "http://hangzhou.anjuke.com/"
    ]

    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        areas = hxs.select("//div[@id='content_Rd1']/div/div[2]/div[@class='areas']/a/@href").extract()
        for area in areas :
            print area