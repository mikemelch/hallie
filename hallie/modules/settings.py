#!/usr/bin/env python
from os.path import expanduser

def getCopyStorageFile():
	return expanduser("~") + '/hallie.dat'

def help():
	"""teaches the user how to use hallie"""