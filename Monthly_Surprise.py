# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:27:33 2020

@author: Andrew Snavely
"""
import random
import datetime
from datetime import datetime
from datetime import date
from datetime import timedelta
from tkinter import *


def last_day(any_day):
    next_month = any_day.replace(day=28) + timedelta(days=4)
    l_day = next_month - timedelta(days=next_month.day)
    l_day = l_day.day
    return l_day

today = datetime.today()

month = today.month
year = today.year

#print(str(month) + "/" + str(year))
final_day = last_day(date(year, month, 1))
rand_num = random.randrange(1,final_day)
print(rand_num)
datetime_object = datetime.strptime(str(month), "%m")
month_name = datetime_object.strftime("%B")


gui = Tk()
gui.geometry("400x400")

gui.configure(background='black')
label1 = Label(gui, fg="green", bg="black", font=(None, 50), text=str(month_name))
label1.config(anchor=CENTER)

label2 = Label(gui, fg="green", bg="black", font=(None, 150), text=str(rand_num))
label2.config(anchor=CENTER)
label1.pack()
label2.pack()




gui.mainloop() 




