from image import *
from mouse import * 
from tricks import *



locations = {
"play":(640, 490),
"newGame":(270, 320),
"leftButton":(100, 435),
"rightButton":(1180, 435),
"easy":(310,310),
"normalLevel":(850,540),
"yes":(900, 500)
}


def isStart():
	startref = Image.open("/Users/moritz/Documents/Bloons/startref.png")
	current = ImageGrab.grab(bbox=(140, 500, 240, 530))
	if compare(startref, current) < 0.01:
		return True
	else:
		return False

def left():
	mouseClick(locations["leftButton"])
	delay(0.1)
def right():
	mouseClick(locations["rightButton"])
	delay(0.1)
	
def select(wanted):
	cur = 0
	while cur != wanted:
		right()
		cur+=1
def newGame(level):
	if isStart():
		mouseClick(locations["play"])
		delay(2)
		mouseClick(locations["newGame"])
		delay(6)
		select(level)
		delay(0.5)
		mouseClick(locations["play"])
		delay(1)
		mouseClick(locations["easy"])
		delay(1.5)
		mouseClick(locations["normalLevel"])
		delay(1)
		mouseClick(locations["yes"])
	else:
		raise BloonsError("not in menu")
