#!/usr/bin/env python
import speech
import platform
import pip
import subprocess

def installPackagePip(package):
	"""tries to install a given package on pip"""
	speech.speak("Attempting to install '" + package + "' on the 'pip' package manager.\n")
	pip.main(['install', package])


#TODO: Add more package managers
def installPackage(package):
	"""installs a given package from a package manager depending on a user's OS"""
	installPackagePip(package)