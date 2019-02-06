#!/usr/bin/env python
"""  Lists the basic settings which is configured  for our spider

For details on each parameter referer :
https://doc.scrapy.org/en/latest/topics/settings.html
"""



BOT_NAME = 'test'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True


FILENAME_EXT = ".out"

