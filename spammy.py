import os
import pyautogui
import time
animalfile = open('animals.txt','r')
time.sleep(5)
for line in animalfile:
    pyautogui.write('You are a '+line)
    pyautogui.press('enter')