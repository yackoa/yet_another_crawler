#!/usr/bin/env python
"""  This is the basic spider crawler code

"""
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

DOMAIN = 'example.com'
URL = 'http://%s' % DOMAIN


class MySpider(CrawlSpider):

    name = "test spider"

    start_urls = [
        "http://www.tesco.com"
    ]
    allowed_domains = ["tesco.com"]

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        url = str(response.url)
        print(" url >>>>>>>>>>>> "+url)

        if self.is_valid(url):
            arquivo = open("file.txt", "a")
            arquivo.write(url + '\n')
            arquivo.close

    def is_valid(self, url):

        if "#" in url:
            return False
        if "?" in url:
            return False

        return True
