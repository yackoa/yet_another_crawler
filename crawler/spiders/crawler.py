#!/usr/bin/env python
"""  This is the basic spider crawler code

"""
import os
import tldextract
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.project import get_project_settings
from scrapy import signals


class MySpider(CrawlSpider):
    name = "test_spider"
    invalid_chars_set = ["#", "?"]
    # See https://doc.scrapy.org/en/latest/topics/autothrottle.html
    # See https://docs.scrapy.org/en/latest/topics/settings.html
    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'AUTOTHROTTLE_ENABLED': True,
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 2

    }

    def __init__(self, urlList='', *args, **kwargs):  #
        self.custom_settings = get_project_settings()
        self.start_urls = self.get_start_urls(urlList)
        self.allowed_domains = self.get_allowed_domains()

        self.rules = (Rule(LinkExtractor(), callback='parse_item', follow=True),)
        super().__init__(__rules=self.rules)

        self.output_file = str(self.allowed_domains[0]) + ".txt"

    def get_start_urls(self, url_file):
        """ reads the input file containing list of URLs and returns list of start urls

        :param url_file:str
            This is the file name
        :return: [start_urls]
            Returns return_list of start_urls

        Example:
            >>> get_start_urls([path_to_file])
            ['https://www.example.com']
        """

        with open(url_file, "rt") as f:
            start_urls = [url.strip() for url in f.readlines()]

        return start_urls

    def get_allowed_domains(self):
        """" takes the list of start urls and returns the allowed domain list
        :param None
        :return: [allowed_domains]
            Returns a returns list of allowed_domains


        Example:
            >>> get_start_urls(['https://www.example.com'])
            ['example.com]
        """
        allowed_domains = []
        for each_url in self.start_urls:
            extracted_domain = tldextract.extract(each_url)
            # extracts example.com from www.example.com
            allowed_domains.append(extracted_domain.domain + "." + extracted_domain.suffix)
        return allowed_domains

    def parse_item(self, response):
        """ Takes each response asyncornosly from the crawler and appends to the file

        :param response: response
        :return: None
        """
        url = str(response.url)
        if self.is_valid(url):
            with open(self.output_file, "a") as infile:
                infile.write(url + '\n')

    def is_valid(self, url):
        """ Checks to see if the URl doesn't have invalid characters mentioned in the charset

        :param url: str
        :return: Boolean

        Example:
            >>> get_start_urls(['https://www.example.com/share?=1'])
            False
            >>> get_start_urls(['https://www.example.com/some_page.html'])
            True
        """
        if any(char in self.invalid_chars_set for char in url):
            return False

        return True

