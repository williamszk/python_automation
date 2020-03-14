#this script will open the browser

import pyautogui
import time

import win32gui
import win32con

#click at the most left bottom corner
#where there is a button to minimize all windows
#Point(x=1919, y=1079)
pyautogui.click(1917, 1052)
time.sleep(3) #waint for 3 seconds

#to click on windows incon
pyautogui.click(x=29, y=1054)
time.sleep(3)

pyautogui.typewrite('google chrome')
pyautogui.typewrite(['enter'])
time.sleep(5)

"""
#the commands below maximizes a window
#this will work on windows OS
window = win32gui.GetForegroundWindow()
win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
"""

#an alternative way to maximize the browser window
#the following command will maxmize a browser window
pyautogui.keyDown('alt') #holds 'alt'
pyautogui.press(' ') #press 'space bar'
pyautogui.press('x') #select 'x' which is the maximize option
pyautogui.keyUp('alt') #unholds 'alt'


#after the window is open we need to enter into my site
#to make python click
#position 357,69 is the position of the browser tab in the browser full screen
pyautogui.click(357,69)

#on the browser it will click on the tab and write "Hello World!"
pyautogui.typewrite("https://williamszk.github.io/")

pyautogui.typewrite(['enter'])




