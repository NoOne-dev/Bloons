import os
import time
from mouse import *

def delay(t=0.1):
	time.sleep(t)

def prepareWindow():
	activate()
	delay()
	moveWindow()
	mouseMove((0,0))

def activate():
	cmd = """osascript -e 'activate application "Bloons TD 5"'"""
	os.system(cmd)
	
def moveWindow():
	cmd = """osascript -e 'tell application "System Events" to set position of first window of application process "Bloons TD 5" to {0, 0}'"""
	os.system(cmd)
