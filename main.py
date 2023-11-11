import numpy as np
from PIL import ImageGrab
import win32api, win32con
import os
import cv2
import keyboard
import pyautogui
import random as r
import time


x_pad = 590
y_pad = 280


def screenGrab():

    im = ImageGrab.grab(bbox=(590,280,1160,810) )
    im.save(os.getcwd() + '\\grab.png','PNG')
    return im

class Cord:
    c2 = (1230,490)
    c3 = (1275,490)
    c4 = (1315,490)
    c5 = (1190,530)
    c6 = (1230,530)
    c7 = (1275,530)
    c8 = (1315,530)
    c9 = (1190,565)
    c10 = (1230,565)
    c11 = (1275,565)
    c12 = (1315,565)
    c13 = (1190,600)
    c14 = (1230,600)
    c15 = (1275,600)
    c16 = (1315,600)
    c17 = (1190,635)
    c18 = (1230,635)
    c19 = (1275,635)
    c20 = (1315,635)
    c21 = (1190,670)
    c22 = (1230,670)
    c23 = (1275,670)
    c24 = (1315,670)
    c25 = (1190,710)
    c26 = (1230,710)
    c27 = (1275,710)
    c28 = (1315,710)



def drop():

    x,y = pyautogui.position()

    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
    pyautogui.moveTo(x,(y+40),0.15)
    leftclick()


def leftclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print("click")
    time.sleep(.01)


def findimage():


    im = ImageGrab.grab(bbox=(640, 327, 685, 348))
    im.save(os.getcwd() + '\\afkgrab.png', 'PNG')

    afkgrb = cv2.imread("afkgrab.png")
    tpl3 = cv2.imread("template_3.png")

    fishing = pyautogui.locate(tpl3, afkgrb, confidence=0.90)
    print(fishing)


    if fishing is not None:
        time.sleep(10)
        print("not afking!")
        return
    else:


        screenGrab()
        image = cv2.imread("grab.png")
        tpl = cv2.imread("template.png")
        result = cv2.matchTemplate(image,tpl,cv2.TM_CCOEFF_NORMED)
        #result = cv2.matchTemplate(image,tpl, cv2.TM_CCORR_NORMED)

        x,y = np.unravel_index(result.argmax(),result.shape, order = 'C')
        print (x,y)

        cord1,cord2 = pyautogui.position()


        cordx = ((((x+y_pad) - cord1)**2)**0.5)
        cordy = ((((y+x_pad) - cord2)**2)**0.5)

        if cordx and cordy <= 200:
            duration = ((r.randint(20,75))/100)
        elif cordx and cordy <= 750:
            duration = ((r.randint(85, 125))/100)
        else:
            duration = ((r.randint(125, 200))/100)

        print(f"duration is {duration}")

        try:
            pyautogui.moveTo((y+x_pad+20),(x+y_pad+10),duration)
            check_tree()

        except:
            return


def emptyinv():

    c = Cord()



    pyautogui.moveTo(c.c28)
    drop()
    pyautogui.moveTo(c.c27)
    drop()
    pyautogui.moveTo(c.c26)
    drop()
    pyautogui.moveTo(c.c25)
    drop()
    pyautogui.moveTo(c.c24)
    drop()
    pyautogui.moveTo(c.c23)
    drop()
    pyautogui.moveTo(c.c22)
    drop()
    pyautogui.moveTo(c.c21)
    drop()
    pyautogui.moveTo(c.c20)
    drop()
    pyautogui.moveTo(c.c19)
    drop()
    pyautogui.moveTo(c.c18)
    drop()
    pyautogui.moveTo(c.c17)
    drop()
    pyautogui.moveTo(c.c16)
    drop()
    pyautogui.moveTo(c.c15)
    drop()
    pyautogui.moveTo(c.c14)
    drop()
    pyautogui.moveTo(c.c13)
    drop()
    pyautogui.moveTo(c.c12)
    drop()
    pyautogui.moveTo(c.c11)
    drop()
    pyautogui.moveTo(c.c10)
    drop()
    pyautogui.moveTo(c.c9)
    drop()
    pyautogui.moveTo(c.c8)
    drop()
    pyautogui.moveTo(c.c7)
    drop()
    pyautogui.moveTo(c.c6)
    drop()
    pyautogui.moveTo(c.c5)
    drop()
    pyautogui.moveTo(c.c4)
    drop()
    pyautogui.moveTo(c.c3)
    drop()
    pyautogui.moveTo(c.c2)
    drop()


    print("Empty!")


def check_tree():


    x,y = pyautogui.position()
    im = ImageGrab.grab(bbox =((x+60),(y+20),(x+85),(y+45)))
    im.save(os.getcwd() + '\\treegrab.png', 'PNG')

    grb = cv2.imread("treegrab.png")
    tpl2 = cv2.imread("template_2.png")

    is_there = pyautogui.locate(tpl2,grb, confidence = 0.60)
    print(is_there)

    if is_there is not None:
        leftclick()
        time.sleep(10)
    else:
        return



def checkinv():


    im = ImageGrab.grab(bbox=(1300,690,1340,725))
    im.save(os.getcwd() + '\\lastinv.png', 'PNG')

    invgrb = cv2.imread("lastinv.png")
    invtpl = cv2.imread("invtemplate.png")

    is_there = pyautogui.locate(invtpl, invgrb, confidence=0.50)
    print(is_there)

    if is_there is not None:
        emptyinv()
        return
    else:
        return





def clicktarget():
    findimage()


def main():


    while True:
        if keyboard.is_pressed("Esc"):
            break
        else:
            checkinv()
            clicktarget()


if __name__ == '__main__':
    main()
