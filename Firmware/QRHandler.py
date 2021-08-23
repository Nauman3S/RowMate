

#!/usr/bin/env python3

from os import SEEK_CUR, getlogin
import time
from PIL import Image, ImageTk
from tkinter import BitmapImage, Tk, BOTH, Canvas, StringVar, Toplevel

from tkinter.ttk import Frame, Label, Style
from tkinter.ttk import *


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    
    def movePointer(self,xy):
        self.labelpointer.place(x=xy[0], y=xy[1])
        self.labelpointer.lift()
    def initUI(self):
        
        self.master.title("Row Mate QR")
        self.pack(fill=BOTH, expand=1)
        edit_labelframe_color_style = Style()
        edit_labelframe_color_style.theme_use('clam') #only theme to handle bordercolor for labelframe
    

        Style().configure("TFrame", background="#171717", foreground="white")
        Style().configure("BW.TLabel", background="#171717", foreground="red",relief="solid",borderwidth=3,highlightbackground = "red", highlightcolor= "red", highlightthickness=3)
        
        self.pointer=Image.open("pointer.png")
        self.pointer = self.pointer.resize((30, 30), Image.ANTIALIAS)
        self.pointerjov = ImageTk.PhotoImage(self.pointer)
        self.labelpointer = Label(self, image=self.pointerjov, borderwidth=0)
        self.labelpointer.image = self.pointerjov
        self.labelpointer.place(x=300, y=80)
        self.labelpointer.lift()


        bard = Image.open("rowmateLogo.png")
        bard = bard.resize((100, 100), Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov, borderwidth=0)
        label1.image = bardejov
        label1.place(x=700, y=-10)

        bard2 = Image.open("rowmate.png")
        bard2 = bard2.resize((200, 100), Image.ANTIALIAS)
        bardejov2 = ImageTk.PhotoImage(bard2)
        label2 = Label(self, image=bardejov2, borderwidth=0)
        label2.image = bardejov2
        label2.place(x=0, y=-10)


        QRIMG = Image.open("qr.png")
        #bard = bard.resize((100, 100), Image.ANTIALIAS)
        qrJ = ImageTk.PhotoImage(QRIMG)
        qrCD = Label(self, image=qrJ, borderwidth=0)
        qrCD.image = qrJ
        qrCD.place(x=50, y=110)

        notiF = Label(self, text="Scan this QR with RowMate App", borderwidth=0,font=("Helvetica", 12), background="#171717",foreground="#fff")
        notiF.place(x=500,y=100)


        btn = Button(self,
             text ="<-Back",
             command = self.exitQRWindow)
        btn.place(x=50, y=410)

        self.labelpointer.place(x=10, y=410)

       
    def setQRCode(self,v):
        self.qrcodev=v
    def getQRCode(self):
        return self.qrcodev
    def exitQRWindow(self):
        # self.destroy()
        exit(0)
    
root = None
app= None
def configUI():
    global root,app
    root = Tk()
    #root.geometry("800x480+0+0")
    root.attributes('-zoomed', True) 
    app = Example()
def setQRCode(value):
    global app
    app.setQRCode(value)
# def quitQRWindow():
#     global app
#     app.exitQRWindow()

configUI()
timeCount=0
exitTime=7.0
def mainUI():
    
    global root, app, timeCount,exitTime
    

    #root.mainloop()

    try:
        while 1:
            
            timeCount=timeCount+0.1
            if(timeCount>exitTime):
                exit(0)
            time.sleep(0.1)
            print(timeCount)
            root.update()
            
       
        
  
    except Exception as e:
        print(e)
        
        exit(0)

if __name__ == '__main__':
    mainUI()
