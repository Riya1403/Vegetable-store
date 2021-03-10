from tkinter import *
from tkinter import messagebox
from DatabaseHelper import *
from DefaultPage import *
import smtplib
class marketPage(DefaultPage):
    def __init__(self,root):
        super().__init__(root)
        self.root.title("Market")
        self.market()
    def market(self):
        self.b=Button(self.f,text="Owner",command=lambda:self.owner_page())
        self.b1=Button(self.f,text="Already_Customer",command=lambda:self.customer_page())
        self.b2 = Button(self.f, text="New_Customer", command=lambda: self.newcustomer_page())
        self.b.place(x=600,y=250,width=95,height=75)
        self.b1.place(x=800,y=250,width=105,height=75)
        self.b2.place(x=1000,y=250,width=95,height=75)
    def newcustomer_page(self):
        self.temproot = Toplevel()
        self.tfr = Frame(self.temproot, width="700", height="250", bg="ivory3")
        self.tfr.pack()
        self.l1 = Label(self.tfr, text="PLEASE CREATE ACCOUNT TO GET FRESH GROCERIES")
        self.l1.grid(row=0, column=0, padx=10, pady=10)
        self.l2 = Label(self.tfr, text="Enter name")
        self.l2.grid(row=1, column=0, padx=10, pady=10)
        self.e_name = Entry(self.tfr, width="30", fg="Black", bg="White")
        self.e_name.grid(row=1, column=1, padx=10, pady=10)
        self.l3 = Label(self.tfr, text="Enter contact")
        self.l3.grid(row=2, column=0, padx=10, pady=10)
        self.e_contact = Entry(self.tfr, width="30", fg="Black", bg="White")
        self.e_contact.grid(row=2, column=1, padx=10, pady=10)
        self.l4= Label(self.tfr, text="Set password for your Account")
        self.l4.grid(row=3, column=0, padx=10, pady=10)
        self.e_pwd = Entry(self.tfr, width="50", fg="Black", bg="White",show="*")
        self.e_pwd.grid(row=3, column=1, padx=10, pady=10)
        self.b = Button(self.tfr, text="Submit", command=lambda: self.register(self.e_name.get(),self.e_contact.get(),self.e_pwd.get()))
        self.b.grid(row=4, column=0, padx=10, pady=10)
        self.b1 = Button(self.tfr, text="Reset", command=lambda: self.Reset2())
        self.b1.grid(row=4, column=1, padx=10, pady=10)
        self.tfr.grid_propagate(0)

    def register(self,username,contact,password):
        params=(username,contact,password)
        query="""Insert into pract_user(username,Contact,password)
                 Values((%s),(%s),SHA(%s))"""
        DatabaseHelper.execute_query(query,params)
        messagebox.showinfo("Welcome","Your Account has been Created")
        import order_page
        self.panel.destroy()
        self.tfr.destroy()
        self.f.destroy()
        self.o = order_page.orderpage(self.root)

    def owner_page(self):
        self.troot = Toplevel()
        self.tf=Frame(self.troot,width="700",height="300",bg="lightblue")
        self.tf.pack()
        self.l1= Label(self.tf, text="ENTER PIN TO TAKE YOU SHOPWAY")
        self.l1.grid(row=0, column=0,padx=10,pady=10)
        self.e_pin=Entry(self.tf,width="30",fg="Black",bg="White",show="*")
        self.e_pin.grid(row=0, column=1,padx=10,pady=10)
        self.b = Button(self.tf, text="Submit", command=lambda: self.check(self.e_pin.get()))
        self.b.grid(row=1,column=0,padx=10,pady=10)
        self.b1= Button(self.tf, text="Reset", command=lambda: self.Reset())
        self.b1.grid(row=1, column=1, padx=10, pady=10)
        self.tf.grid_propagate(0)
    def check(self,e_pin):
        query="select * from practice_market where pin= SHA(%s)"
        res = DatabaseHelper.get_data(query,e_pin)
        if (len(res)==0 or res==None):
            messagebox.showerror("Invalid Pin","Don't Fraud With Owner!")
            self.troot.tkraise()
            self.Reset()
        else:
            messagebox.showinfo("Success", "WELCOME!")
            self.troot.destroy()
            self.f.destroy()
            self.panel.destroy()
            import status_page
            self.s=status_page.statusPage(self.root)
    def Reset(self):
        self.e_pin.delete(0, END)
    def Reset1(self):
        self.e_name.delete(0, END)
        self.e_password.delete(0,END)
    def Reset2(self):
        self.e_name.delete(0, END)
        self.e_password.delete(0,END)
        self.e_contact.delete(0,END)
    def customer_page(self):
        self.tproot = Toplevel()
        self.tfr= Frame(self.tproot, width="700", height="250", bg="ivory3")
        self.tfr.pack()
        self.l1=Label(self.tfr, text="PLEASE LOGIN TO GET FRESH GROCERIES")
        self.l1.grid(row=0, column=1, padx=10, pady=10)
        self.l2= Label(self.tfr, text="Enter name")
        self.l2.grid(row=1, column=0, padx=10, pady=10)
        self.e_name = Entry(self.tfr, width="30", fg="Black", bg="White")
        self.e_name.grid(row=1, column=1, padx=10, pady=10)
        self.l3= Label(self.tfr, text="Enter password")
        self.l3.grid(row=2, column=0, padx=10, pady=10)
        self.e_password = Entry(self.tfr, width="50", fg="Black", bg="White",show="*")
        self.e_password.grid(row=2, column=1, padx=10, pady=10)
        self.bt = Button(self.tfr, text="Forgot password", command=lambda:self.forgot(self.e_name.get()))
        self.bt.grid(row=3, column=1, padx=10, pady=10)
        self.b = Button(self.tfr, text="Submit", command=lambda: self.login(self.e_name.get(),self.e_password.get()))
        self.b.grid(row=4, column=0, padx=10, pady=10)
        self.b1 = Button(self.tfr, text="Reset", command=lambda: self.Reset1())
        self.b1.grid(row=4, column=1, padx=10, pady=10)
        self.tfr.grid_propagate(0)
    def forgot(self,username):
        self.tproot.destroy()
        self.e_name=username
        self.tmproot = Toplevel()
        self.tmfr = Frame(self.tmproot, width="700", height="350", bg="ivory3")
        self.tmfr.pack()
        self.lb = Label(self.tmfr, text="KINDLY DO THE FOLLOWING:")
        self.lb.grid(row=0, column=1, padx=10, pady=10)
        self.lb1 = Label(self.tmfr, text="Set new password")
        self.lb1.grid(row=1, column=0, padx=10, pady=10)
        self.e_newpassword = Entry(self.tmfr, width="50", fg="Black", bg="White", show="*")
        self.e_newpassword.grid(row=1, column=1, padx=10, pady=10)
        self.lb2 = Label(self.tmfr, text="Confirm new password")
        self.lb2.grid(row=2, column=0, padx=10, pady=10)
        self.e_cpassword = Entry(self.tmfr, width="50", fg="Black", bg="White", show="*")
        self.e_cpassword.grid(row=2, column=1, padx=10, pady=10)
        self.lb3 = Label(self.tmfr, text="Enter Valid E-mail")
        self.lb3.grid(row=3, column=0, padx=10, pady=10)
        self.e_email = Entry(self.tmfr, width="50", fg="Black", bg="White")
        self.e_email.grid(row=3, column=1, padx=10, pady=10)
        self.btn = Button(self.tmfr, text="Submit", command=lambda:self.setp(self.e_name,self.e_cpassword.get(),self.e_email.get()))
        self.btn.grid(row=4, column=0, padx=10, pady=10)
        self.btn1 = Button(self.tmfr, text="Back", command=self.back)
        self.btn1.grid(row=4, column=1, padx=10, pady=10)
    def back(self):
        self.tmproot.destroy()
        self.customer_page()
    def setp(self,username,newp,email):
        self.username=username
        self.emailid=email
        params=(newp,username)
        query="""Update pract_user
                 set password=%s
                 Where username=%s"""
        op=DatabaseHelper.execute_query(query,params)
        print(op)
        messagebox.showinfo("wooho!","password changed successfully")
        self.mail(self.username,self.emailid)
    def mail(self,username,emailid):
        sender_add="2018.riya.matwani@ves.ac.in"
        pwd="Riya@12345"
        reciever_add=emailid
        message="Thankyouu being a part of E-Mandi!" \
                 f"{username} your account's password changed right now" \
                 "If it was not you.kindly revert us back!" \
                 "Your pleasure!"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_add, pwd)
        server.sendmail(sender_add, reciever_add,message)
        messagebox.showwarning("Attention!","Kindly check your mailbox.")
    def login(self,username,pwd):
        query = "select * from pract_user where username=(%s) And password= SHA(%s)"
        params=(username,pwd)
        res = DatabaseHelper.get_data(query,params)
        if ( res == None or len(res) == 0):
            messagebox.showerror("Invalid Details", "Please Try Again!")
            self.tproot.tkraise()
            self.Reset1()
        else:
            messagebox.showinfo("Login Success", "WELCOME!")
            self.tproot.destroy()
            self.tfr.destroy()
            import order_page
            self.o = order_page.orderpage(self.root,res)
if(__name__=='__main__'):
    root=Tk()
    #root.state('zoomed')
    marketPage(root)
    root.mainloop()
