#! /usr/bin/python3

# Description:
#   This is to try out the functionality of the selenium module.
#   It opens a Firefox webbrowser and surfs to the shopping page bol.com,
#   where it searches for a specified  word or phrase

# Usage:
#   geckodriver needs to be found in PATH
#       --> https://github.com/mozilla/geckodriver/releases/tag/v0.29.0
#   >> ./seleniumDemo.py searchstring

import sys
from selenium import webdriver

if len(sys.argv)>1:
    searchFor = ' '.join(sys.argv[1:])
else:
    searchFor = 'Katzenfutter'

browser = webdriver.Firefox()
browser.get('https://www.bol.com')

elem = browser.find_element_by_css_selector('.js-decline-button > span:nth-child(1)')
elem.click()

elem = browser.find_element_by_css_selector('.modal__window__content > div:nth-child(1) > wsp-toggle-visibility:nth-child(1) > div:nth-child(4) > div:nth-child(2) > wsp-switch-country:nth-child(1) > a:nth-child(1)')
elem.click()

elem = browser.find_element_by_css_selector('#searchfor')
elem.send_keys(searchFor)
elem.submit()