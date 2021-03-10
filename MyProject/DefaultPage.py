from tkinter import *
from PIL import Image,ImageTk
class DefaultPage:
    def __init__(self,root):
        self.root=root
        self.root.title("Market")
        self.f=Frame(self.root,width=1600,height=900)
        self.f.pack()
        self.raw_image=Image.open("images/Market.jpg")
        self.raw_image=self.raw_image.resize((1600,900))
        self.img=ImageTk.PhotoImage(self.raw_image)
        self.panel=Label(self.f,image=self.img)
        self.panel.pack()
        self.panel.pack_propagate(0)
        self.f.pack_propagate(0)
        self.m = Message(self.f, width=600, font=("Monotype Corsiva", 30, "bold", "italic"), text="E-Mandi",
                         bg="white", relief=SOLID, borderwidth=2)
        self.l2=Label(self.panel,text="@copyright2020 E-Mandi. All rights reserved.",bg="ivory3",height=1,fg="black")
        self.m.place(x=725,y=20)
        self.l2.pack(side=BOTTOM,fill=X)
        self.l2.tkraise()
if(__name__=='__main__'):
    root=Tk()
    #root.state('zoomed')
    d=DefaultPage(root)
    root.mainloop()