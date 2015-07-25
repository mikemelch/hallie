#!/usr/bin/env python
import speech
import subprocess
import os
import settings
from pyunpack import Archive
import pickle
import pkg_resources
from os.path import expanduser

def printFiles():
	"""ls command"""
	speech.speak("Executing 'ls' command to show your files.")
	subprocess.call(["ls"])

def renameFile(original, new):
	"""rename a file"""
	speech.speak("Executing 'mv' command to rename your file.")
	subprocess.call(["mv", original, new])

def removeFile(file):
	"""remove a file"""
	if "y" in speech.question("Are you sure you want to remove " + file + "? (Y/N): ").lower():
		speech.speak("Removing " + file + " with the 'rm' command.")
		subprocess.call(["rm", "-r", file])
	else:
		speech.speak("Okay, I won't remove " + file + ".")

def mkdir(name):
	"""create new directory with a given name and location"""
	speech.speak("Executing 'mkdir " + name + "' command to create a directory.")
	subprocess.call(["mkdir", name])

def man(command):
	"""show documentation for a given command"""
	speech.speak("Executing 'man " + command + "' to show you documentation for this command.")
	subprocess.call(["man", command])

def extract(file, format, location):
	"""extract tar, gz, zip, rar files"""
	speech.speak("Extracting files in " + file + ".")
	if not location:
		location = "."
	Archive(file).extractall(location)

def copy(location):
	"""copy file or directory at a given location; can be pasted later"""
	copyData = settings.getCopyStorageFile()
	copyFileLocation = os.path.abspath(location)
	copy = {"copyLocation": copyFileLocation}
	pickle.dump(copy, open(copyData, "wb"))
	speech.speak(location + " copied successfully!")
	speech.speak("Tip: use 'hallie paste' to paste this file.")

def paste(location):
	"""paste a file or directory that has been previously copied"""
	copyData = settings.getCopyStorageFile()
	data = pickle.load(open(copyData, "rb"))
	if not location:
		location = "."
	speech.speak("Pasting " + data["copyLocation"] + " to current directory.")
	process, error = subprocess.Popen(["cp", "-r", data["copyLocation"], location], stderr=subprocess.STDOUT, stdout=subprocess.PIPE).communicate()
	if "denied" in process:
		speech.fail("Unable to paste your file successfully. This is most likely due to a permission issue. You can try to run me as sudo!")

def whoami():
	"""whoami"""
	speech.speak("Running 'whoami' command.")
	subprocess.call(["whoami"])
