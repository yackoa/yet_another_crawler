
import os

from scrapy.http import Response, Request
from urllib import parse as urlparse


def fake_response_from_file(file_name, url=None):
    """
    Create a Scrapy fake HTTP response from a HTML file
    @param file_name: The relative filename from the responses directory,
                      but absolute paths are also accepted.
    @param url: The URL of the response.
    returns: A scrapy HTTP response which can be used for unittesting.
    """
    print(file_name)
    print(url)
    print("*****")
    if not url:
        url = 'http://www.example.com'
    print(url)
    #request = Request(url=urlparse.urljoin(Response.url, url))
    request = Request(url=url)
    if not file_name[0] == '/':
        responses_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(responses_dir, file_name)
    else:
        file_path = file_name

    file_content = open(file_path, 'r').read()

    response = Response(url=url,request=request,body=file_content)
    #response.encoding = 'utf-8'
    return response
