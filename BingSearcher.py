#Welcome to the Main script of my auto Bing Searcher

import time
import pyautogui
import random




def test():
    pyautogui.write('Hello World!')
    pyautogui.press('enter')

time.sleep(5)
#print(v)
#print(pyautogui.position())

while True:
    v = random.randint(1, 100)
    pyautogui.click(x=315, y=177)
    pyautogui.write(str(v))
    pyautogui.press('enter')
    time.sleep(5)



