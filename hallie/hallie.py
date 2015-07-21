#!/usr/bin/env python
import sys
import re
import pickle

from modules import *

def parse(command):
	if re.search(r"(show|give|tell|list|print)\s(me|my)*.*\s(files)", command):
		files.printFiles()

	#elif re.match(r"(run.*(as|with)\s(priv.*|super.*|sudo|root|admin.*))|sudo|admin|super.*", command):
		#files.sudo()

	elif re.search(r"(create|make|start|build|construct|prepare|whip).*(directory|folder|catalogue)(\s)(and\s)?(call(ed)?|name(ed)?)(\sit\s)?(?P<name>.*)", command):
		matches = re.search(r"(create|make|start|build|construct|prepare|whip).*(directory|folder|catalogue)(\s)(and\s)?(call(ed)?|name(ed)?)(\sit\s)?(?P<name>.*)", command)
		files.mkdir(matches.group('name').strip())

	elif re.search(r"(((teach|show|how|what|advise|enlighten|give).*(me|does|information|about|how|is|are)\s((\'|\")?(?P<command>\w*)(\'|\")?).*(works?|means?)*\??)|(\w*)\?)", command):
		matches = re.search(r"(((teach|show|how|what|advise|enlighten|give).*(me|does|information|about|how|is|are)\s((\'|\")?(?P<command>\w*)(\'|\")?).*(works?|means?)*\??)|(\w*)\?)", command)
		files.man(matches.group('command').strip())

	elif re.search(r"(unpack\w*|unzip|unload|unarchive|unrar|untar|extract)\s(?P<file>\"?(.)*\"?\.(?P<format>(\w)*))(\s(to|here)\s(?P<location>\"?(.)*\"?))?", command):
		matches = re.search(r"(unpack\w*|unzip|unload|unarchive|unrar|untar|extract)\s(?P<file>\"?.*\"?\.(?P<format>\w*))(\s(to|here)\s(?P<location>\"?.*\"?))?", command)
		files.extract(matches.group('file').strip(), matches.group('format').strip(), matches.group('location'))

	elif re.search(r"copy.*((file|directory|folder)*)?\s(?P<location>\"?(.)*\"?)$", command):
		matches = re.search(r"copy.*((file|directory|folder)*)?\s(?P<location>\"?(.)*\"?)$", command)
		files.copy(matches.group('location'))

	elif re.search(r"(open|navigate to|browse)\s(?P<site>.*)", command):
		matches = re.search(r"(open|navigate to|browse)\s(?P<site>.*)", command)
		browser.openSite(matches.group('site').lower())

	elif re.search(r"play\s(?P<song>(\w|\s)*)\sby\s(?P<artist>(\w|\s)*)\s((off|on|from|album|within|of)\s)+(the\s)?(album\s)?(?P<album>(\w|\s)*)", command):
		"""matches song, artist, and album ex: play runaway by kanye west from my beautiful dark twisted fantasy"""
		matches = re.search(r"play\s(?P<song>(\w|\s)*)\sby\s(?P<artist>(\w|\s)*)\s((off|on|from|album|within|of)\s)+(the\s)?(album\s)?(?P<album>(\w|\s)*)", command)
		itunes.play(matches.group('song'), matches.group('artist'), matches.group('album'))

	elif re.search(r"play\s.*album\s(called\s|named\s)?(?P<album>(\w|\s)*)\sby\s(?P<artist>(\w|\s)*)", command):
		"""matches album ex: play the album born sinner by j. cole"""
		matches = re.search(r"play\s.*album\s(called\s|named\s)?(?P<album>(\w|\s)*)\sby\s(?P<artist>(\w|\s)*)", command)
		itunes.play(None, matches.group('artist'), matches.group('album'))

	elif re.search(r"play\s.*album\s(called\s|named\s)?(?P<album>(\w|\s)*)", command):
		"""matches album ex: play the album born sinner"""
		matches = re.search(r"play\s.*album\s(called\s|named\s)?(?P<album>(\w|\s)*)", command)
		itunes.play(None, None, matches.group('album'))

	elif re.search(r"play\s.*artist\s(called\s|named\s)?(?P<artist>(\w|\s)*)", command):
		"""matches album ex: play the artist kanye west"""
		matches = re.search(r"play\s.*artist\s(called\s|named\s)?(?P<artist>(\w|\s)*)", command)
		itunes.play(None, matches.group('artist'), None)

	elif re.search(r"play\s(?P<song>(\w|\s)*)\sby\s(?P<artist>(\w|\s)*)", command):
		"""matches song and artist ex: play runaway by kanye west"""
		matches = re.search(r"play\s(?P<song>(\w|\s)*)\sby\s(?P<artist>(\w|\s)*)", command)
		itunes.play(matches.group('song'), matches.group('artist'))

	elif re.search(r"play\s(?P<song>(\w|\s)*)", command):
		"""matches song ex: play runaway"""
		matches = re.search(r"play\s(?P<song>(\w|\s)*)", command)
		itunes.play(matches.group('song'))
	
	elif re.search(r"(skip|next\ssong)", command):
		"""skips the current song in itunes"""
		itunes.skip()

	elif re.search(r"(play|resume|unpause)", command):
		"""resumes the current song in itunes"""
		itunes.resume()

	elif re.search(r"(stop|pause)", command):
		"""pauses the current song in itunes"""
		itunes.pause()

	elif re.search(r"paste", command):
		"""paste the current copied file"""
		files.paste()

	else:
		"""hallie doesn't match the command"""
		speech.speak("I'm sorry, I don't understand that command. Try \"hallie help\" if you need help.")
		speech.speak("Feel free to fork me on github at http://github.com/mikemelch to teach me new commands!")

def main():
	if len(sys.argv) < 2:
		speech.emptyCommand()
		return -1

	command = " ".join([str(sys.argv[word]) for word in range(1, len(sys.argv))]).lower()

	parse(command)