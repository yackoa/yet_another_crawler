#!/usr/bin/env python

""" Tests go here

"""
import os
import unittest
from crawler.spiders.re_crawler import MySpider
from tests.responses import fake_response_from_file as fake
from scrapy.selector import Selector


class CrawlSpiderTest(unittest.TestCase):

    def setUp(self):
        self.url = "responses/osdir/index.html"
        self.responses_dir = os.path.dirname(os.path.realpath(__file__))
        self.file_path = os.path.join(self.responses_dir, self.url)
        self.fake_response = Selector(text=open(self.file_path, 'r').read())
        self.spider = MySpider(_follow_links=True)

    def test_parse(self):
        from scrapy.http import Response, request
        response = Response(url=self.url,
                            request=request,
                            body=str.encode(self.file_path))

        results = self.spider.parse(response)
        print(list(results))
