#!/usr/bin/env python
"""  This is the basic spider crawler code

"""
import os
import tldextract
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MySpider(CrawlSpider):

    name = "test spider"
    invalid_chars_set = ["#", "?"]

    def __init__(self, urlList='',  *args, **kwargs ): #
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, urlList)

        with open(file_path, "rt") as f:
            self.start_urls = [url.strip() for url in f.readlines()]

        self.allowed_domains = []
        for each_url in self.start_urls:
            extracted_domain = tldextract.extract(each_url)
            # extracts example.com from www.example.com
            self.allowed_domains.append(extracted_domain.domain + "." + extracted_domain.suffix)

        self.rules = (Rule(LinkExtractor(), callback='parse_item', follow=True),)
        super().__init__(__rules=self.rules)
        self.output_file = str(extracted_domain.domain) + ".txt"

    def parse_item(self, response):
        url = str(response.url)
        if self.is_valid(url):
            with open(self.output_file, "a") as infile:
                infile.write(url + '\n')

    def is_valid(self, url):
        if any(char in self.invalid_chars_set for char in url):
            return False

        return True
