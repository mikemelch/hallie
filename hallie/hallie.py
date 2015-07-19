#!/usr/bin/env python
import sys
import re
import pickle

from modules import *

def parse(command):
	if re.search(r"(please\s)*(show|give|tell|list|print)\s(me|my)*.*\s(files)", command):
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

def main():
	if len(sys.argv) < 2:
		speech.emptyCommand()
		return -1

	command = " ".join([str(sys.argv[word]) for word in range(1, len(sys.argv))]).lower()

	parse(command)