import pyautogui as pg
import os
import webbrowser
import time
import sys
import datetime
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
from time import strftime
import win32gui, win32con



hour1 = 8
minute1 = 30
hour2 = 10
minute2 = 10
hour3 = 11 
minute3 = 45



print(hour1, minute1)
time_now =datetime.datetime.now().strftime("%H:%M:%S")


while (1 ==1):
    time.sleep(5)
    time_now =datetime.datetime.now().strftime("%H:%M:%S")
    print(time_now)
    
    if hour1 == datetime.datetime.now().hour and minute1 == datetime.datetime.now().minute:
        print("Class Time")
        webbrowser.get(chrome_path).open('https://student.allendigital.in/BENGALURU/digital-doubt/Anchith-S-Murthy?token=uBCAWCCwNsCsJ/rIaIcoqDW1hFeLDhjO')
        time.sleep(5)
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        time.sleep(4)
        pg.click(465,398)
        time.sleep(4)
        pg.click(881,478)
        time.sleep(3)
        pg.click(1159,51)
        time.sleep(2)
        Minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
        time.sleep(900)
        os.system("taskkill/f /im chrome.exe")
        time.sleep(5400)
        
        


        hour2 == datetime.datetime.now().hour and minute2 == datetime.datetime.now().minute
        print("Time for 2nd period")
        webbrowser.get(chrome_path).open('https://student.allendigital.in/BENGALURU/digital-doubt/Anchith-S-Murthy?token=uBCAWCCwNsCsJ/rIaIcoqDW1hFeLDhjO')
        time.sleep(4)
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        time.sleep(4)
        pg.click(465,398)
        time.sleep(4)
        pg.click(881,478)
        time.sleep(2)
        pg.click(1159,51)
        time.sleep(2)
        Minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
        time.sleep(900)
        os.system("taskkill/f /im chrome.exe")

        
        hour3 == datetime.datetime.now().hour and minute3 == datetime.datetime.now().minute 
        print("Time for 3rd period")
        webbrowser.get(chrome_path).open('https://student.allendigital.in/BENGALURU/digital-doubt/Anchith-S-Murthy?token=uBCAWCCwNsCsJ/rIaIcoqDW1hFeLDhjO')
        time.sleep(4)
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        time.sleep(4)
        pg.click(465,398)
        time.sleep(4)
        pg.click(881,478)
        time.sleep(2)
        pg.click(1159,51)
        time.sleep(2)
        Minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
        time.sleep(900)
        os.system("taskkill/f /im chrome.exe")



        

        

        

        

        

        

time.sleep(2)
print('done')







