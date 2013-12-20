#! /usr/bin/env python

import curses
import urllib
import sys
import time

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
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)


def displayGui():

	count = 1

	while 1:
		createHeader()
		readData(count)
		myscreen.refresh()

		

		if count < 5:
			count += 1
		else:
			count = 1

		time.sleep(1)



def readData(count):

	row = 2
	data = eval(urllib.urlopen("").read());

	for current in data["jobs"]:

		nameToDisplay = current["name"].strip();
		myscreen.addstr(row, 2, nameToDisplay, curses.color_pair(2))
		animation = createAnimation(count);
		myscreen.addstr(row, 30, animation, curses.color_pair(3))
		row += 1

def createAnimation(count):
	result = "|" * count
	space = " " * (5-count)
	result = result+space
	return result



init();
displayGui()
	
curses.endwin()

readData();