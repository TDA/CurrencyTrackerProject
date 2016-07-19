__author__ = 'saipc'
import requests
from bs4 import BeautifulSoup

def get_current_rate(a, b):
    default_amount = 1
    url = "http://www.google.com/finance/converter?a=%s&from=%s&to=%s"%(default_amount, a, b)
    print "Requesting conversion rate for %s to %s"%(a, b)
    r = requests.get(url)
    currency_string = get_text(r.text, "#currency_converter_result")
    currency_amount = float(str(currency_string).split(' ')[0])
    return currency_amount

def get_text(html, id_selector):
    s = BeautifulSoup(html, "lxml")
    currency_string = s.select(id_selector + ' > span')[0].get_text()
    return currency_string

if __name__ == '__main__':
    a = 'usd'
    b = 'inr'
    currency_amount = get_current_rate(a, b)
    print "Today's currency rate: %s to %s is %s" % (a, b, currency_amount)