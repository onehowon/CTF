from telnetlib import X3PAD
import pyautogui
import keyboard
import mouse

click = 0
while True:        
        if mouse.is_pressed("left"):
            click += 1
            print(click,"번 클릭했습니다.")
            if click == 5:
                break;
            