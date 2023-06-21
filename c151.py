#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 16:57:55 2023

@author: aquilavijayanayagam
"""

from tkinter import*
import random
root=Tk()
root.title("profits")
root.geometry("400x400")
month =("jan","feb"",mar","apr","may","jun","jul","aug","sep","oct","nov","dec")

profits =("20","15","20","32","52","16","1","0.5","12","13","88","99.1")

max_profits = max(profits)
max_profits_index=max_profits.index(max_profits)
print(max_profits_index)

max_profits_months = max(month)[max_profits_index]
print("the maximum profit was " + str(max_profits) + " it was recorded in " + str(max_profits_months))



min_profits = min(profits)
min_profits_index=min_profits.index(min_profits)
print(min_profits_index)

max_profits_months = max(month)[max_profits_index]
print("the minimum profit was " + str(min_profits) + " it was recorded in " + str(max_profits_months))


label1=Label(root,text=month)
label2=Label(root,text=profits)
button1=Button(root, text="show most profitable month",command=print("the minimum profit was " + str(min_profits) + " it was recorded in " + str(max_profits_months)))
button2=Button(root,text="show least profitable month",command=print("the minimum profit was " + str(min_profits) + " it was recorded in " + str(max_profits_months)))

label1.place(relx= 0.5, rely=0.2, anchor = CENTER)
label2.place(relx= 0.5, rely=0.3, anchor = CENTER)
button1.place(relx= 0.5, rely=0.5, anchor = CENTER)
button2.place(relx= 0.5, rely=0.6, anchor = CENTER)
root.mainloop()


