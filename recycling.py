#how many recycling centers within 10 miles are at some zipcode
from urllib.request import urlopen
import re
import Homer 
ourUrl = "https://search.earth911.com/?what=CFLs%2C+desktop+computers%2C+cell+phones%2C+etc...&where="
zipcode = Homer.getZip()

#@app.route('/results', methods=["POST"])
#def getZip():
 #   global zipcode
  #  zipcode = request.forms.get('zip')
ourUrl += zipcode
#TODO: Switch to an actual variable
ourUrl += "&list_filter=all&max_distance=10&family_id=&latitude=&longitude=&country=&province=&city=&sponsor="

pageRecycle = urlopen(ourUrl) #returns an HTTPResponse object
html_bytes = pageRecycle.read()
html = html_bytes.decode("utf-8")

numResults = html.count("result-item")
#TODO: make this thing pop up on webpage print("This zipcode has at least " + numResults + " recycling centers")
