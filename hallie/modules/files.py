#!/usr/bin/env python
import speech
import subprocess

def printFiles():
	"""ls command"""
	speech.speak("Executing 'ls' command to show your files.\n")
	subprocess.call(["ls"])

def sudo():
	"""sudo the last command"""
	speech.speak("Executing 'sudo !!' command to give the last command admin rights.\n")
	subprocess.call(['sudo', '!!'])

def mkdir(name):
	"""create new directory with a given name and location"""
	speech.speak("Executing 'mkdir " + name + "' command to create a directory.\n")
	subprocess.call(["mkdir", name])