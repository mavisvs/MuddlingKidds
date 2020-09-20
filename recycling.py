#how many recycling centers within 10 miles are at some zipcode
from urllib.request import urlopen
import re
from flask import Flask, render_template, request
zipcode = ""
app = Flask(__name__)

ourUrl = "https://search.earth911.com/?what=CFLs%2C+desktop+computers%2C+cell+phones%2C+etc...&where="

@app.route('/results', methods=["POST"])
def getZip():
    global zipcode
    zipcode = request.forms.get('zip')
ourUrl += zipcode
#TODO: Switch to an actual variable
ourUrl += "&list_filter=all&max_distance=10&family_id=&latitude=&longitude=&country=&province=&city=&sponsor="

pageRecycle = urlopen(ourUrl) #returns an HTTPResponse object
html_bytes = pageRecycle.read()
html = html_bytes.decode("utf-8")

numResults = html.count("result-item")
print(numResults)
