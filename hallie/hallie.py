#!/usr/bin/env python
import sys
import re

from modules import *

def parse(command):
	#print re.match("(run.*(as|with)\s(priv.*|super.*|sudo|root|admin.*))|sudo|admin|super.*", command)

	if re.match(r"(please\s)*(show|give|tell|list|print)\s(me|my)*.*\s(files)", command):
		files.printFiles()
	elif re.match(r"(run.*(as|with)\s(priv.*|super.*|sudo|root|admin.*))|sudo|admin|super.*", command):
		files.sudo()
	elif re.match(r"(create|make|start|build|construct|prepare|whip).*(directory|folder|catalogue)(\sin\s(?P<location>""?.*""?))*\s(and\s)(call(ed)?|name(ed)?)(\sit\s)?(?P<name>.*)", command):
		files.mkdir()

def main():
	if len(sys.argv) < 2:
		speech.emptyCommand()
		return -1

	command = " ".join([str(sys.argv[word]) for word in range(1, len(sys.argv))]).lower()

	parse(command)