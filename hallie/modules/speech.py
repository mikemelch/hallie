#!/usr/bin/env python

prefix = "hallie> "

def speak(words):
	print prefix + words

def emptyCommand():
	print prefix + "Sorry, I don't understand!\n" + prefix + "Tell me something to do, like 'hallie show me the current files'"
