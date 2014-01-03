#! /usr/bin/env python

# Jenkins monitor in terminal based on the curses library

import curses
import urllib
import sys
import time

def createHeader():

	header = "Curses Jenkins"
	headerPos = (x/2) - 7

	myscreen.addstr(0, headerPos, header,curses.color_pair(1))

def init():	

	global myscreen, x, y

	myscreen = curses.initscr()
	myscreen.border(0)
	curses.curs_set(0);

	y,x = myscreen.getmaxyx();

	defineColors();
	
def defineColors():

	curses.start_color()
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
	curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)

def displayGui():

	count = 1

	try:
		while 1:

			createHeader()
			readData(count)
			myscreen.refresh()

			if count < 5:
				count += 1
			else:
				count = 1

			time.sleep(1)

	except (KeyboardInterrupt, SystemExit):
		curses.endwin()
		sys.exit(0)



def readData(count):

	row = 4
	data = eval(urllib.urlopen(str(sys.argv[1]) + "/api/python?depth=1&pretty=true").read());

	addDescription(data["description"])

	for current in data["jobs"]:

		nameToDisplay = current["name"].strip();
		color = current["color"].strip();
		colorCode = getColorCode(color);

		addHealthReport(current, row)

		myscreen.addstr(row, 16, nameToDisplay, curses.color_pair(colorCode))

		addStructure(row)
		
		addProgressBar(count, row, nameToDisplay, color)

		createStatus(row, color)

		addQuitInstructions(y)
		
		row += 1

def addStructure(row):

		myscreen.addstr(row, 49, "[", curses.color_pair(1))
		myscreen.addstr(row, 56, "]", curses.color_pair(1))

def addHealthReport(current, row):

	if x > 119:	
		myscreen.addstr(row, 58, " " * (x-59), curses.color_pair(4))
		myscreen.addstr(row, 58, current["healthReport"][0]["description"], curses.color_pair(4))

def addDescription(description):

	# We just allow 1 line of description
	description = description.split('\n')[0]

	# If description is to long, cut of parts of the end
	if (x-2) < len(description):
		description = description[:(x-10)]
		description += " (...)"

	myscreen.addstr(2, 2, description, curses.color_pair(1))

def addProgressBar(count, row, nameToDisplay, color):

	if "anime" in color:
		progressBar = createProgressBar(count);
		myscreen.addstr(row, 50, progressBar, curses.color_pair(3))
	else:
		myscreen.addstr(row, 50, " " * 5, curses.color_pair(3))

def createProgressBar(count):

	result = "|" * count
	space = " " * (5-count)
	result = result+space
	return result

def addQuitInstructions(y):
	myscreen.addstr(y-2, 2, "To quit, press ctrl+C")

def createStatus(y, color):

	if "blue" in color:
		myscreen.addstr(y, 2, "      [ OK ]", curses.color_pair(2))
	elif "disabled" in color:
		myscreen.addstr(y, 2, "[ DISABLED ]", curses.color_pair(4))
	elif "yellow" in color:
		myscreen.addstr(y, 2, "[ UNSTABLE ]", curses.color_pair(5))
	elif "red":
		myscreen.addstr(y, 2, "  [ FAILED ]", curses.color_pair(6))

def getColorCode(color):

	if "blue" in color:
		return 2
	elif "disabled" in color:
		return 4
	elif "yellow" in color:
		return 5
	elif "red":
		return 6


if len(sys.argv) != 2:
	print("ERROR: Wrong nr of parameter")
	print("  Usage: ./cjenkins.py <pathToJenkins>")
	exit(1)

init();

displayGui()
	
curses.endwin()

readData();
