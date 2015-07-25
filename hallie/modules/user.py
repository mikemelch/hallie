#!/usr/bin/env python
from requests import get
from socket import gethostbyname, gethostname
import speech

def getPublicIPAddress():
	"""gets the user's public IP address"""
	speech.speak("Retrieving your public IP address. Please wait a moment.")
	ip = get('http://api.ipify.org').text
	speech.speak("Your public IP address is: " + ip)

def getLocalIPAddress():
	"""gets the user's local IP address"""
	ip = gethostbyname(gethostname())
	speech.speak("Your local IP address is: " + ip)

