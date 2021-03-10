from tkinter import *
from DefaultPage import *
from components.Table import *
from DatabaseHelper import *
from tkinter import messagebox
class statusPage(DefaultPage):
    def __init__(self,root):
        super().__init__(root)
        self.dct_IntVar={}
        self.l1 = Label(self.f, text="HERE IS YOUR FOCUS FOR TODAY")
        self.l1.place(x=720,y=120)
        self.b=Button(self.f,text="View Orders",command=lambda:self.view_pending_orders())
        self.b.place(x=690,y=190)
        self.b1 = Button(self.f, text="Work done",command=lambda:self.view_completed_orders())
        self.b1.place(x=890, y=190)

    def view_completed_orders(self):
        query="""Select OrderId,username,orders,TotalAmt,OrderDate
               from Orders o
               Join pract_user p
               ON o.id=p.id
               WHERE IsComplete=1;"""
        result = DatabaseHelper.get_all_data(query)
        self.cmp_order = SimpleTable(self.f, rows=len(result), columns=len(result[0]), width=350, height=600)
        self.cmp_order.place(x=1030, y=10)
        self.cmp_order.grid_propagate(0)
        for i in range(len(result)):
            for j in range(len(result[0])):
                self.cmp_order.set(row=i, column=j, value=result[i][j])
    def view_pending_orders(self):
        query="""Select OrderId,username,orders,TotalAmt,OrderDate
               from Orders o
               Join pract_user p
               ON o.id=p.id
               WHERE IsComplete=0;"""
        result=DatabaseHelper.get_all_data(query)
        self.place_order=SimpleTable(self.f,rows=len(result),columns=len(result[0]),width=400,height=600)
        self.place_order.place(x=10,y=10)
        self.place_order.grid_propagate(0)
        for i in range(1,len(result)):
            self.dct_IntVar[result[i][0]]=IntVar()

        for i in range(len(result)):
            for j in range(len(result[0])):
                if i!=0 and j==0:
                    self.c=Checkbutton(self.place_order,text=result[i][0],variable=self.dct_IntVar.get(result[i][j]))
                    self.place_order.set(row=i, column=j, value=result[i][j],widget=self.c)
                else:
                    self.place_order.set(row=i,column=j,value=result[i][j])

        self.execute = Button(self.f, text="Execute_Order",command=lambda:self.execute_order())
        self.execute.place(x=550, y=220)
    def execute_order(self):
        Selected_items=[]
        for key,value in self.dct_IntVar.items():
            if(value.get()==1):
                Selected_items.append(key)
                self.dct_IntVar[key].set(0)
        if (len(Selected_items)==0):
            messagebox.showwarning("No order","Please select at_least 1 order to execute")
        else:
            query="""Update world.Orders 
                     Set IsComplete=1
                     Where OrderId in (%s)"""
            DatabaseHelper.execute_all_data_multiple_input(query,Selected_items)
            messagebox.showinfo("Success","Order Executed")
            self.view_pending_orders()
if(__name__=='__main__'):
    root=Tk()
    #root.state('zoomed')
    d=statusPage(root)
    root.mainloop()