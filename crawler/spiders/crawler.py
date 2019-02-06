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
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "input_domain_urls.txt")

    with open(file_path, "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    allowed_domains =[]
    for each_url in start_urls:
        extracted_domain = tldextract.extract(each_url)
        # extracts example.com -> www.example.com
        allowed_domains.append(extracted_domain.domain + "." + extracted_domain.suffix)


    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        url = str(response.url)
        if self.is_valid(url):
            with open("file.txt", "a") as infile:
                infile.write(url + '\n')

    def is_valid(self, url):
        if any(char in self.invalid_chars_set for char in url):
            return False

        return True
