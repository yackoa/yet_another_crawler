#!/usr/bin/env python

""" Tests go here

"""
import os
import unittest
from crawler.spiders.crawler import MySpider
from tests.responses import fake_response_from_file as fake
from scrapy.selector import Selector

# Test part
from betamax import Betamax
from betamax.fixtures.unittest import BetamaxTestCase
from scrapy.http import HtmlResponse
from crawler.spiders.crawler import MySpider

with Betamax.configure() as config:
    # where betamax will store cassettes (http responses):
    config.cassette_library_dir = '/home/stormfield/PycharmProjects/yet_another_crawler'
    config.preserve_exact_body_bytes = True


class TestExample(BetamaxTestCase):  # superclass provides self.session

    def test_parse(self):
        example = MySpider(urlList='/home/stormfield/PycharmProjects/yet_another_crawler/input_domain_urls.txt')
        example._follow_links =True
        file_= u"/home/stormfield/PycharmProjects/yet_another_crawler/tests/responses/osdir/index.html"
        # http response is recorded in a betamax cassette:
        import requests
        response = self.session.get(requests.build_absolute_uri(file_))

        # forge a scrapy r  esponse to test
        scrapy_response = HtmlResponse(body=response.content, url=file_)

        result = example.parse(scrapy_response)
        for i in result:
            print(str(scrapy_response.url)    )
