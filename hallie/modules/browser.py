#!/usr/bin/env python
import webbrowser
import speech

def lookupSite(site):
	givenSites = {
		"google": "http://google.com",
		"overflow": "http://stackoverflow.com",
		"gmail": "http://inbox.google.com",
		"inbox": "http://inbox.google.com",
		"github": "http://github.com",
		"facebook": "http://facebook.com",
		"twitter": "http://twitter.com",
		"apple": "http://apple.com",
		"google": "http://google.com",
		"ebay": "http://ebay.com",
		"reddit": "http://reddit.com",
		"netflix": "http://netflix.com",
	}
	if site in givenSites:
		return givenSites[site]
	
	if "http://" not in site:
		site = "http://" + site
	if "." not in site:
		site += ".com"

	return site

def openSite(site):
	"""Opens a given site in the user's default browser"""
	speech.speak("Opening " + site + " in your default browser.\n")
	webbrowser.open(lookupSite(site))
