

#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this script, we lay out images
using absolute positioning.

Author: Jan Bodnar
Website: www.zetcode.com
"""

from PIL import Image, ImageTk
from tkinter import Tk, BOTH, Canvas

from tkinter.ttk import Frame, Label, Style
from tkinter.ttk import *

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Row Mate")
        self.pack(fill=BOTH, expand=1)
        edit_labelframe_color_style = Style()
        edit_labelframe_color_style.theme_use('clam') #only theme to handle bordercolor for labelframe
    

        Style().configure("TFrame", background="#171717")
        Style().configure("BW.TLabel", background="#171717", foreground="red",relief="solid",borderwidth=3,highlightbackground = "red", highlightcolor= "red", highlightthickness=3)

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

        frame1_1 = Frame(self, width=250, height=60, style="BW.TLabel")
        frame1_1.place(x=510, y=80)

        frame2 = Frame(self, width=790, height=60, style="BW.TLabel")
        frame2.place(x=0, y=145)


        frame3 = Frame(self, width=500, height=60, style="BW.TLabel")
        frame3.place(x=0, y=210)

        frame3_1 = Frame(self, width=250, height=60, style="BW.TLabel")
        frame3_1.place(x=510, y=210)

        frame4 = Frame(self, width=790, height=60, style="BW.TLabel")
        frame4.place(x=0, y=275)

        frame5 = Frame(self, width=790, height=60, style="BW.TLabel")
        frame5.place(x=0, y=340)

        frame6 = Frame(self, width=790, height=60, style="BW.TLabel")
        frame6.place(x=0, y=405)
       


def main():

    root = Tk()
    root.geometry("800x480+400+240")
    app = Example()
    
    root.mainloop()


if __name__ == '__main__':
    main()
