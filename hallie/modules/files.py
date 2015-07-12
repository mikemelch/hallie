#!/usr/bin/env python
import os
import speech
import subprocess
from subprocess import Popen

def printFiles():
	"""ls command"""
	speech.speak("Executing 'ls' command to show your files.\n")
	os.system("ls")

def sudo():
	"""sudo the last command"""
	speech.speak("Executing 'sudo !!' command to give the last command admin rights.\n")
	subprocess.Popen(["!!"])

def mkdir():
	print