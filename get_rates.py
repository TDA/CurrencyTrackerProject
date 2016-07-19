__author__ = 'saipc'
import requests
from bs4 import BeautifulSoup
import datetime

def get_current_rate(a, b):
    default_amount = 1
    url = "http://www.google.com/finance/converter?a=%s&from=%s&to=%s"%(default_amount, a, b)
    print "Requesting conversion rate for %s to %s"%(a, b)
    r = requests.get(url)
    currency_string = get_text(r.text, "#currency_converter_result > span")
    currency_amount = float(str(currency_string).split(' ')[0])
    return currency_amount

def get_text(html, selector):
    s = BeautifulSoup(html, "lxml")
    currency_string = s.select(selector)[0].get_text()
    return currency_string

def get_wire_rate(url):
    r = requests.get(url)
    currency_string = get_text(r.text, ".xcma-fx-rate > .fx-rate")
    currency_amount = float(str(currency_string).split('=')[1].split(' ')[1])
    return currency_amount

if __name__ == '__main__':
    a = 'usd'
    b = 'inr'
    currency_amount = get_current_rate(a, b)
    wire_amount = get_wire_rate('https://www.xoom.com/india/send-money')
    delta = currency_amount - wire_amount
    time = datetime.date
    op_string = "%s : %s\n" % (time.today().strftime("%d %B, %Y"), delta)
    with open('deltas', 'a') as f:
        f.write(op_string)
        f.write("Today's currency rate: %s to %s is %s\n" % (a, b, currency_amount))
        f.write("Today's xoom rate: %s\n" % wire_amount)

