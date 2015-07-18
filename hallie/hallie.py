#!/usr/bin/env python
import sys
import re

from modules import *

def parse(command):
	if re.search(r"(please\s)*(show|give|tell|list|print)\s(me|my)*.*\s(files)", command):
		files.printFiles()
	#elif re.match(r"(run.*(as|with)\s(priv.*|super.*|sudo|root|admin.*))|sudo|admin|super.*", command):
		#files.sudo()
	elif re.search(r"(create|make|start|build|construct|prepare|whip).*(directory|folder|catalogue)(\s)(and\s)?(call(ed)?|name(ed)?)(\sit\s)?(?P<name>.*)", command):
		matches = re.search(r"(create|make|start|build|construct|prepare|whip).*(directory|folder|catalogue)(\s)(and\s)?(call(ed)?|name(ed)?)(\sit\s)?(?P<name>.*)", command)
		files.mkdir(matches.group('name').strip())

def main():
	if len(sys.argv) < 2:
		speech.emptyCommand()
		return -1

	command = " ".join([str(sys.argv[word]) for word in range(1, len(sys.argv))]).lower()

	parse(command)