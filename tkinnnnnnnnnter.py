
#===============importing things================

import tkinter as tk
import time

#==============some constants===================

y = time.asctime(time.localtime()).split(" ")[3].split(":")
x = 0

#==============Main class========================

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "How much clicks"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

    def say_hi(self):
        global x
        x+=1

#==============spagetti code===============================

root = tk.Tk()
app = Application(master=root)
app.mainloop()
z = time.asctime(time.localtime()).split(" ")[3].split(":")
w = int(z[-1]) - int(y[-1])
if x/w > 0:
    print(round(x/w, 2), end = "")
else:
    print(-round(x/w, 2) ,end = "")
print(" cps")
input()
