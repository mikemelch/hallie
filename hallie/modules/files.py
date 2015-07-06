#!/usr/bin/env python
import os
import speech

def printFiles():
	"""ls command"""
	speech.speak("Executing 'ls' command to show your files.\n")
	os.system("ls")
