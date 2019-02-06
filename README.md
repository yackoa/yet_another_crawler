# The crawler
Hello there!

## Installation
1. Download the project
2. Extract to a folder and navigat to the location
3. install dependencies using Run `pip install -r  requirements.txt` to install dependencies


Recommended to activate virtual env before installing the dependencies.
The project uses `scrapy` for the crawling and another library `tldextract` for working with domain names


## How to run ?
Use the following command to run
`scrapy runspider crawler/spiders/crawler.py -a urlList="path/to/input/domain_list.txt"`


For example : `scrapy runspider crawler/spiders/crawler.py -a urlList="/home/user_name/PycharmProjects/test/yet_another_crawler/input_domain_urls.txt"`


## TODO
* get tests working, offline testing of response isn't working (sorry for that). Lost a lot of time trying


## Hasta la vista, baby.
![mic drop](mic_drop.gif)
