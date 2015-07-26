#!/usr/bin/env python
from os.path import expanduser

def getDataFile():
	return expanduser("~") + '/.hallie.dat'

def platformCompatible():
	"""Checks whether the user's operating system is MACOSX (Darwin)"""
	if platform.system() != "Darwin":
		speech.fail("Sorry but this command isn't available on your platform.")
		return False
	return True

def help():
	"""teaches the user how to use hallie"""


	print """\n\n
	Hey there! My name is hallie and my goal is to help save 
	you some time while you're using the command line.

	Why don't we start with some basic commands...

	'hallie show my files' -> executes 'ls' command to show all the files
	in your current directory

	'hallie extract file.zip' -> extracts the files in file.zip

	'hallie teach me how to use ls' -> executes 'man' command to give you
	information about the ls command

	'hallie copy thisFile' -> copies thisFile for you

	'hallie paste' -> pastes whatever was copied for you, in the directory 
	that you are currently in

	For Mac users...

	'hallie play all too well by taylor swift' -> will play All Too Well by
	Taylor Swift if it is in your iTunes library (which it should be)

	'hallie pause' -> pauses iTunes if it is playing

	'hallie skip' -> skips the current song in iTunes

	'hallie play the artist kanye west' -> will create a playlist of all kanye
	west songs for you and play them (playlist name will be hallie song queue)


	There are many more things that I can do! 

	Visit https://github.com/mikemelch/hallie to see more. If I can't do something
	that you think I should, feel free to fork me or add an issue.

	Thanks and enjoy!
	"""