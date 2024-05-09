import webbrowser
import keyboard
import pyautogui , sys
import time
from tkinter import *
from tkinter import ttk

ChromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(ChromePath))

def OpenDocs():
    webbrowser.get('chrome').open("https://docs.google.com/document/u/0/?pli=1&tgif=d")
def OpenClass():
    webbrowser.get('chrome').open("https://classroom.google.com/h")
def OpenSlides():
    webbrowser.get('chrome').open("https://docs.google.com/presentation/u/0/?tgif=c")


while True:
    if keyboard.is_pressed("Numlock"):
        root = Tk()
        frm = ttk.Frame(root, padding=50)
        frm.grid()
        ttk.Label(frm, text="Choose Thing").grid(column=0,row=0)
        ttk.Button(frm, text="Google Classroom", command=OpenClass).grid(column=1,row=0)
        ttk.Button(frm, text="Google Docs", command=OpenDocs).grid(column=2,row=0)
        root.wm_attributes("-topmost", True)
        ttk.Button(frm, text="Google Slides", command=OpenSlides).grid(column=3,row=0)
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4,row=0)
        root.mainloop()
        time.sleep(5)