#!/usr/bin/python2
#Source of this information comes from the following site.
#https://www.tutorialspoint.com/python/python_gui_programming.htm
import Tkinter
import tkMessageBox
import os
import sys
import urllib

top = Tkinter.Tk()
top.title("PyKeys")

#Creating my message box data string.
data = """
Hello Everyone\n\nWelcome to our first venture into creating a GUI!!!
\n\nIf you want to know how I did this, go to this website:\n\n
https://www.tutorialspoint.com/python/python_gui_programming.htm
"""
#define the following.
def aboutCallBack():
	tkMessageBox.showinfo( "About", '%s' % data)

def vupdateCallBack():
	os.system('/home/usrname/Documents/ShortKeys/ttvup.py')
	print "Done...But keep terminal open!"

def vendCallBack():
	os.system('/home/usrname/Documents/ShortKeys/ttvend.py')
	print "Done...But keep terminal open!"

def updateCallBack():
	os.system('/home/usrname/Documents/ShortKeys/ttup2.py')
	print "Done...But keep terminal open!"

def tktopenCallBack():
	os.system('/home/usrname/Documents/ShortKeys/ttopen.py')
	print "Done...But keep terminal open!"

def tktcloseCallBack():
	os.system('/home/usrname/Documents/ShortKeys/ttclo.py')
	print "Done...But keep terminal open!"

def rtopsidCallBack():
	os.system('/home/usrname/Documents/ShortKeys/ttservice.py')
	print "Done...But keep terminal open!"

def rtopimpCallBack():
	os.system('/home/usrname/Documents/ShortKeys/ttimpact.py')
	print "Done...But keep terminal open!"
	#Dis what it's gon say at the beginning.
B = Tkinter.Button(top, text ="About this Script", command = aboutCallBack, foreground="red")
C = Tkinter.Button(top, text="Vendor Update", command = vupdateCallBack, foreground="blue")
D = Tkinter.Button(top, text="Vendor Ticket", command = vendCallBack, foreground="blue")
E = Tkinter.Button(top, text="Operator Update", command = updateCallBack, foreground="blue")
F = Tkinter.Button(top, text="Ticket Open", command = tktopenCallBack, foreground="blue")
G = Tkinter.Button(top, text="Ticket Close", command = tktcloseCallBack, foreground="blue")
H = Tkinter.Button(top, text="iRTOP SID", command = rtopsidCallBack, foreground="blue")
I = Tkinter.Button(top, text="iRTOP Impact", command = rtopimpCallBack, foreground="blue")


B.pack()
C.pack()
D.pack()
E.pack()
F.pack()
G.pack()
H.pack()
I.pack()
#you have to leave this here, so that it will always run...it's a loop
top.mainloop()
