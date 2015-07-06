#!/usr/bin/env python
import sys
import re

from modules import *

def parse(command):
	if re.match("(please )*(show|give|tell|list|print) (me|my)*.* (files)", command):
		files.printFiles()


def main():
	if len(sys.argv) < 2:
		speech.emptyCommand()
		return -1

	command = " ".join([str(sys.argv[word]) for word in range(1, len(sys.argv))]).lower()

	parse(command)
	
