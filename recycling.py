#how many recycling centers within 10 miles are at some zipcode
"""
from urllib.request import urlopen
import re
import Homer 
zipcode = Homer.getZip()

lithiumUrl = "https://search.earth911.com/?what=Lithium-ion+Batteries&where="
lithiumUrl += zipcode
#TODO: Switch to an actual variable
lithiumUrl += "&list_filter=all&max_distance=5&family_id=&latitude=&longitude=&country=&province=&city=&sponsor="
bottleUrl = "https://search.earth911.com/?what=%233+Plastic+Bottles&where=" + zipcode + "&list_filter=all&max_distance=5&family_id=&latitude=&longitude=&country=&province=&city=&sponsor="
leadUrl = "https://search.earth911.com/?what=Lead-acid+Batteries+-+Non-automotive&where=" + zipcode + "&list_filter=all&max_distance=5&family_id=&latitude=&longitude=&country=&province=&city=&sponsor=" 

def numOfCents(url): #function takes in url and gives out least number of places within 5 mile radius
  pageRecycle = urlopen(url) #returns an HTTPResponse object
  html_bytes = pageRecycle.read()
  html = html_bytes.decode("utf-8")
  numResults = html.count("result-item")
  return numResults

def allNearbyCents():
  lithiumMin = numOfCents(lithiumUrl)
  bottleMin = numOfCents(bottleUrl)
  leadMin = numOfCents(leadUrl)
  recyclePlants = {"Lithium Ion Battery Return Centers": lithiumMin, "Plastic Bottle Recycling Centers": bottleMin, "Lead Battery Return Locations": leadMin}
  return recyclePlants
#TODO: make this thing pop up on webpage print("This zipcode has at least " + numResults + " recycling centers")

#first thing - lithium ion battery centers, second - plastic bottles, lead batteries
"""