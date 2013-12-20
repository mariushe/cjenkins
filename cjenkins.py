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
	while 1:
		createHeader()
		readData()
		myscreen.refresh()

		time.sleep(1)



def readData():

	row = 2
	data = eval(urllib.urlopen("http://jenkins.sendregning.no:8090/api/python?pretty=true").read());

	for current in data["jobs"]:

		nameToDisplay = current["name"].strip();
		myscreen.addstr(row, 2, nameToDisplay, curses.color_pair(2))
		myscreen.addstr(row, 30, "||||||||", curses.color_pair(3))
		row += 1


init();
displayGui()
	
curses.endwin()

readData();