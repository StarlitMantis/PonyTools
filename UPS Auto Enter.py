#UPS Auto Enter
import pyautogui
import time
import pymsgbox
import re
import ast


trackingNumList=[]

while True:
    trackingNum=pymsgbox.prompt(text='Enter a UPS Tracking Number:',title='Tracking Number Prompt',default='1Z.........')
    if trackingNum not in trackingNumList:
        trackingNumList.append(trackingNum)
    stopRe=re.compile('.*stop')
    stopCheck=stopRe.search(trackingNum)

    try:
        if stopCheck.group(0)=='stop':
            break    
    
    except AttributeError:
        continue
    continue
    

pyautogui.click(69, 740) #opens search
time.sleep(1)
pyautogui.write('chrome') #types chrome into search
time.sleep(.1)
pyautogui.press('enter')
time.sleep(.5)
pyautogui.keyDown('winleft') #maximizes the window
pyautogui.keyDown('up')
time.sleep(.2)
pyautogui.keyUp('winleft')
pyautogui.keyUp('up')
time.sleep(.2)
pyautogui.write('https://ap.ups.com/REAP/AccessPoint.htm') #goes to website
pyautogui.press('enter')

pyautogui.click(684,399, duration=1.5) #logs in
pyautogui.click(351,554, duration=3) #opens tracking num screen
time.sleep(1)
for i in range(len(trackingNumList)-1):
    pyautogui.write(trackingNumList[i]) #enters tracking nums
    pyautogui.press('enter')
    time.sleep(2)
pyautogui.click(928,456,duration=.8) #enters tracking nums
