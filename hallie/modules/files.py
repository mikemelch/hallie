#!/usr/bin/env python
import speech
import subprocess
from pyunpack import Archive

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

def man(command):
	"""show documentation for a given command"""
	speech.speak("Executing 'man " + command + "' to show you documentation for this command.\n")
	subprocess.call(["man", command])

def extract(file, format, location):
	"""extract tar, gz, zip, rar files"""
	speech.speak("Extracting files in " + file + ".\n")
	if not location:
		location = "."
	Archive(file).extractall(location)
