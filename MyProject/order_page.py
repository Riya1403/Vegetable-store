from tkinter import *
from components.Table import *
from DatabaseHelper import *
from tkinter import messagebox
from PIL import Image,ImageTk
import datetime
class orderpage():
    def __init__(self,root,details):
        self.root=root
        self.details=details
        self.selected_items = []
        self.dct_IntVar={}
        self.root.geometry("800x600")
        self.ofr=Frame(self.root,width=1600,height=900)
        self.ofr.pack()
        self.ofr.pack_propagate(0)
        self.raw_image=Image.open("images/menu.jpg")
        self.raw_image=self.raw_image.resize((1600,900))
        self.image=ImageTk.PhotoImage(self.raw_image)
        self.panel=Label(self.ofr,image=self.image)
        self.panel.pack()
        self.panel.pack_propagate(0)
        self.m = Message(self.ofr, width=600, font=("Monotype Corsiva", 30, "bold", "italic"), text="E-Mandi",
                         bg="white", relief=SOLID, borderwidth=2)
        self.m1= Message(self.ofr, width=600, font=("Monotype Corsiva", 15, "bold", "italic"), text="HERE,TAKE A GLANCE OF ITEMS",
                         bg="white", relief=SOLID, borderwidth=2)
        self.l2 = Label(self.panel, text="@copyright2020 E-Mandi. All rights reserved.", bg="ivory3", height=1,
                        fg="black")
        self.m.place(x=650, y=20)
        self.m1.place(x=570,y=100)
        self.l2.pack(side=BOTTOM,fill=X)
        self.l2.tkraise()
        self.fr_tb=None
        self.add_buttons()
    def add_buttons(self):
        self.b1=Button(self.ofr,text="Fruits",width="30",height="1",command=lambda :self.show("Freshens"))
        self.b1.place(x=290,y=200)
        self.b2= Button(self.ofr, text="Vegetables", width="30", height="1", command=lambda :self.show("Nutritious"))
        self.b2.place(x=290, y=300)
        self.b3 = Button(self.ofr, text="Others", width="30", height="1", command=lambda :self.show("Others"))
        self.b3.place(x=290, y=400)
        self.b4 = Button(self.ofr, text="Place Order", width="30", height="1", command=self.place)
        self.b4.place(x=290, y=500)
        self.b5 = Button(self.ofr, text="Previous Order ", width="30", height="1", command=self.prev)
        self.b5.place(x=290, y=600)
    def show(self,itemType):
        param=(itemType,)
        query="""Select * from world.Menu
                 Where itemType=(%s)"""
        result=DatabaseHelper.get_all_data(query,param)
        print(result)
        if (self.fr_tb!=None):
            self.fr_tb.destroy()
        self.fr_tb=SimpleTable(self.panel,rows=len(result),columns=len(result[0]),height=250,width=600)
        self.fr_tb.place(x=650,y=200)
        self.fr_tb.grid_propagate(0)

        for i in range(len(result)):
            self.dct_IntVar[result[i][1]]=IntVar()

        for i in range(len(result)):
            for j in range(len(result[0])):
                if (j==0 and i!=0):
                    self.c=Checkbutton(self.fr_tb,text=result[i][0],variable=self.dct_IntVar.get(result[i][1]))
                    self.fr_tb.set(row=i, column=j, value=result[i][j],widget=self.c,width=20)
                else:
                    self.fr_tb.set(row=i,column=j,value=result[i][j],width=20)

    def place(self):
        for key,value in self.dct_IntVar.items():
            if(value.get()==1):
                self.selected_items.append(key)
        query="""Select itemName,itemPrice from world.Menu
                Where itemName in (%s)"""
        param=(self.selected_items)
        result=DatabaseHelper.get_all_data_multiple_input(query,param)
        print(result)
        self.fr_tb.destroy()
        self.fr_tb=SimpleTable(self.panel,rows=len(result),columns=len(result[0]),height=250,width=450)
        self.fr_tb.place(x=650,y=200)
        self.fr_tb.grid_propagate(0)
        for i in range(len(result)):
            for j in range(len(result[0])):
                self.fr_tb.set(row=i,column=j,value=result[i][j],width=20)
        self.b5 = Button(self.fr_tb, text="Confirm", width="30", height="1", command=lambda:self.submit(result))
        self.b5.grid(row=len(result),column=0)
        self.b6 = Button(self.fr_tb, text="Reset", width="30", height="1", command=self.Reset)
        self.b6.grid(row=len(result),column=1)
    def status(self):
        messagebox.showinfo("Order Placed Successfully!",f"Your order for {self.orders} for {self.TotalAmt} Rs has been sent to Admin")
        self.fr_tb.destroy()
    def submit(self,result):
        self.result=result
        """result=((FoodItem,FoodTotal),(MAngo,200),(Babuti,100),(Methi,150))"""
        orders=map(lambda x:x[0],result[1:])
        self.orders=",".join(orders)
        self.TotalAmt=sum(map(lambda x:x[1],result[1:]))
        id=self.details[0]
        param=(id,self.orders,self.TotalAmt,datetime.datetime.today().date())
        query="""Insert into world.Orders(
                 id,orders,TotalAmt,OrderDate) 
                 Values(%s,%s,%s,%s)"""
        result=DatabaseHelper.execute_query(query,param)
        self.status()
    def Reset(self):
        self.selected_items.clear()
        self.show("Freshens")
    def prev(self):
        param=(self.details[0],1)
        query="""Select orders,TotalAmt,OrderDate from world.Orders
                 Where id=%s and IsComplete=%s"""
        ress=DatabaseHelper.get_all_data(query,param)
        print(ress)
        self.prev_tb=SimpleTable(self.panel,rows=len(ress),columns=len(ress[0]),height=250,width=400)
        self.prev_tb.place(x=650,y=200)
        self.prev_tb.grid_propagate(0)
        for i in range(len(ress)):
            for j in range(len(ress[0])):
                self.prev_tb.set(row=i,column=j,value=ress[i][j],width=20)
if(__name__=='__main__'):
    root=Tk()
    root.title("Order_Page")
    root.state("zoomed")
    d=orderpage(root,(1,'Ew',7038313665,'ew'))
    root.mainloop()
