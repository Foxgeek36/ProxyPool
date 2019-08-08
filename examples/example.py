# coding=utf-8
import os
import sys
import requests
from bs4 import BeautifulSoup

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dir)


# get proxy from WebApi
def get_proxy():
    try:
        # proxy-API
        # the right interface->http://127.0.0.1:5000/random +--
        r = requests.get('http://127.0.0.1:5000/get')
        if r.status_code == 200:
            # attention this way +--
            proxy = BeautifulSoup(r.text, "lxml").get_text()
            return proxy
    except ConnectionError:
        return None


# test the proxxy
def crawl(url, proxy):
    proxies = {
        'http': 'http://' + proxy,
        'https':  'https://' + proxy
    }
    try:
        # url='http://httpbin.org/get'
        r = requests.get(url, proxies=proxies)
        # print(r.text)
        return r.text
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)


def main():
    proxy = get_proxy()
    html = crawl('http://docs.jinkan.org/docs/flask/', proxy)
    print(html)

if __name__ == '__main__':
    main()

