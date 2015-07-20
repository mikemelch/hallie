#!/usr/bin/env python
import speech
import subprocess
import os
import platform

DEFAULT_ITUNES_PLAY = """tell application "iTunes"
	set playlistName to "hallie song queue"
	--Check to see if song exists
	set songResults to (every file track of playlist "Library" whose name contains "%s")
	if not songResults = {} then
		set song to item 1 of songResults
		play song
		return get name of song & " by " & (get artist of song)
	else
		--Check to see if it's an artist
		set artistResults to (every file track of playlist "Library" whose artist contains "%s")
		if not artistResults = {} then
			set song to item 1 of artistResults
			if user playlist playlistName exists then
				try
					delete tracks of user playlist playlistName
				end try
			else
				make new user playlist with properties {name:playlistName}
			end if
			
			try
				repeat with trk in artistResults
					duplicate trk to user playlist playlistName
				end repeat
			end try
			play the playlist named playlistName
			return get name of song & " by " & (get artist of song)
		else
			set albumResults to (every file track of playlist "Library" whose album contains "%s")
			if not albumResults = {} then
				set song to item 1 of albumResults
				if user playlist playlistName exists then
					try
						delete tracks of user playlist playlistName
					end try
				else
					make new user playlist with properties {name:playlistName}
				end if
				
				try
					repeat with trk in albumResults
						duplicate trk to user playlist playlistName
					end repeat
				end try
				play the playlist named playlistName
				return get album of song & " by " & (get artist of song)
			else
				return -1
			end if
		end if
	end if
end tell"""

ITUNES_SONG_AND_ARTIST = """tell application "iTunes"
	set songResults to (every file track of playlist "Library" whose name contains "%s" and artist contains "%s")
	if not songResults = {} then
		set song to item 1 of songResults
		play song
		return get name of song & " by " & (get artist of song)
	end if
end tell"""




def play(song, artist=None, album=None):
	"""Tells iTunes to play a given song/artist/album"""
	global DEFAULT_ITUNES_PLAY

	if platform.system() != "Darwin":
		speech.speak("Sorry but this command isn't available on your platform.\n")
		return

	if song and not artist and not album:
		(output, error) = subprocess.Popen(["osascript", "-e", DEFAULT_ITUNES_PLAY % (song, song, song)], stdout=subprocess.PIPE).communicate()
		if output:
			speech.speak("Playing " + output)
		else:
			speech.speak("Unable to find " + song + " in your library.\n")

	elif song and artist and not album:
		(output, error) = subprocess.Popen(["osascript", "-e", ITUNES_SONG_AND_ARTIST % (song, artist)], stdout=subprocess.PIPE).communicate()
		if output:
			speech.speak("Playing " + output)
		else:
			speech.speak("Unable to find " + song + " in your library.\n")

play("watch the throne")
