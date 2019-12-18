import pyautogui
import time
from threading import Timer
import math
from art import *

print(text2art("RAH v1.0", font="small"))

f = open("log.txt","w+")
session = time.time()
f = open("log.txt","a")
f.write(str(session))
i = 0

print("please enter r,g,b values(default values will be used if no input)")
a = int(input("r: ") or 99)
b = int(input("\ng: ") or 219)
c = int(input("\nb: ") or 100)
speed = float(input("Please input your desired speed (0-1)") or 0.50)
print("watching...")

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def hello():
    coords()
    Timer(speed, hello).start()
Timer(speed, hello).start()

def coords():
    screen = pyautogui.screenshot()
    coords = pyautogui.position()
    colors = (a,b,c)
    if screen.getpixel(coords) == colors:
        click(coords)

def click(x):
    begin = time.time()
    pyautogui.click(x)
    f = open("log.txt","a")
    f.write(("- clicked screen after %fms(score should be around %d) \n"  % (truncate(time.time() - begin,6),(time.time() - begin)*1000)))
    time.sleep(1)

if exit():
    f.close()