#!/usr/bin/env python

prefix = "hallie> "

class PrintColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def success(words):
	print PrintColors.OKGREEN + prefix + words + PrintColors.ENDC

def fail(words):
	print PrintColors.FAIL + prefix + words + PrintColors.ENDC

def warning(words):
	print PrintColors.WARNING + prefix + words + PrintColors.ENDC

def speak(words):
	print prefix + words

def error():
	print PrintColors.FAIL + prefix + "Sorry, I don't know how to do this for your platform yet!" + PrintColors.ENDC

def question(words):
	return raw_input(prefix + words)

def emptyCommand():
	print prefix + "Sorry, I don't understand!\n" + prefix + "Tell me something to do, like 'hallie show me the current files'"
