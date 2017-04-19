from bs4 import BeautifulSoup
import requests, sys
from tkinter import *
from tkinter import messagebox

BASE_URL = 'https://google.com/search?q='

def makeRequest(word):
	url = BASE_URL + word + '+meaning'
	r = requests.get(url)
	return r.content

def getMeaning(content):
	means = []
	soup = BeautifulSoup(content,'lxml')
	for table in soup.find_all('table'):
		if(table.get('style') == 'font-size:14px;width:100%'):
			for meaning in table.tr.td.ol.children:
				means.append(meaning.string)
	return means

def showMeaning():
	t = Tk()
	t.withdraw()
	text = t.clipboard_get()
	while True:
		while text == t.clipboard_get():
			pass
		content = makeRequest(t.clipboard_get())
		meaning = getMeaning(content)
		messagebox.showinfo('Meaning',meaning)
		text = t.clipboard_get()

if __name__=='__main__':
	try:
		showMeaning()
	except KeyboardInterrupt:
		print("Bye")
		sys.exit(0)