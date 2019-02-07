# The crawler
Hello there!

This is a solution to the [interview question](https://github.com/pricesearcher/senior-python-software-developer) by [PriceSearcher](https://www.pricesearcher.com)

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

Assuming you have git installed in your system
```
mkdir test ; cd test
git clone https://github.com/yackoa/yet_another_crawler.git .
virtualenv env
source env/bin/activate
pip install -r requirements.txt

scrapy runspider crawler/spiders/crawler.py -a urlList="input_domain_urls.txt"
```

## TODO
* get tests working, offline testing of response isn't working (sorry for that). Lost a lot of time trying


## Hasta la vista, baby.
![mic drop](mic_drop.gif)
