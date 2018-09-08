#! coding:utf-8


from Tkinter import *
class App(Frame):
    def createWidgets(self):
        self.l1 = Label(self, text="srt name(1.srt)").grid(row=0)
        self.e1 = Entry(self)
        self.e1.grid(row=0,column=1)
        self.name = StringVar()
        self.l2 = Label(self, text="audio name(1.mp3)").grid(row=1)
        self.e2 = Entry(self)
        self.e2.grid(row=1,column=1)
        self.aname = StringVar()
        self.e1["textvariable"] = self.name
        self.b = Button(self)
        self.b['text'] = 'Submit'
        self.b.grid(row=3,column=1)
        self.b["command"] = self.say_hi
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def say_hi(self):
        print self.name.get()

root = Tk()
root.title("bubugao")
app = App(master=root)
app.mainloop()
root.destroy()
