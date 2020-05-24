import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Manual Upload Test")
        self.master.minsize(400,400)
        self.master.maxsize(1000,400)
        self.pack()
        self.create_widgets()
        self.create_frame()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="left")
        
    def create_frame(self):
        optionList = ('train', 'plane', 'boat')
        self.v = tk.StringVar(self)
        self.v.set(optionList[0])
        self.om = tk.OptionMenu(self, self.v, *optionList)

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()