

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
    
    def set_total_time_elapsed(self,v):
        self.total_time_elapsed.set(v)
    def set_strokes_PM(self,v):
        self.strokes_PM.set(v)
    def set_split_time(self,v):
        self.Split_Time.set(v)
    def set_total_meters(self,v):
        self.Total_Meters.set(v)
    def set_avg_split_time(self,v):
        self.Average_Split_Time.set(v)
    def set_split_meters(self,v):
        self.Split_Meters.set(v)
    def set_projected_distance(self,v):
        self.Projected_Distance.set(v)
    def set_latt_lng(self,v):
        self.latt_lng.set(v)
    def movePointer(self,xy):
        self.labelpointer.place(x=xy[0], y=xy[1])
        self.labelpointer.lift()
    def initUI(self):
        self.total_time_elapsed = StringVar()
        self.strokes_PM=StringVar()
        self.Split_Time=StringVar()
        self.Total_Meters=StringVar()
        self.Average_Split_Time=StringVar()
        self.Split_Meters=StringVar()
        self.Projected_Distance=StringVar()
        self.latt_lng=StringVar()

        self.total_time_elapsed.set("TotalTE")
        self.strokes_PM.set("Strokes Per Minute")
        self.Split_Time.set("Split time")
        self.Total_Meters.set("Total Meters")
        self.Average_Split_Time.set("Avergae Split Time")
        self.Split_Meters.set("Split Meters")
        self.Projected_Distance.set("Projected Meters at current pace")
        self.latt_lng.set("Latt,Lng")

        self.master.title("Row Mate")
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

        frame1 = Frame(self, width=500, height=60, style="BW.TLabel")
        frame1.place(x=0, y=80)
        timeElapsed = Label(frame1, textvariable=self.total_time_elapsed, borderwidth=0,font=("Helvetica", 15), background="#171717",foreground="#fff")
        timeElapsed.place(x=140,y=15)
        

        frame1_1 = Frame(self, width=250, height=60, style="BW.TLabel")
        frame1_1.place(x=510, y=80)
        strokesPM = Label(frame1_1, textvariable=self.strokes_PM , borderwidth=0,font=("Helvetica", 15), background="#171717",foreground="#fff")
        strokesPM.place(x=80,y=15)


        frame2 = Frame(self, width=790, height=60, style="BW.TLabel")
        frame2.place(x=0, y=145)
        SplitTime = Label(frame2, textvariable=self.Split_Time, borderwidth=0,font=("Helvetica", 15), background="#171717",foreground="#fff")
        SplitTime.place(x=300,y=15)


        frame3 = Frame(self, width=500, height=60, style="BW.TLabel")
        frame3.place(x=0, y=210)
        TotalMeters = Label(frame3, textvariable=self.Total_Meters, borderwidth=0,font=("Helvetica", 15), background="#171717",foreground="#fff")
        TotalMeters.place(x=200,y=15)
        

        frame3_1 = Frame(self, width=250, height=60, style="BW.TLabel")
        frame3_1.place(x=510, y=210)
        LattLng = Label(frame3_1, textvariable=self.latt_lng, borderwidth=0,font=("Helvetica", 15), background="#171717",foreground="#fff")
        LattLng.place(x=80,y=15)


        frame4 = Frame(self, width=790, height=60, style="BW.TLabel")
        frame4.place(x=0, y=275)
        AverageSplitTime = Label(frame4, textvariable=self.Average_Split_Time, borderwidth=0,font=("Helvetica", 15), background="#171717",foreground="#fff")
        AverageSplitTime.place(x=300,y=15)

        frame5 = Frame(self, width=790, height=60, style="BW.TLabel")
        frame5.place(x=0, y=340)
        SplitMeters = Label(frame5, textvariable=self.Split_Meters, borderwidth=0,font=("Helvetica", 15), background="#171717",foreground="#fff")
        SplitMeters.place(x=300,y=15)

        frame6 = Frame(self, width=790, height=60, style="BW.TLabel")
        frame6.place(x=0, y=405)
        ProjectedDistance = Label(frame6, textvariable=self.Projected_Distance, borderwidth=0,font=("Helvetica", 15), background="#171717",foreground="#fff")
        ProjectedDistance.place(x=300,y=15)
        self.labelpointer.lift()

        btn = Button(frame6,
             text ="Connect to App",
             command = self.QRWindow)
        btn.place(x=500, y=15)
    def setQRCode(self,v):
        self.qrcodev=v
    def getQRCode(self):
        return self.qrcodev
    def exitQRWindow(self):
        self.qrw.destroy()
    def QRWindow(self):
        self.qrw = Toplevel(self)
        self.qrw.title("Connect to the RowMate App")
        self.qrw.geometry("800x480+400+240")
        
        QRIMG = Image.open("qr.png")
        #bard = bard.resize((100, 100), Image.ANTIALIAS)
        qrJ = ImageTk.PhotoImage(QRIMG)
        qrCD = Label(self.qrw, image=qrJ, borderwidth=0)
        qrCD.image = qrJ
        qrCD.place(x=50, y=50)

        notiF = Label(self.qrw, text="Scan this QR with RowMate App", borderwidth=0,font=("Helvetica", 12), background="#171717",foreground="#fff")
        notiF.place(x=500,y=100)


        btn = Button(self.qrw,
             text ="<-Back",
             command = self.exitQRWindow)
        btn.place(x=50, y=400)
root = None
app= None
def configUI():
    global root,app
    root = Tk()
    root.geometry("800x480+400+240")
    app = Example()
widgetsPos=[[0,80],[510,80],[0,145],[0,210],[510,210],[0,275],[0,340],[0,405],[470,415]]
# currPos=0
# def moveCursor(frV):
#     global currPos,widgetsPos
#     if(frV>=0 and frV<=7):
#         currPos=frV
#         return widgetsPos[frV]
        
def setQRCode(value):
    global app
    app.setQRCode(value)
# def quitQRWindow():
#     global app
#     app.exitQRWindow()



def mainUI(totalTimeElapsed, strokespm, splittime,totalmeters,avgsplittime,splitmeters,projecteddistance,latlng,curpos):
    
    global root, app
    

    #root.mainloop()

    try:
        root.update()
        app.set_total_time_elapsed(str(totalTimeElapsed))
        app.set_strokes_PM(str(strokespm))
        app.set_split_time(str(splittime))
        app.set_total_meters(str(totalmeters))
        app.set_avg_split_time(str(avgsplittime))
        app.set_split_meters(str(splitmeters))
        app.set_projected_distance(str(projecteddistance))
        app.set_latt_lng(str(latlng))
        app.movePointer(curpos)
        #print('ep',enterpoll)
        
  
    except Exception as e:
        print(e)
        
        root.quit()
        root.update()
        exit(0)

# if __name__ == '__main__':
#     mainUI()
