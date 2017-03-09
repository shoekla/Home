import urllib2
import re
import nltk
import csv
import time
import requests
import string
from bs4 import BeautifulSoup
from urllib2 import urlopen
import os
from twilio.rest import TwilioRestClient 
import webbrowser
import pyrebase

config = {
  "apiKey": "AIzaSyBrINRcTraKgd5WHzwV1X3PflNmeG9eQYQ",
  "authDomain": "abir-stuff.firebaseapp.com",
  "databaseURL": "https://abir-stuff.firebaseio.com",
  "storageBucket": "abir-stuff.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
def getMovieName():
	movie = db.child("movies").get()
	s = str(movie.val())
	if s.startswith("OrderedDict") == False:
		return s
	name = s[s.find("'",s.find(","))+1:s.find("'",s.find("'",s.find(","))+1)]
	return name

def openInWeb(url):
	print "In ethod"
	# Open URL in new window, raising the window if possible.
	webbrowser.open_new(url)


def getMovieDownloadLink(name):
	url = "https://thepiratebay.org/search/"+str(name)+"/"
	source_code=requests.get(url)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
	for link in soup.findAll('a'):

		href=link.get('href')
		href_test=str(href)
		if href_test.startswith("magnet:?"):
			openInWeb(href_test)
			return




 
# put your own credentials here 
ACCOUNT_SID = "ACa4c3ccef1ad1756610b63eac37ffa0ce" 
AUTH_TOKEN = "879040038e39074537d376416659b1e6" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

while True:
	mov = getMovieName()
	db.child("movies").set("")


	if mov != "None" and mov != "":
		arr = mov.split(",")
		#print arr[0]
		for movie in arr:
			getMovieDownloadLink(movie)
			client.messages.create(
	    to="+17132317925", 
	    from_="+18326481563", 
	    body=str(movie)+" started Downloading!", 
	)
	time.sleep(2)


#getMovieDownloadLink(a)


















#openInWeb(a)