#!/usr/bin/env python3

import os
import sys
import requests
import time
import bs4
from bs4 import BeautifulSoup

def notify(title, message):
    t = '-title {!r}'.format(title)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t])))

def get_html(url):
    headers = {
        'Host':             'www.amd.com',
        'User-Agent':       'Mozilla/5.0 (X11; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'Accept':           'text/html,application/xhtml+xml,application/xml',
        'Accept-Language':  'en',
        'Accept-Encoding':  'gzip, deflate',
        'Set-Cookie':       'pmuser_country=it;'
    }

    r = requests.get(url, headers=headers, timeout=5)
    r.raise_for_status()
    
    return r

def checkIfAvailable(body):
    soup = BeautifulSoup(body, "lxml")
    oos = soup.find('p', class_='product-out-of-stock')
    if ADD_TO_CART in body:
        notify('GPU Available', name)
        os.system("open {url}")
        return True
    return False

AMD_RX6800XT = "RX6800XT"
AMD_RX6800XT_BLACK = "RX6800XT BLACK"
AMD_RX6700XT = "RX6700XT"

URL_AMD_RX6800XT = "https://www.amd.com/en/direct-buy/5458374100/it"
URL_AMD_RX6800XT_BLACK = "https://www.amd.com/en/direct-buy/5496921500/it"
URL_AMD_RX6700XT = "https://www.amd.com/en/direct-buy/5496921400/it"

STOCKS_URL = { AMD_RX6800XT: URL_AMD_RX6800XT, AMD_RX6800XT_BLACK: URL_AMD_RX6800XT_BLACK, AMD_RX6700XT: URL_AMD_RX6700XT }

OUT_OF_STOCK = "Out of stock"
ADD_TO_CART = "Add to cart"

def main():
    while True:
        for name, url in STOCKS_URL.items():
            print("CHECK", name)
            body = ""
            try:
                body = get_html(url).text
            except requests.exceptions.HTTPError as e:
                print(e)
                print("CHECK", name, "FAILED")
            checkIfAvailable(body)
        time.sleep(60)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)