import pyautogui
import time
from threading import Timer
import math
from art import *
import webbrowser
import os
from colorama import Fore
import sys, traceback


def main():
  try:

    os.system("cls")

    print(Fore.RED + text2art("RAH v1.0", font = "small"))

    i = 0
    logFile = 0

    print("please enter r,g,b values(default values will be used if no input)")
    webrgb = (input("Do you want to open a website to choose the rgb colors(y/n)? ") or "n").lower()

    if len(webrgb) == 1:
      if webrgb == "y":
        webbrowser.open('https://htmlcolorcodes.com/color-picker/', new = 2)

    a = int(input("r: ") or 99)
    b = int(input("\ng: ") or 219)
    c = int(input("\nb: ") or 100)
    speed = float(input("Please input your desired speed (0-1) ") or 0.50)
    log = (input("Do you want to generate a log.txt file for debugging purposes(y/n)? ") or "n").lower()
    if len(log) == 1:
      if log == "y":
        logFile = 1
        f = open("log.txt", "w+")
      elif log == "n":
        logFile = 0
    print("watching...[CTRL+C to stop]")

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
      colors = (a, b, c)
      if screen.getpixel(coords) == colors:
        click(coords)

    def click(x):
      begin = time.time()
      pyautogui.click(x)
      if logFile:
        f = open("log.txt", "a")
        f.write(("- clicked screen after %dms \n" % truncate((time.time() - begin) * 1000, 6)))
        time.sleep(1)

  except KeyboardInterrupt:
    print ("exiting...")

if __name__ == "__main__":
  main()