#!/usr/bin/python2
#Source of this information comes from the following site.
#https://www.tutorialspoint.com/python/python_gui_programming.htm
import Tkinter
import tkMessageBox
import sys
import os

top = Tkinter.Tk()
top.title('ShortKeys')

#Creating my message box data string.
data1 = ("Hello Everyone\n\nWelcome to our first venture into creating a GUI!!!")
data2 = ("\n\nIf you want to know how I did this, go to this website:")
data3 = ("\n\nhttps://www.tutorialspoint.com/python/python_gui_programming.htm")
data = data1 + data2 + data3
xdata = ("Did my new button open this?")
#define the following.
def helloCallBack():
    tkMessageBox.showinfo( "About This Program", '%s' % data)

def hiyaCallBack():
    os.system('~/Documents/scripts/helloworld.py')
#Dis what it's gon say at the beginning.
B = Tkinter.Button(top, text ="About", command = helloCallBack, foreground="red")
C = Tkinter.Button(top, text="Launch", command = hiyaCallBack, foreground="green")

B.pack()
C.pack()
#you have to leave this here, so that it will always run...it's a loop
top.mainloop()
