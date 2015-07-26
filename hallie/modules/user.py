#!/usr/bin/env python
from requests import get
from socket import gethostbyname, gethostname
import speech
import pickle
import settings
import os
import subprocess

CHANGE_DIR = """tell application "Terminal" 
activate 
do script ("cd %s") in window 1
end tell"""

def getPublicIPAddress():
	"""gets the user's public IP address"""
	speech.speak("Retrieving your public IP address. Please wait a moment.")
	ip = get('http://api.ipify.org').text
	speech.speak("Your public IP address is: " + ip)

def getLocalIPAddress():
	"""gets the user's local IP address"""
	ip = gethostbyname(gethostname())
	speech.speak("Your local IP address is: " + ip)

def saveDirectory(alias):
	"""save a directory to a certain alias/nickname"""
	if not settings.platformCompatible():
		return False
	dataFile = open(settings.getDataFile(), "wb")
	currentDirectory = os.path.abspath(".")
	directory = {alias : currentDirectory}
	pickle.dump(directory, dataFile)
	speech.success(alias + " will now link to " + currentDirectory + ".")
	speech.success("Tip: use 'hallie go to " + alias + "' to change to this directory.")

def goToDirectory(alias):
	"""go to a saved directory"""
	if not settings.platformCompatible():
		return False
	data = pickle.load(open(settings.getDataFile(), "rb"))
	try:
		data[alias]
	except KeyError:
		speech.fail("Sorry, it doesn't look like you have saved " + alias + " yet.")
		speech.fail("Go to the directory you'd like to save and type 'hallie save as " + alias + "\'")
		return
	try:
		(output, error) = subprocess.Popen(["osascript", "-e", CHANGE_DIR % (data[alias])], stdout=subprocess.PIPE).communicate()
	except:
		speech.fail("Something seems to have gone wrong. Please report this error to michaelmelchione@gmail.com.")
		return
	speech.success("Successfully navigating to " + data[alias])
