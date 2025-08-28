from tkinter import *

class Aplicação:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text = "Interface de Login")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack()
        
root = Tk()
Aplicação(root)
root.mainloop()