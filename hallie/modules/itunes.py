#!/usr/bin/env python
import speech
import subprocess
import os
import platform
import settings

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
			end if
		end if
	end if
end tell"""

ITUNES_SONG_AND_ARTIST = """tell application "iTunes"
	set playlistName to "hallie song queue"
	set songResults to (every file track of playlist "Library" whose name contains "%s" and artist contains "%s")
	if not songResults = {} then
		set song to item 1 of songResults
		play song
		return get name of song & " by " & (get artist of song)
	else
		set albumResults to (every file track of playlist "Library" whose album contains "%s" and artist contains "%s")
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
		end if
	end if
end tell"""

ITUNES_ALBUM_AND_ARTIST = """tell application "iTunes"
	set playlistName to "hallie song queue"
	set albumResults to (every file track of playlist "Library" whose artist contains "%s" and album contains "%s")
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
	end if
end tell"""

ITUNES_ALBUM = """tell application "iTunes"
	set playlistName to "hallie song queue"
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
	end if
end tell"""

ITUNES_ARTIST = """tell application "iTunes"
	set playlistName to "hallie song queue"
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
		return get artist of song
	end if
end tell"""

SKIP = """tell application "iTunes"
next track
end tell"""

PAUSE = """tell application "iTunes"
pause
end tell"""

RESUME = """tell application "iTunes"
playpause
end tell"""

def pause():
	"""Tell iTunes to pause"""

	if not platformCompatible():
		return False

	(output, error) = subprocess.Popen(["osascript", "-e", PAUSE], stdout=subprocess.PIPE).communicate()

def resume():
	"""Tell iTunes to resume"""

	if not platformCompatible():
		return False

	(output, error) = subprocess.Popen(["osascript", "-e", RESUME], stdout=subprocess.PIPE).communicate()


def skip():
	"""Tell iTunes to skip a song"""

	if not platformCompatible():
		return False

	(output, error) = subprocess.Popen(["osascript", "-e", SKIP], stdout=subprocess.PIPE).communicate()


def play(song, artist=None, album=None):
	"""Tells iTunes to play a given song/artist/album - MACOSX ONLY"""

	if not settings.platformCompatible():
		return False

	if song and not artist and not album:
		(output, error) = subprocess.Popen(["osascript", "-e", DEFAULT_ITUNES_PLAY % (song, song, song)], stdout=subprocess.PIPE).communicate()
		if output:
			speech.speak("Playing " + output)
		else:
			speech.speak("Unable to find " + song + " in your library.")

	elif song and artist and not album:
		(output, error) = subprocess.Popen(["osascript", "-e", ITUNES_SONG_AND_ARTIST % (song, artist, song, artist)], stdout=subprocess.PIPE).communicate()
		if output:
			speech.speak("Playing " + output)
		else:
			speech.speak("Unable to find " + song + " in your library.")

	elif album and artist and not song:
		(output, error) = subprocess.Popen(["osascript", "-e", ITUNES_ALBUM_AND_ARTIST % (artist, album)], stdout=subprocess.PIPE).communicate()
		if output:
			speech.speak("Playing " + output)
		else:
			speech.speak("Unable to find " + song + " in your library.")

	elif album and not artist and not song:
		(output, error) = subprocess.Popen(["osascript", "-e", ITUNES_ALBUM % (album)], stdout=subprocess.PIPE).communicate()
		if output:
			speech.speak("Playing " + output)
		else:
			speech.speak("Unable to find " + song + " in your library.")

	elif artist and not album and not song:
		(output, error) = subprocess.Popen(["osascript", "-e", ITUNES_ARTIST % (artist)], stdout=subprocess.PIPE).communicate()
		if output:
			speech.speak("Playing " + output)
		else:
			speech.speak("Unable to find " + song + " in your library.")
