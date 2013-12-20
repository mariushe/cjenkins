#! /usr/bin/env python

import curses
import urllib
import sys

def createHeader():

	header = "Curses Jenkins"
	spaceLength = " " * ((y-14)/2)


	header = spaceLength + header + spaceLength;
	myscreen.addstr(0, 0, header,curses.color_pair(1))

def init():	
	global myscreen, x, y

	myscreen = curses.initscr()
	myscreen.border(0)
	x,y = myscreen.getmaxyx();
	curses.start_color()
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
	createHeader()
	readData()

	myscreen.refresh()
	myscreen.getch()
	curses.endwin()

def readData():

	row = 2
	data = eval(urllib.urlopen("").read());

	for current in data["jobs"]:

		nameToDisplay = current["name"].strip();
		myscreen.addstr(row, 2, nameToDisplay)
		row += 1


init();

readData();