from telnetlib import X3PAD
import pyautogui
import keyboard
import mouse

pyautogui.click(960,540, button='left', clicks=10000, interval=0.001)      
click = 0       
if mouse.is_pressed("left"):
        click += 1
        if click == 10000:
            pyautogui.mouseUp(x=960, y=540, button='left')
