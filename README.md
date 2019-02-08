# The crawler
This is a crawler written in [Scrapy](https://github.com/scrapy/scrapy) to crawl a site without a using sitemap. It recursively crawls the entire site within its domain ignoring the offsite requests. The crawling is throttled using the autothrottle feature of Scrapy to limit a maximum of two requests every two seconds. It creates an output file in this [format](https://github.com/yackoa/yet_another_crawler#output-file)

[Scrapy's](https://github.com/scrapy/scrapy) documentation is available [here](https://docs.scrapy.org/en/latest/)

Contributers welcome.

## Installation
1. Download the project
2. Extract to a folder and navigat to the location
3. install dependencies using Run `pip install -r  requirements.txt` to install dependencies


Recommended to activate virtual env before installing the dependencies.
The project uses `scrapy` for the crawling and another library `tldextract` for working with domain names


## How to run ?
Use the following command to run

`scrapy runspider crawler/spiders/crawler.py -a urlList="path/to/input/domain_list.txt"`

**Summing up**

Assuming you have git installed in your system & `input_domain_urls.txt` contains say `https://www.example.com`
```
mkdir test ; cd test
git clone https://github.com/yackoa/yet_another_crawler.git .
virtualenv env
source env/bin/activate
pip install -r requirements.txt

scrapy runspider crawler/spiders/crawler.py -a urlList="input_domain_urls.txt"
```

## Output file
Say if the domain name was `example.com` then the output file name will be `example.com.txt`
```
https://www.example.com
https://www.example.com/product/123
https://www.example.com/page/about-us
[...]
```
## TODO
* Get tests working. Lost a lot of time trying betamax, fake_offline_requests. I am willing to learn, could you teach me to test the crawlSpider in Scrapy ?


## Hasta la vista, baby.
![mic drop](mic_drop.gif)
