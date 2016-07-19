__author__ = 'saipc'
import requests

def get_current_rate(a, b):
    url = "http://www.google.com/finance/converter?a=%s&from=%s&to=%s"
    default_amount = 1
    print "Requesting conversion rate for "
    r = requests.get(url%(default_amount, a, b))
    print r

if __name__ == '__main__':
    get_current_rate('usd', 'inr')