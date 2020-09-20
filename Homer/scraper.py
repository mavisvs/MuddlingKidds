
##First part of the scraping
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests

#FLOODING WEBSITE INFO
urlFlooding = "https://coast.noaa.gov/slr/#/layer/sce/0/-11581024.663779823/5095888.569004184/4/satellite/88/0.8/2050/interHigh/midAccretion"
pageFlood = urlopen(urlFlooding) #returns an HTTPResponse object
html_bytes = pageFlood.read()
html = html_bytes.decode("utf-8")

#TOXIC WASTE WEBSITE INFO
urlToxic = ""

# re.findall("ab*c", "abcd")

def scrape_conversionWebsite(zipcode):
    # pageFlood = urlopen("https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude/table/?q=" + zipcode)
    # tml_bytes = pageFlood.read()
    # html = html_bytes.decode("utf-8")
    page = requests.get("https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude/table/?q=" + zipcode)
    html = BeautifulSoup(page.content, 'html.parser')
    # print(html)
    # print(re.findall("<span", html))
    options = html.find_all('span', string=lambda text: bool(re.match("^[-+]?\d+(\.\d+)?$", str(text))))
    print(options)

scrape_conversionWebsite("94602")