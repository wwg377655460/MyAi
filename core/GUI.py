# coding:utf8

from Tkconstants import END, W, CURRENT, BOTTOM
import threading
import time

__author__ = 'wsdevotion'

from Tkinter import Tk, RIGHT, BOTH, RAISED, Text, Canvas, Label, PhotoImage
from ttk import Frame, Button, Style
import Assistant


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("Simple")

        self.style = Style()
        self.style.theme_use("default")



        self.textup = Text(self, width=340, height=34)
        self.textup.bind("<KeyPress>", lambda e: "break")
        self.textup.pack()

        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.frame.pack(fill=BOTH, expand=1)
        self.pack(fill=BOTH, expand=1)

        Label(self.frame,text = '', width= "350", height="1").pack()
        Label(self.frame,text = '欢迎大家', width= "350", height="1").pack()
        Label(self.frame,text = '', width= "350", height="3").pack()

        self.text = Text(self, width=340, height=3)
        self.text.bind("<Return>", self.sendMes)
        self.text.pack()
        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK",
                          command=self.onClick)
        okButton.pack(side=RIGHT)


    def onClick(self):
        str = self.text.get(1.0, END).strip()
        if str != "":

            self.printmes(str)

            self.update()
            self.assistants(str)

        else:
            print "123"


    def printmes(self, str):
        msgcontent = '\n我:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n  '
        self.textup.insert(CURRENT, msgcontent, 'green')
        self.textup.insert(CURRENT, str)
        self.text.delete("1.0", END)


    def assistants(self, str):
        retrunstr = Assistant.assistant(str)
        self.textup.insert(CURRENT, "\n机器人:\n")
        self.textup.insert(CURRENT, "  " + retrunstr)


    def sendMes(self, mes):
        # print mes
        str = self.text.get(1.0, END).strip()
        if str != "":
            self.printmes(str)
            self.update()
            self.assistants(str)
            self.text.contents = ""

        else:
            print "123"


def main():
    root = Tk()
    root.geometry("350x700+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
