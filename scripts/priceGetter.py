#! /usr/bin/env python3

# Description:
#   looks up the price of a specified item at the shopping platform bol.com
#   and returns it as clear text.
#
# Idea for further usage:
#   could be used for automated price-comparison for specific items over a longer period
#
# Usage:
#   - edit the link to the bol-item-page
#   - python3 priceGetter.py
#
# Author: samari-k
# Version: 1.0

import bs4, requests

URL = 'https://www.bol.com/nl/p/hands-on-machine-learning-with-scikit-learn-keras-and-tensorflow/9200000094568602/'


def getBolPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('.promo-price')
    price = elems[0].text.strip().replace('\n  ', '.') + '€'

    return price


price = getBolPrice(URL)
print('The price is: ' + price)
