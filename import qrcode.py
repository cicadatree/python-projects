
import calendar
from tkinter import *

def showCalendar():
    gui = Tk()
    gui.config(background='grey')
    gui.title("calendar for the year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainLoop()