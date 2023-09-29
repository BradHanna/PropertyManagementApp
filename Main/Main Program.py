import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
import tkinter.messagebox
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Property App")
        self.resizable(width=True, height=True)

        container = tk.Frame(self)
        container.grid(row=0, column = 0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (PropertyLogin, MainView, PropertyView, NewAccount, Tenant, View2, Account2, StaffView, FinanceView, JobView, View3, JobView2, Request):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(PropertyLogin)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        

class PropertyLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.frame = Frame(self, bg="dodgerblue", relief = RIDGE, bd=25, height = 1000, width=1440)
        self.frame.grid(row=0, column=0)

        self.username_verify = StringVar()
        self.password_verify = StringVar()
        self.controller = controller

        self.lblTitle = Label(self.frame, text = "Property Management Login System", font=("Arial",60,"bold"),
                              bg="dodgerblue", fg="black")
        self.lblTitle.grid(row =0, column =0, columnspan=2, pady =20)

        self.LoginFrame1 = LabelFrame(self.frame , width = 1350, height = 400
                                      ,font = ("Arial",20,"bold"),relief="ridge",bg="dodgerblue2", bd=40)
        self.LoginFrame1.grid(row=1, column=1)

        self.LoginFrame2 = LabelFrame(self.frame , width=1000,height=200
                                      ,font=("Arial",20,"bold"),relief="ridge",bg="dodgerblue2", bd=40)
        self.LoginFrame2.grid(row=2, column=1)

        self.lblUsername =Label(self.LoginFrame1, text="Username",font=("Arial",30,"bold"),bd=22,
                                bg="dodgerblue2", fg="black")
        self.lblUsername.grid(row=0, column=0)
        
        self.txtUsername =Entry(self.LoginFrame1,font=("Arial",30,"bold"),bd=7,textvariable=self.username_verify,
                                width=33)
        self.txtUsername.grid(row=0, column=1, padx=88)

        self.lblPassword = Label(self.LoginFrame1,text="Password",font=("Arial",30,"bold"),bd=22,
                                 bg="dodgerblue2", fg="black")
        self.lblPassword.grid(row=1, column=0)

        self.txtPassword= Entry(self.LoginFrame1,font=("Arial",30,"bold"),show= "*",bd=7,textvariable=self.password_verify,
                                width=33)
        self.txtPassword.grid(row=1, column=1, columnspan=2, pady=30)

        self.lblNew = Label(self.frame, text="Dont have an account?",font=("Arial",19),bg="dodgerblue")
        self.lblNew.place(x=430, y=668)

        self.btnLogin = Button(self.LoginFrame2, text = "Login", width = 15,font=("Arial",30,"bold"),
                               bg="dodgerblue2", fg="black", command=self.login_verify)
        self.btnLogin.grid(row=3, column =0, pady=20, padx=8)

        self.btnReset = Button(self.LoginFrame2, text = "Reset", width = 15,font=("Arial",30,"bold"),
                               bg="dodgerblue2", fg="black", command=self.Reset)
        self.btnReset.grid(row=3, column=1, pady=20, padx=8)

        self.btnExit = Button(self.LoginFrame2, text = "Exit", width = 15, font=("Arial",30,"bold"),
                              bg="dodgerblue2", fg="black", command=self.Exit)
        self.btnExit.grid(row=3, column=2, pady=20, padx=8)

        self.btnNew = Button(self.frame, text = "Sign Up", width = 6, height = 0, font=("Arial",18,"bold"),
                             bg="dodgerblue2", fg="black", command=lambda:controller.show_frame(NewAccount))
        self.btnNew.place(x=700, y=660)

        self.btnG = Button(self.frame, width=20, height = 10, bg="dodgerblue", bd = False)
        self.btnG.grid(row=8, column = 8)

        
        

    def login_verify(self):
        self.username1 = self.username_verify.get()
        self.password1 = self.password_verify.get()
        self.view1 = str(1)
        self.view2 = str(2)
        self.view3 = str(3)
        self.txtUsername.delete(0, END)
        self.txtPassword.delete(0, END)

        list_of_files = os.listdir()
        if self.username1 in list_of_files:
            file1 = open(self.username1, "r")
            verify = file1.read().splitlines()
            if self.password1 in verify:
                if self.view1 in verify:
                    self.controller.show_frame(View2)
                elif self.view2 in verify:
                    self.controller.show_frame(View3)
                elif self.view3 in verify:
                    self.controller.show_frame(MainView)
                else:
                    tkinter.messagebox.showinfo("Property Management System", "Unauthorised Access Level")
            else:
                tkinter.messagebox.showinfo("Property Management System", "Password not recognised")
        else:
            tkinter.messagebox.showinfo("Property Management System", "User not found")

    def Reset(self):
        self.username_verify.set("")
        self.password_verify.set("")

    
    def Exit(self):
        self.Exit = tkinter.messagebox.askyesno("Property Management System", "Confrim if you want to exit")
        if self.Exit > 0:
            self.frame.destroy()
            return

class NewAccount(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.MainFrame = Frame(self, bd=25, width = 1600, height = 820, relief = RIDGE, bg = "dodgerblue")
        self.MainFrame.grid(row=0, column=0)

        self.Username = StringVar()
        self.Password = StringVar()
        self.Confirm = StringVar()

        self.MainFrame1 = Frame(self.MainFrame, bd=22, width=500, height=600, relief= RIDGE, bg = "dodgerblue")
        self.MainFrame1.place(x=100,y=110)

        self.lblTitle = Label(self.MainFrame, font=("Arial", 55, "bold"), text="Create Account", bg = "dodgerblue", anchor = "c")
        self.lblTitle.place(x=550,y=0)

        self.lblUsername =Label(self.MainFrame1, text="Username",font=("Arial",30,"bold"),bd=25,
                                bg="dodgerblue", fg="black")
        self.lblUsername.grid(row=0, column=0)
        
        self.txtUsername =Entry(self.MainFrame1,font=("Arial",30,"bold"),bd=7,textvariable=self.Username,
                                width=33)
        self.txtUsername.grid(row=0, column=1, padx=88)

        self.lblPassword = Label(self.MainFrame1,text="Password",font=("Arial",30,"bold"),bd=22,
                                 bg="dodgerblue", fg="black")
        self.lblPassword.grid(row=1, column=0)

        self.txtPassword= Entry(self.MainFrame1,font=("Arial",30,"bold"),show= "*",bd=7,textvariable=self.Password,
                                width=33)
        self.txtPassword.grid(row=1, column=1, columnspan=2, pady=30)

        self.lblConfirm = Label(self.MainFrame1,text="Confirm Password",font=("Arial",30,"bold"),bd=22,
                                 bg="dodgerblue", fg="black")
        self.lblConfirm.grid(row=2, column=0)

        self.txtConfirm= Entry(self.MainFrame1,font=("Arial",30,"bold"),show= "*",bd=7,textvariable=self.Confirm,
                                width=33)
        self.txtConfirm.grid(row=2, column=1, columnspan=2, pady=30)

        self.btnReg = Button(self.MainFrame, text = "Register", width = 15, font=("Arial",30,"bold"),
                              bg="dodgerblue2", fg="black", command=self.Reg)
        self.btnReg.place(x=10,y=500)

        self.btnBack = Button(self.MainFrame, text = "Back", width = 8, font=("Arial",30,"bold"), bg="dodgerblue2", fg="black", command=lambda:controller.show_frame(PropertyLogin))
        self.btnBack.place(x=10,y=10)


    def Reg(self):

        username_info = self.Username.get()
        password_info = self.Password.get()
        confirm_info = self.Confirm.get()
        view_info = str(1)
        if password_info == confirm_info:
            file=open(username_info, "w")
            file.write(username_info+"\n")
            file.write(password_info+"\n")
            file.write(view_info)
            file.close()
            tkinter.messagebox.showinfo("Property Management System", "Registration Success")
            self.txtUsername.delete(0, END)
            self.txtPassword.delete(0, END)
            self.txtConfirm.delete(0, END)
        else:
            tkinter.messagebox.showinfo("Property Management System", "Entered passwords do not match, please try again.")
            self.txtPassword.delete(0, END)
            self.txtConfirm.delete(0, END)

class Account2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.MainFrame = Frame(self, bd=25, width = 1600, height = 820, relief = RIDGE, bg = "dodgerblue")
        self.MainFrame.grid(row=0, column=0)

        self.Username = StringVar()
        self.Password = StringVar()
        self.Confirm = StringVar()

        self.MainFrame1 = Frame(self.MainFrame, bd=30, width=500, height=600, relief= RIDGE, bg = "dodgerblue")
        self.MainFrame1.place(x=100,y=110)

        self.lblTitle = Label(self.MainFrame, font=("Arial", 55, "bold"), text="Create Account For Staff", bg = "dodgerblue", anchor = "c")
        self.lblTitle.place(x=480,y=0)

        self.lblUsername =Label(self.MainFrame1, text="Username",font=("Arial",30,"bold"),bd=25,
                                bg="dodgerblue", fg="black")
        self.lblUsername.grid(row=0, column=0)
        
        self.txtUsername =Entry(self.MainFrame1,font=("Arial",30,"bold"),bd=7,textvariable=self.Username,
                                width=33)
        self.txtUsername.grid(row=0, column=1, padx=88)

        self.lblPassword = Label(self.MainFrame1,text="Password",font=("Arial",30,"bold"),bd=22,
                                 bg="dodgerblue", fg="black")
        self.lblPassword.grid(row=1, column=0)

        self.txtPassword= Entry(self.MainFrame1,font=("Arial",30,"bold"),show= "*",bd=7,textvariable=self.Password,
                                width=33)
        self.txtPassword.grid(row=1, column=1, columnspan=2, pady=30)

        self.lblConfirm = Label(self.MainFrame1,text="Confirm Password",font=("Arial",30,"bold"),bd=22,
                                 bg="dodgerblue", fg="black")
        self.lblConfirm.grid(row=2, column=0)

        self.txtConfirm= Entry(self.MainFrame1,font=("Arial",30,"bold"),show= "*",bd=7,textvariable=self.Confirm,
                                width=33)
        self.txtConfirm.grid(row=2, column=1, columnspan=2, pady=30)

        self.btnReg = Button(self.MainFrame, text = "Register", width = 15, font=("Arial",30,"bold"),
                              bg="dodgerblue2", fg="black", command=self.Reg)
        self.btnReg.place(x=10,y=500)

        self.btnBack = Button(self.MainFrame, text = "Back", width = 8, font=("Arial",30,"bold"), bg="dodgerblue2", fg="black", command=lambda:controller.show_frame(MainView))
        self.btnBack.place(x=10,y=10)


    def Reg(self):

        username_info = self.Username.get()
        password_info = self.Password.get()
        confirm_info = self.Confirm.get()
        view_info = str(2)
        if password_info == confirm_info:
            file=open(username_info, "w")
            file.write(username_info+"\n")
            file.write(password_info+"\n")
            file.write(view_info)
            file.close()
            tkinter.messagebox.showinfo("Property Management System", "Registration Success")
            self.txtUsername.delete(0, END)
            self.txtPassword.delete(0, END)
            self.txtConfirm.delete(0, END)
        else:
            tkinter.messagebox.showinfo("Property Management System", "Entered passwords do not match, please try again.")
            self.txtPassword.delete(0, END)
            self.txtConfirm.delete(0, END)
    
    
        
class MainView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        blank_space = " "
        

        MainFrame = Frame(self, bd=25, width = 1590, height = 840, relief = RIDGE, bg = "dodgerblue")
        MainFrame.grid(row=0, column=0)

        TopFrame = Frame(MainFrame, bd = 7, width = 1540, height = 165, relief = RIDGE)
        TopFrame.place(x=0, y=0)

        self.lblTitle = Label(TopFrame, font=("Arial", 40,"bold"), text="Dashboard", bd=7, anchor = "w", justify=LEFT)
        self.lblTitle.place(x=600, y=0)

        self.btnAccount = Button(TopFrame, pady = 1, bd = 4, font=("Arial",15, "bold"), text = "Create Account", padx = 24, width = 13, height = 1, command=lambda:controller.show_frame(Account2), relief = RAISED)\
                            .place(x=0, y=100)
        self.btnProperty = Button(TopFrame, pady = 1, bd = 4, font=("Arial",15, "bold"), text = "Properties", padx = 24, width = 13, height = 1, command=lambda:controller.show_frame(PropertyView), relief = RAISED)\
                            .place(x=220, y=100)
        self.btnTenants = Button(TopFrame, pady = 1, bd = 4, font=("Arial",15, "bold"), text = "Tenants", padx = 24, width = 13, height = 1, command=lambda:controller.show_frame(Tenant), relief = RAISED)\
                            .place(x=440, y=100)
        self.btnTenancies = Button(TopFrame, pady = 1, bd = 4, font=("Arial",15, "bold"), text = "Tenancies", padx = 24, width = 13, height = 1, relief = RAISED)\
                            .place(x=660, y=100)
        self.btnFinance = Button(TopFrame, pady = 1, bd = 4, font=("Arial",15, "bold"), text = "Finance", padx = 24, width = 13, height = 1, command=lambda:controller.show_frame(FinanceView), relief = RAISED)\
                            .place(x=880, y=100)
        self.btnStaff = Button(TopFrame, pady = 1, bd = 4, font=("Arial",15, "bold"), text = "Maintenance Staff", padx = 24, width =13, height = 1, command=lambda:controller.show_frame(StaffView), relief = RAISED)\
                            .place(x=1100, y=100)
        self.btnMaintenance = Button(TopFrame, pady = 1, bd = 4, font=("Arial",15, "bold"), text = "Repair Requests", padx = 24, width = 12, height = 1, command=lambda:controller.show_frame(JobView), relief = RAISED)\
                            .place(x=1320, y=100)
        self.btnLogout = Button(TopFrame, pady = 1, bd=4, font=("Arial",15, "bold"), text = "Log Out", padx = 24, width = 10, height = 1,  command=lambda:controller.show_frame(PropertyLogin), relief = RAISED)\
                            .place(x=0,y=0)
        self.btnEmail = Button(MainFrame, pady = 1, bd= 4, font=("Arial",15, "bold"), text = "Send Email", padx = 24, width = 10, height = 1, command=self.Email, relief = RIDGE)\
                            .place(x=300,y=500)

    def Email(self):
        self.sender_email = "HannaProperties0@gmail.com"
        self.receiver_email = "HannaProperties0@gmail.com"
        self.password = "Coursework1!"

        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "multipart test"
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email

        text = """\
                Hi,
                Unfortunantely our email services are under maintenace, thank you for your pateince!
               """
        html =  """
                <html>
                    <body>
                    <p>Hi,<br>
                        Unfortunantely our email services are under maintenace, thank you for your pateince!
                    </p>
                    </body>
                </html>
                """

        self.part1 = MIMEText(text, "plain")
        self.part2 = MIMEText(html, "html")

        self.message.attach(self.part1)
        self.message.attach(self.part2)

        self.context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(
                self.sender_email, self.receiver_email, self.message.as_string()
                )
        tkinter.messagebox.showinfo("Property Management System", "Email sent successfully")
            
        

class View2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        blank_space = " "

        MainFrame = Frame(self, bd=25, width = 1590, height = 840, relief = RIDGE, bg = "dodgerblue")
        MainFrame.grid(row=0, column=0)

        TopFrame = Frame(MainFrame, bd = 7, width = 1540, height = 165, relief = RIDGE)
        TopFrame.place(x=0, y=0)

        self.lblTitle = Label(TopFrame, font=("Arial", 40,"bold"), text=" Tenant Dashboard", bd=7, anchor = "w", justify=LEFT)
        self.lblTitle.place(x=600, y=0)

        self.btnDashboard = Button(TopFrame, pady = 1, bd = 4, font=("Arial",15, "bold"), text = "Dashboard", padx = 24, width = 13, height = 1, relief = RAISED)\
                            .place(x=220, y=100)
        self.btnProperty = Button(TopFrame, pady = 1, bd = 4, font=("Arial",15, "bold"), text = "Tenancy", padx = 24, width = 13, height = 1, relief = RAISED)\
                            .place(x=550, y=100)
        self.btnTenants = Button(TopFrame, pady = 1, bd = 4, font=("Arial",15, "bold"), text = "Repair Request", padx = 24, width = 13, height = 1, command=lambda:controller.show_frame(Request), relief = RAISED)\
                            .place(x=880, y=100)
        self.btnLogout = Button(TopFrame, pady = 1, bd=4, font=("Arial",15, "bold"), text = "Log Out", padx = 24, width = 10, height = 1,  command=lambda:controller.show_frame(PropertyLogin), relief = RAISED)\
                            .place(x=0,y=0)

class View3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        blank_space = " "

        MainFrame = Frame(self, bd=25, width = 1590, height = 840, relief = RIDGE, bg = "dodgerblue")
        MainFrame.grid(row=0, column=0)

        TopFrame = Frame(MainFrame, bd = 7, width = 1540, height = 165, relief = RIDGE)
        TopFrame.place(x=0, y=0)

        self.lblTitle = Label(TopFrame, font=("Arial", 40,"bold"), text=" Staff Dashboard", bd=7, anchor = "w", justify=LEFT)
        self.lblTitle.place(x=600, y=0)

        self.btnDashboard = Button(TopFrame, pady = 1, bd = 4, font=("Arial",15, "bold"), text = "Properties", padx = 24, width = 13, height = 1, relief = RAISED)\
                            .place(x=220, y=100)
        self.btnProperty = Button(TopFrame, pady = 1, bd = 4, font=("Arial",15, "bold"), text = "Maintenance work", padx = 24, width = 13, height = 1, command=lambda:controller.show_frame(JobView2), relief = RAISED)\
                            .place(x=550, y=100)
        self.btnTenants = Button(TopFrame, pady = 1, bd = 4, font=("Arial",15, "bold"), text = "Repair Request", padx = 24, width = 13, height = 1, command=lambda:controller.show_frame(JobView2), relief = RAISED)\
                            .place(x=880, y=100)
        self.btnLogout = Button(TopFrame, pady = 1, bd=4, font=("Arial",15, "bold"), text = "Log Out", padx = 24, width = 10, height = 1,  command=lambda:controller.show_frame(PropertyLogin), relief = RAISED)\
                            .place(x=0,y=0)


class PropertyView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        
        self.root = tk.Frame(self,bg="dodgerblue")
        self.root.grid(row=0, column=0)
        
        
        blank_space = " "

        PropertyID = StringVar()
        Address = StringVar()
        Postcode = StringVar()
        Mortgage = StringVar()
        Rent_Cost = StringVar()
        Bedrooms = StringVar()
        Bathrooms = StringVar()
        Property_type = StringVar()
        Available = StringVar()
        LandlordID = StringVar()
    
#-----------------------------------------------------------------------------------------------Functions------------------------------------------------------------------------------------------------------            

        def Exit():
            Exit = tkinter.messagebox.askyesno("Property Management ","Confirm if you want to exit")
            if Exit > 0:
                self.root.destroy()
                
                return

        def searchData(PropertyID="", Address="", Postcode="", Mortgage="", Rent_Cost="", Bedrooms="", Bathrooms="", Property_type="", Available="", LandlordID=""):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM Property WHERE PropertyID=? OR Address=? OR Postcode=? OR Mortgage=? OR Rent_Cost=? OR Bedrooms=? OR Bathrooms=? OR Property_type=? OR Available=? OR LandlordID=?",(PropertyID,Address, Postcode, Mortgage, Rent_Cost, Bedrooms, Bathrooms, Property_type, Available, LandlordID))
                rows = cur.fetchall()
                con.close()
                return rows

        def searchData1():
                for row in self.propertylist.get_children():
                        self.propertylist.delete(row)
                for row in searchData(PropertyID.get(),Address.get(),Postcode.get(),Mortgage.get(), Rent_Cost.get(),Bedrooms.get(),Bathrooms.get(),Property_type.get(),Available.get(),LandlordID.get()):
                        self.propertylist.insert("", 'end', values= row)

        def Reset():
                self.txtPropertyID.delete(0, END)
                self.txtAddress.delete(0, END)
                self.txtPostcode.delete(0, END)
                self.txtMortgage.delete(0, END)
                self.txtRentCost.delete(0, END)
                self.txtBedrooms.delete(0, END)
                self.txtBathrooms.delete(0, END)
                self.txttype.delete(0, END)
                self.txtAvailable.delete(0, END)
                self.txtLandlordID.delete(0, END)
                DisplayData()

        def updateProperty(PropertyID, Address, Postcode, Mortgage, Rent_Cost, Bedrooms, Bathrooms, Property_type, Available, LandlordID):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("UPDATE Property SET  Address=?, Postcode=?, Mortgage=?, Rent_Cost=?, Bedrooms=?, Bathrooms=?, Property_type=?, Available=?, LandlordID=? WHERE PropertyID = ?",(Address, Postcode, Mortgage, Rent_Cost, Bedrooms, Bathrooms, Property_type, Available, LandlordID, PropertyID))
                con.commit()
                con.close()
                

        def addData():
                if PropertyID.get() =="" or Address.get() =="" or Postcode.get() =="" :
                        tkinter.messagebox.showinfo("Property Management App","Please Enter Valid Data")

                else:
                    addRecord(PropertyID.get(),
                              Address.get(),
                              Postcode.get(),
                              Mortgage.get(),
                              Rent_Cost.get(),
                              Bedrooms.get(),
                              Bathrooms.get(),
                              Property_type.get(),
                              Available.get(),
                              LandlordID.get())
                    
                    super(self.propertylist, self).delete()
                    
                    self.propertylist.insert(END,(PropertyID.get(),
                                                  Address.get(),
                                                  Postcode.get(),
                                                  Mortgage.get(),
                                                  Rent_Cost.get(),
                                                  Bedrooms.get(),
                                                  Bathrooms.get(),
                                                  Property_type.get(),
                                                  Available.get(),
                                                  LandlordID.get()))
                    DisplayData()

        def DisplayData():
                result = viewData()
                if len(result)!= 0:
                        self.propertylist.delete(*self.propertylist.get_children())
                        for row in result:
                                self.propertylist.insert('',END,values =row)
                                
        def DeleteData():
                selectedRecord = self.propertylist.focus()
                selectedRecord = self.propertylist.item(selectedRecord)
                deleteRecord(selectedRecord["values"][0])
                DisplayData()
                tkinter.messagebox.showinfo("Property Management App","Record Successfully Deleted")
                DisplayData()
                Reset()

        def get_selected_row(event):
                try:
                        selectedRecord = self.propertylist.focus()
                        selectedRecord=self.propertylist.item(selectedRecord)
                        self.txtPropertyID.delete(0,END)
                        self.txtPropertyID.insert(END,selectedRecord["values"][0])
                        self.txtAddress.delete(0,END)
                        self.txtAddress.insert(END,selectedRecord["values"][1])
                        self.txtPostcode.delete(0,END)
                        self.txtPostcode.insert(END,selectedRecord["values"][2])
                        self.txtMortgage.delete(0,END)
                        self.txtMortgage.insert(END,selectedRecord["values"][3])
                        self.txtRentCost.delete(0,END)
                        self.txtRentCost.insert(END,selectedRecord["values"][4])
                        self.txtBedrooms.delete(0,END)
                        self.txtBedrooms.insert(END,selectedRecord["values"][5])
                        self.txtBathrooms.delete(0,END)
                        self.txtBathrooms.insert(END,selectedRecord["values"][6])
                        self.txttype.delete(0,END)
                        self.txttype.insert(END,selectedRecord["values"][7])
                        self.txtAvailable.delete(0,END)
                        self.txtAvailable.insert(END,selectedRecord["values"][8])
                        self.txtLandlordID.delete(0,END)
                        self.txtLandlordID.insert(END,selectedRecord["values"][9])
                except IndexError:
                        pass
                        
        def addRecord(PropertyID, Address, Postcode, Mortgage, Rent_Cost, Bedrooms, Bathrooms, Property_type, Available, LandlordID):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("INSERT INTO Property VALUES (?,?,?,?,?,?,?,?,?,?)", \
                            (PropertyID,Address, Postcode, Mortgage, Rent_Cost, Bedrooms, Bathrooms, Property_type, Available, LandlordID))
                con.commit()
                con.close()

        def viewData():
               con = sqlite3.connect("Landlord_App.db")
               cur = con.cursor()
               cur.execute("SELECT * FROM Property")
               rows = cur.fetchall()
               con.close()
               return rows

        def deleteRecord(Propertyid):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("DELETE FROM Property WHERE Propertyid=?", (Propertyid,))
                con.commit()
                con.close()

        def updateData():
                selectedRecord = self.propertylist.focus()
                selectedRecord=self.propertylist.item(selectedRecord)
                updateProperty(selectedRecord["values"][0],Address.get(),Postcode.get(),Mortgage.get(), Rent_Cost.get(),Bedrooms.get(),Bathrooms.get(),Property_type.get(),Available.get(),LandlordID.get())
                viewData()
#-------------------------------------------------------------------------------------------Frames----------------------------------------------------------------------------------------------------------
        
        MainFrame = Frame(self.root, bd=25, width =1350, height =700, relief = RIDGE, bg = "dodgerblue")
        MainFrame.grid(row=0, column=0)
    
        TopFrame1 = Frame(MainFrame, bd=5, width =1340, height =50, relief = RIDGE)
        TopFrame1.grid(row = 2, column = 0, pady = 8)
        TitleFrame = Frame(MainFrame, bd=7, width =1340, height =100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)
        TopFrame3 = Frame(MainFrame, bd=5, width = 1340, height = 500, relief = RIDGE)
        TopFrame3.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame3, bd = 5, width = 1340, height = 400, padx = 2, bg="dodgerblue2", relief = RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd = 5, width = 600, height = 180, padx = 2, pady = 4, relief = RIDGE)
        LeftFrame1.pack(side=TOP, padx = 0, pady = 4)

        RightFrame1 = Frame(TopFrame3, bd = 5, width = 320, height = 400, padx = 2, pady = 2, relief =  RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd = 5, width = 310, height = 200, padx = 2, pady = 2)
        RightFrame1a.pack(side=TOP)

        


        self.lblTitle = Label(TitleFrame, font=("Arial", 56,"bold"), text ="Property Hub", bd=7)
        self.lblTitle.grid(row=0, column=0, padx=132)

#----------------------------------------------------------------------------------Entry widgets-----------------------------------------------------------------------------------------------------

        self.lblPropertyID = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Property ID", bd=7, anchor = "w", justify=LEFT)
        self.lblPropertyID.grid(row=0, column=0, sticky = W, padx = 5)
        self.txtPropertyID = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = PropertyID)
        self.txtPropertyID.grid(row=0, column=1)

        self.lblAddress = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Address", bd=7, anchor = "w", justify=LEFT)
        self.lblAddress.grid(row=1, column=0, sticky = W, padx = 5)
        self.txtAddress = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Address)
        self.txtAddress.grid(row=1, column=1)

        self.lblPostcode = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Postcode", bd=7, anchor = "w", justify=LEFT)
        self.lblPostcode.grid(row=2, column=0, sticky = W, padx = 5)
        self.txtPostcode = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Postcode)
        self.txtPostcode.grid(row=2, column=1)

        self.lblMortgage = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Mortgage", bd=7, anchor = "w", justify=LEFT)
        self.lblMortgage.grid(row=3, column=0, sticky = W, padx = 5)
        self.txtMortgage = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Mortgage)
        self.txtMortgage.grid(row=3, column=1)

        self.lblRentCost = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Rent Cost", bd=7, anchor = "w", justify=LEFT)
        self.lblRentCost.grid(row=4, column=0, sticky = W, padx = 5)
        self.txtRentCost = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Rent_Cost)
        self.txtRentCost.grid(row=4, column=1)

        self.lblBedrooms = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Bedrooms", bd=7, anchor = "w", justify=LEFT)
        self.lblBedrooms.grid(row=5, column=0, sticky = W, padx = 5)
        self.txtBedrooms = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Bedrooms)
        self.txtBedrooms.grid(row=5, column=1)

        self.lblBathrooms = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Bathrooms", bd=7, anchor = "w", justify=LEFT)
        self.lblBathrooms.grid(row=6, column=0, sticky = W, padx = 5)
        self.txtBathrooms = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Bathrooms)
        self.txtBathrooms.grid(row=6, column=1)

        self.lbltype = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Property Type", bd=7, anchor = "w", justify=LEFT)
        self.lbltype.grid(row=7, column=0, sticky = W, padx = 5)
        self.txttype = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Property_type)
        self.txttype.grid(row=7, column=1)

        self.lblAvailable = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Available", bd=7, anchor = "w", justify=LEFT)
        self.lblAvailable.grid(row=8, column=0, sticky = W, padx = 5)
        self.txtAvailable = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Available)
        self.txtAvailable.grid(row=8, column=1)

        self.lblLandlordID = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Landlord ID", bd=7, anchor = "w", justify=LEFT)
        self.lblLandlordID.grid(row=9, column=0, sticky = W, padx = 5)
        self.txtLandlordID = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = LandlordID)
        self.txtLandlordID.grid(row=9, column=1)
        
#-----------------------------------------------------------------------------------------Treeview-------------------------------------------------------------------------------------------------

        scroll_x = Scrollbar(RightFrame1a, orient = HORIZONTAL)
        scroll_y = Scrollbar(RightFrame1a, orient = VERTICAL)

        self.propertylist = ttk.Treeview(RightFrame1a, height = 12, columns =("PropertyID","Address","Postcode","Mortgage","Rent_cost","Bedrooms","Bathrooms","Property_type","Available","LandlordID"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        self.propertylist.heading("PropertyID",text="PropertyID")
        self.propertylist.heading("Address",text="Address")
        self.propertylist.heading("Postcode",text="Postcode")
        self.propertylist.heading("Mortgage",text="Mortgage")
        self.propertylist.heading("Rent_cost",text="Rent_cost")
        self.propertylist.heading("Bedrooms",text="Bedrooms")
        self.propertylist.heading("Bathrooms",text="Bathrooms")
        self.propertylist.heading("Property_type",text="Property_type")
        self.propertylist.heading("Available",text="Available")
        self.propertylist.heading("LandlordID",text="LandlordID")

        self.propertylist["show"] = "headings"

        self.propertylist.column("PropertyID", width = 110)
        self.propertylist.column("Address", width = 130)
        self.propertylist.column("Postcode", width = 130)
        self.propertylist.column("Mortgage", width = 100)
        self.propertylist.column("Rent_cost", width = 80)
        self.propertylist.column("Bedrooms", width = 80)
        self.propertylist.column("Bathrooms", width = 80)
        self.propertylist.column("Property_type", width = 130)
        self.propertylist.column("Available", width = 65)
        self.propertylist.column("LandlordID", width = 110)

        self.propertylist.pack(fill = BOTH, expand = 1)
        self.propertylist.bind('<ButtonRelease-1>', get_selected_row)
        DisplayData()

#---------------------------------------------------------------------------------------------Buttons--------------------------------------------------------------------------------------------------------

        self.btnAddNew = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Add new", padx = 24, width = 9, height = 2, relief = RAISED, command = addData).grid(row = 0,column = 0, padx = 1)

        self.btnDisplay = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Display", padx = 24, width = 9, height = 2, relief = RAISED, command = DisplayData).grid(row = 0,column = 1, padx = 1)

        self.btnDelete = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Delete", padx = 24, width = 9, height = 2, relief = RAISED, command = DeleteData).grid(row = 0,column = 2, padx = 1)

        self.btnReset = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Reset", padx = 24, width = 9, height = 2, relief = RAISED, command = Reset).grid(row = 0,column = 3, padx = 1)

        self.btnExit = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Update", padx = 24, width = 9, height = 2, relief = RAISED, command = updateData).grid(row = 0,column = 4, padx = 1)

        self.btnSearch = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Search", padx = 24, width = 9, height = 2, relief = RAISED, command = searchData1).grid(row = 0, column = 5, padx = 1)

        self.btnUpdate = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Exit", padx = 24, width = 9, height = 2, relief = RAISED, command = Exit).grid(row = 0, column = 6, padx = 1)

        self.btnBack = Button(MainFrame, pady = 1,bd = 4, font=("Arial",18, "bold"), text = "Back", padx = 24, width = 9, height = 2, relief = RIDGE, command=lambda:controller.show_frame(MainView)).place(x=0,y=0)
 

        
class Tenant(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.root = tk.Frame(self,bg="dodgerblue")
        self.root.grid(row=0, column=0)
        
        
        blank_space = " "

        TenantID = StringVar()
        First_name = StringVar()
        Surname = StringVar()
        Email = StringVar()
        DOB = StringVar()
        Rent_cost = StringVar()
        City = StringVar()
        Postcode = StringVar()
        Address = StringVar()
        Phone_number = StringVar()
        TenancyID = StringVar()
        User_level = StringVar()
        Password = StringVar()

        User_level.set("")
        Password.set("")
    
#-----------------------------------------------------------------------------------------------Functions------------------------------------------------------------------------------------------------------            

        def Exit():
            Exit = tkinter.messagebox.askyesno("Property Management ","Confirm if you want to exit")
            if Exit > 0:
                self.root.destroy()
                
                return

        def searchData(TenantID="", First_name="", Surname="", Email="", DOB="", Rent_cost="", City="", Postcode="", Address="", Phone_number="", TenancyID=""):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM Tenant WHERE TenantID=? OR First_name=? OR Surname=? OR Email=? OR DOB=? OR Rent_cost=? OR City=? OR Postcode=? OR Address=? OR Phone_number=? OR TenancyID=?",(TenantID, First_name, Surname, Email, DOB, Rent_cost, City, Postcode, Address, Phone_number, TenancyID))
                rows = cur.fetchall()
                con.close()
                return rows

        def searchData1():
                for row in self.tenantlist.get_children():
                        self.tenantlist.delete(row)
                for row in searchData(TenantID.get(), First_name.get(), Surname.get(), Email.get(), DOB.get(), Rent_cost.get(), City.get(), Postcode.get(), Address.get(), Phone_number.get(), TenancyID.get()):
                        self.tenantlist.insert("", 'end', values= row)

        def Reset():
                self.txtTenantID.delete(0, END)
                self.txtFirst_name.delete(0, END)
                self.txtSurname.delete(0, END)
                self.txtEmail.delete(0, END)
                self.txtDOB.delete(0, END)
                self.txtRent_cost.delete(0, END)
                self.txtCity.delete(0, END)
                self.txtPostcode.delete(0, END)
                self.txtAddress.delete(0, END)
                self.txtPhone_number.delete(0, END)
                self.txtTenancyID.delete(0, END)
                DisplayData()

        def updateTenant(TenantID, First_name, Surname, Email, DOB, Rent_cost, City, Postcode, Address, Phone_number, TenancyID):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("UPDATE Tenant SET First_name=?, Surname=?, Email=?, DOB=?, Rent_cost=?, City=?, Postcode=?, Address=?, Phone_number=?, TenancyID=? WHERE TenantID = ?",(First_name, Surname, Email, DOB, Rent_cost, City, Postcode, Address, Phone_number, TenancyID, TenantID))
                con.commit()
                con.close()
                

        def addData():
                if TenantID.get() =="" or Address.get() =="" or Postcode.get() =="" or TenancyID.get() =="" or First_name.get() =="" or Surname.get() =="" or DOB.get() =="" or Phone_number.get() =="" or Email.get() =="" or Rent_cost.get() =="" or City.get() =="" or TenantID.get() =="":
                        tkinter.messagebox.showinfo("Property Management App","Please Enter Valid Data")

                else:
                    addRecord(TenantID.get(), First_name.get(), Surname.get(), Email.get(), DOB.get(), Rent_cost.get(), City.get(), Postcode.get(), Address.get(), Phone_number.get(), TenancyID.get(), User_level.get(), Password.get())
                    
                    super(self.tenantlist, self).delete()
                    
                    self.tenantlist.insert(END,(TenantID.get(), First_name.get(), Surname.get(), Email.get(), DOB.get(), Rent_cost.get(), City.get(), Postcode.get(), Address.get(), Phone_number.get(), TenancyID.get(), User_level.get(), Password.get()))
                    DisplayData()

        def DisplayData():
                result = viewData()
                if len(result)!= 0:
                        self.tenantlist.delete(*self.tenantlist.get_children())
                        for row in result:
                                self.tenantlist.insert('',END,values =row)
                                
        def DeleteData():
                selectedRecord = self.tenantlist.focus()
                selectedRecord = self.tenantlist.item(selectedRecord)
                deleteRecord(selectedRecord["values"][0])
                DisplayData()
                tkinter.messagebox.showinfo("Property Management App","Record Successfully Deleted")
                DisplayData()
                Reset()

        def get_selected_row(event):
                try:
                        selectedRecord = self.tenantlist.focus()
                        selectedRecord=self.tenantlist.item(selectedRecord)
                        self.txtTenantID.delete(0,END)
                        self.txtTenantID.insert(END,selectedRecord["values"][0])
                        self.txtFirst_name.delete(0,END)
                        self.txtFirst_name.insert(END,selectedRecord["values"][1])
                        self.txtSurname.delete(0,END)
                        self.txtSurname.insert(END,selectedRecord["values"][2])
                        self.txtEmail.delete(0,END)
                        self.txtEmail.insert(END,selectedRecord["values"][3])
                        self.txtDOB.delete(0,END)
                        self.txtDOB.insert(END,selectedRecord["values"][4])
                        self.txtRent_cost.delete(0,END)
                        self.txtRent_cost.insert(END,selectedRecord["values"][5])
                        self.txtCity.delete(0,END)
                        self.txtCity.insert(END,selectedRecord["values"][6])
                        self.txtPostcode.delete(0,END)
                        self.txtPostcode.insert(END,selectedRecord["values"][7])
                        self.txtAddress.delete(0,END)
                        self.txtAddress.insert(END,selectedRecord["values"][8])
                        self.txtPhone_number.delete(0,END)
                        self.txtPhone_number.insert(END,selectedRecord["values"][9])
                        self.txtTenancyID.delete(0,END)
                        self.txtTenancyID.insert(END,selectedRecord["values"][10])
                except IndexError:
                        pass
                        
        def addRecord(TenantID, First_name, Surname, Email, DOB, Rent_cost, City, Postcode, Address, Phone_number, TenancyID, User_level, Password):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("INSERT INTO Tenant VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", \
                            (TenantID, First_name, Surname, Email, DOB, Rent_cost, City, Postcode, Address, Phone_number, TenancyID, User_level, Password))
                con.commit()
                con.close()

        def viewData():
               con = sqlite3.connect("Landlord_App.db")
               cur = con.cursor()
               cur.execute("SELECT * FROM Tenant")
               rows = cur.fetchall()
               con.close()
               return rows

        def deleteRecord(Tenantid):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("DELETE FROM Tenant WHERE Tenantid=?", (Tenantid,))
                con.commit()
                con.close()

        def updateData():
                selectedRecord = self.tenantlist.focus()
                selectedRecord=self.tenantlist.item(selectedRecord)
                updateTenant(selectedRecord["values"][0],First_name.get(), Surname.get(), Email.get(), DOB.get(), Rent_cost.get(), City.get(), Postcode.get(), Address.get(), Phone_number.get(), TenancyID.get())
                viewData()
#-------------------------------------------------------------------------------------------Frames----------------------------------------------------------------------------------------------------------
        
        MainFrame = Frame(self.root, bd=25, width =1350, height =700, relief = RIDGE, bg = "dodgerblue")
        MainFrame.grid(row=0, column=0)
    
        TopFrame1 = Frame(MainFrame, bd=5, width =1340, height =50, relief = RIDGE)
        TopFrame1.grid(row = 2, column = 0, pady = 8)
        TitleFrame = Frame(MainFrame, bd=7, width =1340, height =100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)
        TopFrame3 = Frame(MainFrame, bd=5, width = 1340, height = 500, relief = RIDGE)
        TopFrame3.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame3, bd = 5, width = 1340, height = 400, padx = 2, bg="dodgerblue2", relief = RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd = 5, width = 600, height = 180, padx = 2, pady = 4, relief = RIDGE)
        LeftFrame1.pack(side=TOP, padx = 0, pady = 4)

        RightFrame1 = Frame(TopFrame3, bd = 5, width = 320, height = 400, padx = 2, pady = 2, relief =  RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd = 5, width = 310, height = 200, padx = 2, pady = 2)
        RightFrame1a.pack(side=TOP)

        


        self.lblTitle = Label(TitleFrame, font=("Arial", 56,"bold"), text ="Tenant Hub", bd=7)
        self.lblTitle.grid(row=0, column=0, padx=132)

#----------------------------------------------------------------------------------Entry widgets-----------------------------------------------------------------------------------------------------

        self.lblTenantID = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Tenant ID", bd=7, anchor = "w", justify=LEFT)
        self.lblTenantID.grid(row=0, column=0, sticky = W, padx = 5)
        self.txtTenantID = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = TenantID)
        self.txtTenantID.grid(row=0, column=1)

        self.lblFirst_name = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="First Name", bd=7, anchor = "w", justify=LEFT)
        self.lblFirst_name.grid(row=1, column=0, sticky = W, padx = 5)
        self.txtFirst_name = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = First_name)
        self.txtFirst_name.grid(row=1, column=1)

        self.lblSurname = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Surname", bd=7, anchor = "w", justify=LEFT)
        self.lblSurname.grid(row=2, column=0, sticky = W, padx = 5)
        self.txtSurname = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Surname)
        self.txtSurname.grid(row=2, column=1)

        self.lblEmail = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Email Address", bd=7, anchor = "w", justify=LEFT)
        self.lblEmail.grid(row=3, column=0, sticky = W, padx = 5)
        self.txtEmail = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Email)
        self.txtEmail.grid(row=3, column=1)

        self.lblDOB = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="DOB", bd=7, anchor = "w", justify=LEFT)
        self.lblDOB.grid(row=4, column=0, sticky = W, padx = 5)
        self.txtDOB = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = DOB)
        self.txtDOB.grid(row=4, column=1)

        self.lblRent_cost = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Rent Cost", bd=7, anchor = "w", justify=LEFT)
        self.lblRent_cost.grid(row=5, column=0, sticky = W, padx = 5)
        self.txtRent_cost = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Rent_cost)
        self.txtRent_cost.grid(row=5, column=1)

        self.lblCity = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="City", bd=7, anchor = "w", justify=LEFT)
        self.lblCity.grid(row=6, column=0, sticky = W, padx = 5)
        self.txtCity = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = City)
        self.txtCity.grid(row=6, column=1)

        self.lblPostcode = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Postcode", bd=7, anchor = "w", justify=LEFT)
        self.lblPostcode.grid(row=7, column=0, sticky = W, padx = 5)
        self.txtPostcode = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Postcode)
        self.txtPostcode.grid(row=7, column=1)

        self.lblAddress = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Address", bd=7, anchor = "w", justify=LEFT)
        self.lblAddress.grid(row=8, column=0, sticky = W, padx = 5)
        self.txtAddress = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Address)
        self.txtAddress.grid(row=8, column=1)

        self.lblPhone_number = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Phone Number", bd=7, anchor = "w", justify=LEFT)
        self.lblPhone_number.grid(row=9, column=0, sticky = W, padx = 5)
        self.txtPhone_number = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Phone_number)
        self.txtPhone_number.grid(row=9, column=1)

        self.lblTenancyID = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="TenancyID", bd=7, anchor = "w", justify=LEFT)
        self.lblTenancyID.grid(row=10, column=0, sticky = W, padx = 5)
        self.txtTenancyID = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = TenancyID)
        self.txtTenancyID.grid(row=10, column=1)
        
#-----------------------------------------------------------------------------------------Treeview-------------------------------------------------------------------------------------------------

        scroll_x = Scrollbar(RightFrame1a, orient = HORIZONTAL)
        scroll_y = Scrollbar(RightFrame1a, orient = VERTICAL)

        self.tenantlist = ttk.Treeview(RightFrame1a, height = 12, columns =("TenantID","First_Name", "Surname", "Email_Address", "DOB", "Rent_Cost", "City", "Postcode", "Address", "Phone_Number", "TenancyID"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        self.tenantlist.heading("TenantID",text="TenantID")
        self.tenantlist.heading("First_Name",text="First_Name")
        self.tenantlist.heading("Surname",text="Surname")
        self.tenantlist.heading("Email_Address",text="Email_Address")
        self.tenantlist.heading("DOB",text="DOB")
        self.tenantlist.heading("Rent_Cost",text="Rent_Cost")
        self.tenantlist.heading("City",text="City")
        self.tenantlist.heading("Postcode",text="Postcode")
        self.tenantlist.heading("Address",text="Address")
        self.tenantlist.heading("Phone_Number",text="Phone_Number")
        self.tenantlist.heading("TenancyID",text="TenancyID")

        self.tenantlist["show"] = "headings"

        self.tenantlist.column("TenantID", width = 70)
        self.tenantlist.column("First_Name", width = 120)
        self.tenantlist.column("Surname", width = 120)
        self.tenantlist.column("Email_Address", width = 160)
        self.tenantlist.column("DOB", width = 80)
        self.tenantlist.column("Rent_Cost", width = 80)
        self.tenantlist.column("City", width = 100)
        self.tenantlist.column("Postcode", width = 100)
        self.tenantlist.column("Address", width = 130)
        self.tenantlist.column("Phone_Number", width = 110)
        self.tenantlist.column("TenancyID", width = 70)

        self.tenantlist.pack(fill = BOTH, expand = 1)
        self.tenantlist.bind('<ButtonRelease-1>', get_selected_row)
        DisplayData()

#---------------------------------------------------------------------------------------------Buttons--------------------------------------------------------------------------------------------------------

        self.btnAddNew = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Add new", padx = 24, width = 9, height = 2, relief = RAISED, command = addData).grid(row = 0,column = 0, padx = 1)

        self.btnDisplay = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Display", padx = 24, width = 9, height = 2, relief = RAISED, command = DisplayData).grid(row = 0,column = 1, padx = 1)

        self.btnDelete = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Delete", padx = 24, width = 9, height = 2, relief = RAISED, command = DeleteData).grid(row = 0,column = 2, padx = 1)

        self.btnReset = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Reset", padx = 24, width = 9, height = 2, relief = RAISED, command = Reset).grid(row = 0,column = 3, padx = 1)

        self.btnExit = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Update", padx = 24, width = 9, height = 2, relief = RAISED, command = updateData).grid(row = 0,column = 4, padx = 1)

        self.btnSearch = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Search", padx = 24, width = 9, height = 2, relief = RAISED, command = searchData1).grid(row = 0, column = 5, padx = 1)

        self.btnUpdate = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Exit", padx = 24, width = 9, height = 2, relief = RAISED, command = Exit).grid(row = 0, column = 6, padx = 1)    

        self.btnBack = Button(MainFrame, pady = 1,bd = 4, font=("Arial",18, "bold"), text = "Back", padx = 24, width = 9, height = 2, relief = RIDGE, command=lambda:controller.show_frame(MainView)).place(x=0,y=0)


class StaffView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        
        self.root = tk.Frame(self,bg="dodgerblue")
        self.root.grid(row=0, column=0)
        
        
        blank_space = " "

        StaffID = StringVar()
        First_name = StringVar()
        Surname = StringVar()
        Phone_number = StringVar()
        City = StringVar()
        Postcode = StringVar()
        Address = StringVar()
        Expertise = StringVar()
        User_level = StringVar()
        Password = StringVar()

        User_level.set("")
        Password.set("")
    
#-----------------------------------------------------------------------------------------------Functions------------------------------------------------------------------------------------------------------            

        def Exit():
            Exit = tkinter.messagebox.askyesno("Property Management ","Confirm if you want to exit")
            if Exit > 0:
                self.root.destroy()
                
                return

        def searchData(StaffID="", First_name="", Surname="", Phone_number="", City="", Postcode="", Address="", Expertise=""):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM Staff where StaffID=? OR First_name=? OR Surname=? OR Phone_number=? OR City=? OR Postcode=? OR Address=? OR Expertise=?",(StaffID, First_name, Surname, Phone_number, City, Postcode, Address, Expertise))
                rows = cur.fetchall()
                con.close()
                return rows

        def searchData1():
                for row in self.stafflist.get_children():
                        self.stafflist.delete(row)
                for row in searchData(StaffID.get(), First_name.get(), Surname.get(), Phone_number.get(), City.get(), Postcode.get(), Address.get(), Expertise.get()):
                        self.stafflist.insert("", 'end', values= row)

        def Reset():
                self.txtStaffID.delete(0, END)
                self.txtFirst_name.delete(0, END)
                self.txtSurname.delete(0, END)
                self.txtPhone_number.delete(0, END)
                self.txtCity.delete(0, END)
                self.txtPostcode.delete(0, END)
                self.txtAddress.delete(0, END)
                self.txtExpertise.delete(0, END)
                DisplayData()

        def updateStaff(StaffID, First_name, Surname, Phone_number, City, Postcode, Address, Expertise):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("UPDATE Staff SET First_name=?, Surname=?, Phone_number=?, City=?, Postcode=?, Address=?, Expertise=? WHERE StaffID = ?",( First_name, Surname, Phone_number, City, Postcode, Address, Expertise, StaffID))
                con.commit()
                con.close()
                

        def addData():
                if StaffID.get() =="" or First_name.get() =="" or Surname.get() =="" or Phone_number.get() =="" or City.get() =="" or Postcode.get() ==""or Address.get() =="" or Expertise.get() =="" :
                        tkinter.messagebox.showinfo("Property Management App","Please Enter Valid Data")

                else:
                    addRecord(StaffID.get(),
                              First_name.get(),
                              Surname.get(),
                              Phone_number.get(),
                              City.get(),
                              Postcode.get(),
                              Address.get(),
                              Expertise.get(),
                              User_level.get(),
                              Password.get())
                    
                    super(self.stafflist, self).delete()
                    
                    self.stafflist.insert(END,(StaffID.get(),
                                                  First_name.get(),
                                                  Surname.get(),
                                                  Phone_number.get(),
                                                  City.get(),
                                                  Postcode.get(),
                                                  Address.get(),
                                                  Expertise.get(),
                                                  User_level.get(),
                                                  Password.get()))
                    DisplayData()

        def DisplayData():
                result = viewData()
                if len(result)!= 0:
                        self.stafflist.delete(*self.stafflist.get_children())
                        for row in result:
                                self.stafflist.insert('',END,values =row)
                                
        def DeleteData():
                selectedRecord = self.stafflist.focus()
                selectedRecord = self.stafflist.item(selectedRecord)
                deleteRecord(selectedRecord["values"][0])
                DisplayData()
                tkinter.messagebox.showinfo("Property Management App","Record Successfully Deleted")
                DisplayData()
                Reset()

        def get_selected_row(event):
                try:
                        selectedRecord = self.stafflist.focus()
                        selectedRecord=self.stafflist.item(selectedRecord)
                        self.txtStaffID.delete(0,END)
                        self.txtStaffID.insert(END,selectedRecord["values"][0])
                        self.txtFirst_name.delete(0,END)
                        self.txtFirst_name.insert(END,selectedRecord["values"][1])
                        self.txtSurname.delete(0,END)
                        self.txtSurname.insert(END,selectedRecord["values"][2])
                        self.txtPhone_number.delete(0,END)
                        self.txtPhone_number.insert(END,selectedRecord["values"][3])
                        self.txtCity.delete(0,END)
                        self.txtCity.insert(END,selectedRecord["values"][4])
                        self.txtPostcode.delete(0,END)
                        self.txtPostcode.insert(END,selectedRecord["values"][5])
                        self.txtAddress.delete(0,END)
                        self.txtAddress.insert(END,selectedRecord["values"][6])
                        self.txtExpertise.delete(0,END)
                        self.txtExpertise.insert(END,selectedRecord["values"][7])
                except IndexError:
                        pass
                        
        def addRecord(StaffID, First_name, Surname, Phone_number, City, Postcode, Address, Expertise, User_level, Password):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("INSERT INTO Staff VALUES (?,?,?,?,?,?,?,?,?,?)", \
                            (StaffID, First_name, Surname, Phone_number, City, Postcode, Address, Expertise, User_level, Password))
                con.commit()
                con.close()

        def viewData():
               con = sqlite3.connect("Landlord_App.db")
               cur = con.cursor()
               cur.execute("SELECT * FROM Staff")
               rows = cur.fetchall()
               con.close()
               return rows

        def deleteRecord(Staffid):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("DELETE FROM Staff WHERE Staffid=?", (Staffid,))
                con.commit()
                con.close()

        def updateData():
                selectedRecord = self.stafflist.focus()
                selectedRecord=self.stafflist.item(selectedRecord)
                updateStaff(selectedRecord["values"][0],StaffID.get(), First_name.get(), Surname.get(), Phone_number.get(), City.get(), Postcode.get(), Address.get(), Expertise.get())
                viewData()
#-------------------------------------------------------------------------------------------Frames----------------------------------------------------------------------------------------------------------
        
        MainFrame = Frame(self.root, bd=25, width =1350, height =700, relief = RIDGE, bg = "dodgerblue")
        MainFrame.grid(row=0, column=0)
    
        TopFrame1 = Frame(MainFrame, bd=5, width =1340, height =50, relief = RIDGE)
        TopFrame1.grid(row = 2, column = 0, pady = 8)
        TitleFrame = Frame(MainFrame, bd=7, width =1340, height =100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)
        TopFrame3 = Frame(MainFrame, bd=5, width = 1340, height = 500, relief = RIDGE)
        TopFrame3.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame3, bd = 5, width = 1340, height = 400, padx = 2, bg="dodgerblue2", relief = RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd = 5, width = 600, height = 180, padx = 2, pady = 4, relief = RIDGE)
        LeftFrame1.pack(side=TOP, padx = 0, pady = 4)

        RightFrame1 = Frame(TopFrame3, bd = 5, width = 320, height = 400, padx = 2, pady = 2, relief =  RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd = 5, width = 310, height = 200, padx = 2, pady = 2)
        RightFrame1a.pack(side=TOP)

        


        self.lblTitle = Label(TitleFrame, font=("Arial", 56,"bold"), text ="Staff Hub", bd=7)
        self.lblTitle.grid(row=0, column=0, padx=132)

#----------------------------------------------------------------------------------Entry widgets-----------------------------------------------------------------------------------------------------

        self.lblStaffID = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Staff ID", bd=7, anchor = "w", justify=LEFT)
        self.lblStaffID.grid(row=0, column=0, sticky = W, padx = 5)
        self.txtStaffID = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = StaffID)
        self.txtStaffID.grid(row=0, column=1)

        self.lblFirst_name = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="First Name", bd=7, anchor = "w", justify=LEFT)
        self.lblFirst_name.grid(row=1, column=0, sticky = W, padx = 5)
        self.txtFirst_name = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = First_name)
        self.txtFirst_name.grid(row=1, column=1)

        self.lblSurname = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Surname", bd=7, anchor = "w", justify=LEFT)
        self.lblSurname.grid(row=2, column=0, sticky = W, padx = 5)
        self.txtSurname = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Surname)
        self.txtSurname.grid(row=2, column=1)

        self.lblPhone_number = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Phone Number", bd=7, anchor = "w", justify=LEFT)
        self.lblPhone_number.grid(row=3, column=0, sticky = W, padx = 5)
        self.txtPhone_number = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Phone_number)
        self.txtPhone_number.grid(row=3, column=1)

        self.lblCity = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="City", bd=7, anchor = "w", justify=LEFT)
        self.lblCity.grid(row=4, column=0, sticky = W, padx = 5)
        self.txtCity = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = City)
        self.txtCity.grid(row=4, column=1)

        self.lblPostcode = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Postcode", bd=7, anchor = "w", justify=LEFT)
        self.lblPostcode.grid(row=5, column=0, sticky = W, padx = 5)
        self.txtPostcode = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Postcode)
        self.txtPostcode.grid(row=5, column=1)

        self.lblAddress = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Address", bd=7, anchor = "w", justify=LEFT)
        self.lblAddress.grid(row=6, column=0, sticky = W, padx = 5)
        self.txtAddress = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Address)
        self.txtAddress.grid(row=6, column=1)

        self.lblExpertise = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Expertise", bd=7, anchor = "w", justify=LEFT)
        self.lblExpertise.grid(row=7, column=0, sticky = W, padx = 5)
        self.txtExpertise = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Expertise)
        self.txtExpertise.grid(row=7, column=1)
        
#-----------------------------------------------------------------------------------------Treeview-------------------------------------------------------------------------------------------------

        scroll_x = Scrollbar(RightFrame1a, orient = HORIZONTAL)
        scroll_y = Scrollbar(RightFrame1a, orient = VERTICAL)

        self.stafflist = ttk.Treeview(RightFrame1a, height = 12, columns =("StaffID","First_name","Surname","Phone_number","City","Postcode","Address","Expertise"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        self.stafflist.heading("StaffID",text="StaffID")
        self.stafflist.heading("First_name",text="First_name")
        self.stafflist.heading("Surname",text="Surname")
        self.stafflist.heading("Phone_number",text="Phone_number")
        self.stafflist.heading("City",text="City")
        self.stafflist.heading("Postcode",text="Postcode")
        self.stafflist.heading("Address",text="Address")
        self.stafflist.heading("Expertise",text="Expertise")

        self.stafflist["show"] = "headings"

        self.stafflist.column("StaffID", width = 60)
        self.stafflist.column("First_name", width = 100)
        self.stafflist.column("Surname", width = 100)
        self.stafflist.column("Phone_number", width = 100)
        self.stafflist.column("City", width = 100)
        self.stafflist.column("Postcode", width = 80)
        self.stafflist.column("Address", width = 160)
        self.stafflist.column("Expertise", width = 150)
        
        self.stafflist.pack(fill = BOTH, expand = 1)
        self.stafflist.bind('<ButtonRelease-1>', get_selected_row)
        DisplayData()

#---------------------------------------------------------------------------------------------Buttons--------------------------------------------------------------------------------------------------------

        self.btnAddNew = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Add new", padx = 24, width = 9, height = 2, relief = RAISED, command = addData).grid(row = 0,column = 0, padx = 1)

        self.btnDisplay = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Display", padx = 24, width = 9, height = 2, relief = RAISED, command = DisplayData).grid(row = 0,column = 1, padx = 1)

        self.btnDelete = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Delete", padx = 24, width = 9, height = 2, relief = RAISED, command = DeleteData).grid(row = 0,column = 2, padx = 1)

        self.btnReset = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Reset", padx = 24, width = 9, height = 2, relief = RAISED, command = Reset).grid(row = 0,column = 3, padx = 1)

        self.btnExit = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Update", padx = 24, width = 9, height = 2, relief = RAISED, command = updateData).grid(row = 0,column = 4, padx = 1)

        self.btnSearch = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Search", padx = 24, width = 9, height = 2, relief = RAISED, command = searchData1).grid(row = 0, column = 5, padx = 1)

        self.btnUpdate = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Exit", padx = 24, width = 9, height = 2, relief = RAISED, command = Exit).grid(row = 0, column = 6, padx = 1)

        self.btnBack = Button(MainFrame, pady = 1,bd = 4, font=("Arial",18, "bold"), text = "Back", padx = 24, width = 9, height = 2, relief = RIDGE, command=lambda:controller.show_frame(MainView)).place(x=0,y=0)


class FinanceView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        
        self.root = tk.Frame(self,bg="dodgerblue")
        self.root.grid(row=0, column=0)
        
        
        blank_space = " "

        FinanceID = StringVar()
        Income = StringVar()
        Transaction_type = StringVar()
        Expenses = StringVar()
        Payments_due = StringVar()
        TenancyID = StringVar()
    
#-----------------------------------------------------------------------------------------------Functions------------------------------------------------------------------------------------------------------            

        def Exit():
            Exit = tkinter.messagebox.askyesno("Property Management ","Confirm if you want to exit")
            if Exit > 0:
                self.root.destroy()
                
                return

        def searchData(FinanceID="", Income="", Transaction_type="", Expenses="", Payments_due="", TenancyID=""):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM Finance WHERE FinanceID=? OR Income=? OR Transaction_type=? OR Expenses=? OR Payments_due=? OR TenancyID=?",(FinanceID, Income, Transaction_type, Expenses, Payments_due, TenancyID))
                rows = cur.fetchall()
                con.close()
                return rows

        def searchData1():
                for row in self.financelist.get_children():
                        self.financelist.delete(row)
                for row in searchData(FinanceID.get(),Income.get(),Transaction_type.get(),Expenses.get(), Payments_due.get(),TenancyID.get()):
                        self.financelist.insert("", 'end', values= row)

        def Reset():
                self.txtFinanceID.delete(0, END)
                self.txtIncome.delete(0, END)
                self.txtTransaction_type.delete(0, END)
                self.txtExpenses.delete(0, END)
                self.txtPayments_due.delete(0, END)
                self.txtTenancyID.delete(0, END)
                DisplayData()

        def updateFinance(FinanceID, Income, Transaction_type, Expenses, Payments_due, TenancyID):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("UPDATE Finance SET Income=?, Transaction_type=?, Expenses=?, Payments_due=?, TenancyID=? WHERE FinanceID=?",(Income, Transaction_type, Expenses, Payments_due, TenancyID, FinanceID))
                con.commit()
                con.close()
                

        def addData():
                if FinanceID.get() =="" or Income.get() =="" or Transaction_type.get() =="" or Expenses.get() =="" or Payments_due.get() =="" or TenancyID.get()=="" :
                        tkinter.messagebox.showinfo("Property Management App","Please Enter Valid Data")

                else:
                    addRecord(FinanceID.get(),
                              Income.get(),
                              Transaction_type.get(),
                              Expenses.get(),
                              Payments_due.get(),
                              TenancyID.get())
                    
                    super(self.financelist, self).delete()
                    
                    self.financelist.insert(END,(FinanceID.get(),
                                                 Income.get(),
                                                 Transaction_type.get(),
                                                 Expenses.get(),
                                                Payments_due.get(),
                                                 TenancyID.get()))
                    DisplayData()

        def DisplayData():
                result = viewData()
                if len(result)!= 0:
                        self.financelist.delete(*self.financelist.get_children())
                        for row in result:
                                self.financelist.insert('',END,values =row)
                                
        def DeleteData():
                selectedRecord = self.financelist.focus()
                selectedRecord = self.financelist.item(selectedRecord)
                deleteRecord(selectedRecord["values"][0])
                DisplayData()
                tkinter.messagebox.showinfo("Property Management App","Record Successfully Deleted")
                DisplayData()
                Reset()

        def get_selected_row(event):
                try:
                        selectedRecord = self.financelist.focus()
                        selectedRecord=self.financelist.item(selectedRecord)
                        self.txtFinanceID.delete(0,END)
                        self.txtFinanceID.insert(END,selectedRecord["values"][0])
                        self.txtIncome.delete(0,END)
                        self.txtIncome.insert(END,selectedRecord["values"][1])
                        self.txtTransaction_type.delete(0,END)
                        self.txtTransaction_type.insert(END,selectedRecord["values"][2])
                        self.txtExpenses.delete(0,END)
                        self.txtExpenses.insert(END,selectedRecord["values"][3])
                        self.txtPayments_due.delete(0,END)
                        self.txtPayments_due.insert(END,selectedRecord["values"][4])
                        self.txtTenancyID.delete(0,END)
                        self.txtTenancyID.insert(END,selectedRecord["values"][5])
                except IndexError:
                        pass
                        
        def addRecord(FinanceID, Income, Transaction_type, Expenses, Payments_due, TenancyID):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("INSERT INTO Finance VALUES (?,?,?,?,?,?)", \
                            (FinanceID, Income, Transaction_type, Expenses, Payments_due, TenancyID))
                con.commit()
                con.close()

        def viewData():
               con = sqlite3.connect("Landlord_App.db")
               cur = con.cursor()
               cur.execute("SELECT * FROM Finance")
               rows = cur.fetchall()
               con.close()
               return rows

        def deleteRecord(Financeid):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("DELETE FROM Finance WHERE Financeid=?", (Financeid,))
                con.commit()
                con.close()

        def updateData():
                selectedRecord = self.financelist.focus()
                selectedRecord=self.financelist.item(selectedRecord)
                updateFinance(selectedRecord["values"][0], Income.get(),Transaction_type.get(),Expenses.get(), Payments_due.get(),TenancyID.get())
                viewData()
#-------------------------------------------------------------------------------------------Frames----------------------------------------------------------------------------------------------------------
        
        MainFrame = Frame(self.root, bd=25, width =1350, height =700, relief = RIDGE, bg = "dodgerblue")
        MainFrame.grid(row=0, column=0)
    
        TopFrame1 = Frame(MainFrame, bd=5, width =1340, height =50, relief = RIDGE)
        TopFrame1.grid(row = 2, column = 0, pady = 8)
        TitleFrame = Frame(MainFrame, bd=7, width =1340, height =100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)
        TopFrame3 = Frame(MainFrame, bd=5, width = 1340, height = 500, relief = RIDGE)
        TopFrame3.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame3, bd = 5, width = 1340, height = 400, padx = 2, bg="dodgerblue2", relief = RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd = 5, width = 600, height = 180, padx = 2, pady = 4, relief = RIDGE)
        LeftFrame1.pack(side=TOP, padx = 0, pady = 4)

        RightFrame1 = Frame(TopFrame3, bd = 5, width = 320, height = 400, padx = 2, pady = 2, relief =  RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd = 5, width = 310, height = 200, padx = 2, pady = 2)
        RightFrame1a.pack(side=TOP)

        


        self.lblTitle = Label(TitleFrame, font=("Arial", 56,"bold"), text ="Finance Hub", bd=7)
        self.lblTitle.grid(row=0, column=0, padx=132)

#----------------------------------------------------------------------------------Entry widgets-----------------------------------------------------------------------------------------------------

        self.lblFinanceID = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Finance ID", bd=7, anchor = "w", justify=LEFT)
        self.lblFinanceID.grid(row=0, column=0, sticky = W, padx = 5)
        self.txtFinanceID = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = FinanceID)
        self.txtFinanceID.grid(row=0, column=1)

        self.lblIncome = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Income", bd=7, anchor = "w", justify=LEFT)
        self.lblIncome.grid(row=1, column=0, sticky = W, padx = 5)
        self.txtIncome = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Income)
        self.txtIncome.grid(row=1, column=1)

        self.lblTransaction_type = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Transaction Type", bd=7, anchor = "w", justify=LEFT)
        self.lblTransaction_type.grid(row=2, column=0, sticky = W, padx = 5)
        self.txtTransaction_type = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Transaction_type)
        self.txtTransaction_type.grid(row=2, column=1)

        self.lblExpenses = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Expenses", bd=7, anchor = "w", justify=LEFT)
        self.lblExpenses.grid(row=3, column=0, sticky = W, padx = 5)
        self.txtExpenses = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Expenses)
        self.txtExpenses.grid(row=3, column=1)

        self.lblPayments_due = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Payments_due", bd=7, anchor = "w", justify=LEFT)
        self.lblPayments_due.grid(row=4, column=0, sticky = W, padx = 5)
        self.txtPayments_due = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Payments_due)
        self.txtPayments_due.grid(row=4, column=1)

        self.lblTenancyID = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="TenancyID", bd=7, anchor = "w", justify=LEFT)
        self.lblTenancyID.grid(row=5, column=0, sticky = W, padx = 5)
        self.txtTenancyID = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = TenancyID)
        self.txtTenancyID.grid(row=5, column=1)

        
#-----------------------------------------------------------------------------------------Treeview-------------------------------------------------------------------------------------------------

        scroll_x = Scrollbar(RightFrame1a, orient = HORIZONTAL)
        scroll_y = Scrollbar(RightFrame1a, orient = VERTICAL)

        self.financelist = ttk.Treeview(RightFrame1a, height = 12, columns =("FinanceID","Income","Transaction_type","Expenses","Payments_due","TenancyID"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        self.financelist.heading("FinanceID",text="FinanceID")
        self.financelist.heading("Income",text="Income")
        self.financelist.heading("Transaction_type",text="Transaction_type")
        self.financelist.heading("Expenses",text="Expenses")
        self.financelist.heading("Payments_due",text="Payments_due")
        self.financelist.heading("TenancyID",text="TenancyID")

        self.financelist["show"] = "headings"

        self.financelist.column("FinanceID", width = 110)
        self.financelist.column("Income", width = 130)
        self.financelist.column("Transaction_type", width = 130)
        self.financelist.column("Expenses", width = 100)
        self.financelist.column("Payments_due", width = 80)
        self.financelist.column("TenancyID", width = 80)

        self.financelist.pack(fill = BOTH, expand = 1)
        self.financelist.bind('<ButtonRelease-1>', get_selected_row)
        DisplayData()

#---------------------------------------------------------------------------------------------Buttons--------------------------------------------------------------------------------------------------------

        self.btnAddNew = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Add new", padx = 24, width = 9, height = 2, relief = RAISED, command = addData).grid(row = 0,column = 0, padx = 1)

        self.btnDisplay = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Display", padx = 24, width = 9, height = 2, relief = RAISED, command = DisplayData).grid(row = 0,column = 1, padx = 1)

        self.btnDelete = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Delete", padx = 24, width = 9, height = 2, relief = RAISED, command = DeleteData).grid(row = 0,column = 2, padx = 1)

        self.btnReset = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Reset", padx = 24, width = 9, height = 2, relief = RAISED, command = Reset).grid(row = 0,column = 3, padx = 1)

        self.btnExit = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Update", padx = 24, width = 9, height = 2, relief = RAISED, command = updateData).grid(row = 0,column = 4, padx = 1)

        self.btnSearch = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Search", padx = 24, width = 9, height = 2, relief = RAISED, command = searchData1).grid(row = 0, column = 5, padx = 1)

        self.btnUpdate = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Exit", padx = 24, width = 9, height = 2, relief = RAISED, command = Exit).grid(row = 0, column = 6, padx = 1)

        self.btnBack = Button(MainFrame, pady = 1,bd = 4, font=("Arial",18, "bold"), text = "Back", padx = 24, width = 9, height = 2, relief = RIDGE, command=lambda:controller.show_frame(MainView)).place(x=0,y=0)
 

class JobView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        
        self.root = tk.Frame(self,bg="dodgerblue")
        self.root.grid(row=0, column=0)
        
        
        blank_space = " "

        JobID = StringVar()
        Description = StringVar()
        Date = StringVar()
        Completed = StringVar()
        Cost = StringVar()
        StaffID = StringVar()
        PropertyID = StringVar()
    
#-----------------------------------------------------------------------------------------------Functions------------------------------------------------------------------------------------------------------            

        def Exit():
            Exit = tkinter.messagebox.askyesno("Property Management ","Confirm if you want to exit")
            if Exit > 0:
                self.root.destroy()
                
                return

        def searchData(JobID="", Description="", Date="", Completed="", Cost="", StaffID="", PropertyID=""):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM Job WHERE JobID=? OR Description=? OR Date=? OR Completed=? OR Cost=? OR StaffID=? OR PropertyID=?",(JobID, Description, Date, Completed, Cost, StaffID, PropertyID))
                rows = cur.fetchall()
                con.close()
                return rows

        def searchData1():
                for row in self.joblist.get_children():
                        self.joblist.delete(row)
                for row in searchData(JobID.get(), Description.get(), Date.get(), Completed.get(), Cost.get(), StaffID.get(), PropertyID.get()):
                        self.joblist.insert("", 'end', values= row)

        def Reset():
                self.txtJobID.delete(0, END)
                self.txtDescription.delete(0, END)
                self.txtDate.delete(0, END)
                self.txtCompleted.delete(0, END)
                self.txtCost.delete(0, END)
                self.txtStaffID.delete(0, END)
                self.txtPropertyID.delete(0, END)
                DisplayData()

        def updateJob(JobID, Description, Date, Completed, Cost, StaffID, PropertyID):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("UPDATE Job SET Description=?, Date=?, Completed=?, Cost=?, StaffID=?, PropertyID=? WHERE JobID = ?",(Description, Date, Completed, Cost, StaffID, PropertyID, JobID))
                con.commit()
                con.close()
                

        def addData():
                if JobID.get() =="" or Description.get() =="" or Date.get() =="" or Completed.get() =="" or Cost.get() =="" or StaffID.get() =="" or PropertyID.get() =="":
                        tkinter.messagebox.showinfo("Property Management App","Please Enter Valid Data")

                else:
                    addRecord(JobID.get(), Description.get(), Date.get(), Completed.get(), Cost.get(), StaffID.get(), PropertyID.get())
                    
                    super(self.joblist, self).delete()
                    
                    self.joblist.insert(END,(JobID.get(), Description.get(), Date.get(), Completed.get(), Cost.get(), StaffID.get(), PropertyID.get()))
                    DisplayData()

        def DisplayData():
                result = viewData()
                if len(result)!= 0:
                        self.joblist.delete(*self.joblist.get_children())
                        for row in result:
                                self.joblist.insert('',END,values =row)
                                
        def DeleteData():
                selectedRecord = self.joblist.focus()
                selectedRecord = self.joblist.item(selectedRecord)
                deleteRecord(selectedRecord["values"][0])
                DisplayData()
                tkinter.messagebox.showinfo("Property Management App","Record Successfully Deleted")
                DisplayData()
                Reset()

        def get_selected_row(event):
                try:
                        selectedRecord = self.joblist.focus()
                        selectedRecord=self.joblist.item(selectedRecord)
                        self.txtJobID.delete(0,END)
                        self.txtJobID.insert(END,selectedRecord["values"][0])
                        self.txtDescription.delete(0,END)
                        self.txtDescription.insert(END,selectedRecord["values"][1])
                        self.txtDate.delete(0,END)
                        self.txtDate.insert(END,selectedRecord["values"][2])
                        self.txtCompleted.delete(0,END)
                        self.txtCompleted.insert(END,selectedRecord["values"][3])
                        self.txtCost.delete(0,END)
                        self.txtCost.insert(END,selectedRecord["values"][4])
                        self.txtStaffID.delete(0,END)
                        self.txtStaffID.insert(END,selectedRecord["values"][5])
                        self.txtPropertyID.delete(0,END)
                        self.txtPropertyID.insert(END,selectedRecord["values"][6])
                except IndexError:
                        pass
                        
        def addRecord(JobID, Description, Date, Completed, Cost, StaffID, PropertyID):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("INSERT INTO Job VALUES (?,?,?,?,?,?,?)", \
                            (JobID, Description, Date, Completed, Cost, StaffID, PropertyID))
                con.commit()
                con.close()

        def viewData():
               con = sqlite3.connect("Landlord_App.db")
               cur = con.cursor()
               cur.execute("SELECT * FROM Job")
               rows = cur.fetchall()
               con.close()
               return rows

        def deleteRecord(Jobid):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("DELETE FROM Job WHERE Jobid=?", (Jobid,))
                con.commit()
                con.close()

        def updateData():
                selectedRecord = self.joblist.focus()
                selectedRecord=self.joblist.item(selectedRecord)
                updateJob(selectedRecord["values"][0], Description.get(), Date.get(), Completed.get(), Cost.get(), StaffID.get(), PropertyID.get())
                viewData()
#-------------------------------------------------------------------------------------------Frames----------------------------------------------------------------------------------------------------------
        
        MainFrame = Frame(self.root, bd=25, width =1350, height =700, relief = RIDGE, bg = "dodgerblue")
        MainFrame.grid(row=0, column=0)
    
        TopFrame1 = Frame(MainFrame, bd=5, width =1340, height =50, relief = RIDGE)
        TopFrame1.grid(row = 2, column = 0, pady = 8)
        TitleFrame = Frame(MainFrame, bd=7, width =1340, height =100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)
        TopFrame3 = Frame(MainFrame, bd=5, width = 1340, height = 500, relief = RIDGE)
        TopFrame3.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame3, bd = 5, width = 1340, height = 400, padx = 2, bg="dodgerblue2", relief = RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd = 5, width = 600, height = 180, padx = 2, pady = 4, relief = RIDGE)
        LeftFrame1.pack(side=TOP, padx = 0, pady = 4)

        RightFrame1 = Frame(TopFrame3, bd = 5, width = 320, height = 400, padx = 2, pady = 2, relief =  RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd = 5, width = 310, height = 200, padx = 2, pady = 2)
        RightFrame1a.pack(side=TOP)

        


        self.lblTitle = Label(TitleFrame, font=("Arial", 56,"bold"), text ="Maintenance Hub", bd=7)
        self.lblTitle.grid(row=0, column=0, padx=132)

#----------------------------------------------------------------------------------Entry widgets-----------------------------------------------------------------------------------------------------

        self.lblJobID = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Job ID", bd=7, anchor = "w", justify=LEFT)
        self.lblJobID.grid(row=0, column=0, sticky = W, padx = 5)
        self.txtJobID = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable =   JobID)
        self.txtJobID.grid(row=0, column=1)

        self.lblDescription = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Description", bd=7, anchor = "w", justify=LEFT)
        self.lblDescription.grid(row=1, column=0, sticky = W, padx = 5)
        self.txtDescription = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Description)
        self.txtDescription.grid(row=1, column=1)

        self.lblDate = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Date", bd=7, anchor = "w", justify=LEFT)
        self.lblDate.grid(row=2, column=0, sticky = W, padx = 5)
        self.txtDate = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Date)
        self.txtDate.grid(row=2, column=1)

        self.lblCompleted = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Completed", bd=7, anchor = "w", justify=LEFT)
        self.lblCompleted.grid(row=3, column=0, sticky = W, padx = 5)
        self.txtCompleted = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Completed)
        self.txtCompleted.grid(row=3, column=1)

        self.lblCost = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Cost", bd=7, anchor = "w", justify=LEFT)
        self.lblCost.grid(row=4, column=0, sticky = W, padx = 5)
        self.txtCost = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Cost)
        self.txtCost.grid(row=4, column=1)

        self.lblStaffID = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Staff ID", bd=7, anchor = "w", justify=LEFT)
        self.lblStaffID.grid(row=5, column=0, sticky = W, padx = 5)
        self.txtStaffID = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = StaffID)
        self.txtStaffID.grid(row=5, column=1)

        self.lblPropertyID = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Property ID", bd=7, anchor = "w", justify=LEFT)
        self.lblPropertyID.grid(row=6, column=0, sticky = W, padx = 5)
        self.txtPropertyID = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = PropertyID)
        self.txtPropertyID.grid(row=6, column=1)

        
#-----------------------------------------------------------------------------------------Treeview-------------------------------------------------------------------------------------------------

        scroll_x = Scrollbar(RightFrame1a, orient = HORIZONTAL)
        scroll_y = Scrollbar(RightFrame1a, orient = VERTICAL)

        self.joblist = ttk.Treeview(RightFrame1a, height = 12, columns =("JobID", "Description", "Date", "Completed", "Cost", "StaffID", "PropertyID"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        self.joblist.heading("JobID",text="JobID")
        self.joblist.heading("Description",text="Description")
        self.joblist.heading("Date",text="Date")
        self.joblist.heading("Completed",text="Completed")
        self.joblist.heading("Cost",text="Cost")
        self.joblist.heading("StaffID",text="StaffID")
        self.joblist.heading("PropertyID",text="PropertyID")

        self.joblist["show"] = "headings"

        self.joblist.column("JobID", width = 110)
        self.joblist.column("Description", width = 150)
        self.joblist.column("Date", width = 130)
        self.joblist.column("Completed", width = 100)
        self.joblist.column("Cost", width = 80)
        self.joblist.column("StaffID", width = 80)
        self.joblist.column("PropertyID", width = 80)

        self.joblist.pack(fill = BOTH, expand = 1)
        self.joblist.bind('<ButtonRelease-1>', get_selected_row)
        DisplayData()

#---------------------------------------------------------------------------------------------Buttons--------------------------------------------------------------------------------------------------------

        self.btnAddNew = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Add new", padx = 24, width = 9, height = 2, relief = RAISED, command = addData).grid(row = 0,column = 0, padx = 1)

        self.btnDisplay = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Display", padx = 24, width = 9, height = 2, relief = RAISED, command = DisplayData).grid(row = 0,column = 1, padx = 1)

        self.btnDelete = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Delete", padx = 24, width = 9, height = 2, relief = RAISED, command = DeleteData).grid(row = 0,column = 2, padx = 1)

        self.btnReset = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Reset", padx = 24, width = 9, height = 2, relief = RAISED, command = Reset).grid(row = 0,column = 3, padx = 1)

        self.btnExit = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Update", padx = 24, width = 9, height = 2, relief = RAISED, command = updateData).grid(row = 0,column = 4, padx = 1)

        self.btnSearch = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Search", padx = 24, width = 9, height = 2, relief = RAISED, command = searchData1).grid(row = 0, column = 5, padx = 1)

        self.btnUpdate = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Exit", padx = 24, width = 9, height = 2, relief = RAISED, command = Exit).grid(row = 0, column = 6, padx = 1)

        self.btnBack = Button(MainFrame, pady = 1,bd = 4, font=("Arial",18, "bold"), text = "Back", padx = 24, width = 9, height = 2, relief = RIDGE, command=lambda:controller.show_frame(MainView)).place(x=0,y=0)

class Request(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.MainFrame = Frame(self, bd=25, width = 1600, height = 820, relief = RIDGE, bg = "dodgerblue")
        self.MainFrame.grid(row=0, column=0)

        self.Description = StringVar()
        self.Date = StringVar()
        self.ID = StringVar()

        self.MainFrame1 = Frame(self.MainFrame, bd=22, width=500, height=600, relief= RIDGE, bg = "dodgerblue")
        self.MainFrame1.place(x=100,y=110)

        self.lblTitle = Label(self.MainFrame, font=("Arial", 55, "bold"), text="Request Repair", bg = "dodgerblue", anchor = "c")
        self.lblTitle.place(x=550,y=0)

        self.lblDescription =Label(self.MainFrame1, text="Description",font=("Arial",30,"bold"),bd=25,
                                bg="dodgerblue", fg="black")
        self.lblDescription.grid(row=0, column=0)
        
        self.txtDescription =Entry(self.MainFrame1,font=("Arial",30,"bold"),bd=7,textvariable=self.Description,
                                width=33)
        self.txtDescription.grid(row=0, column=1, padx=88)

        self.lblDate = Label(self.MainFrame1,text="Date",font=("Arial",30,"bold"),bd=22,
                                 bg="dodgerblue", fg="black")
        self.lblDate.grid(row=1, column=0)

        self.txtDate= Entry(self.MainFrame1,font=("Arial",30,"bold"),bd=7,textvariable=self.Date,
                                width=33)
        self.txtDate.grid(row=1, column=1, columnspan=2, pady=30)

        self.lblID = Label(self.MainFrame1,text="Enter Property ID",font=("Arial",30,"bold"),bd=22,
                                 bg="dodgerblue", fg="black")
        self.lblID.grid(row=2, column=0)

        self.txtID= Entry(self.MainFrame1,font=("Arial",30,"bold"),bd=7,textvariable=self.ID,
                                width=33)
        self.txtID.grid(row=2, column=1, columnspan=2, pady=30)

        self.btnReq = Button(self.MainFrame, text = "Request repair", width = 15, font=("Arial",30,"bold"),
                              bg="dodgerblue2", fg="black")
        self.btnReq.place(x=10,y=500)

        self.btnBack = Button(self.MainFrame, text = "Back", width = 8, font=("Arial",30,"bold"), bg="dodgerblue2", fg="black", command=lambda:controller.show_frame(View2))
        self.btnBack.place(x=10,y=10)


class JobView2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        
        self.root = tk.Frame(self,bg="dodgerblue")
        self.root.grid(row=0, column=0)
        
        
        blank_space = " "

        JobID = StringVar()
        Description = StringVar()
        Date = StringVar()
        Completed = StringVar()
        Cost = StringVar()
        StaffID = StringVar()
        PropertyID = StringVar()
    
#-----------------------------------------------------------------------------------------------Functions------------------------------------------------------------------------------------------------------            

        def Exit():
            Exit = tkinter.messagebox.askyesno("Property Management ","Confirm if you want to exit")
            if Exit > 0:
                self.root.destroy()
                
                return

        def searchData(JobID="", Description="", Date="", Completed="", Cost="", StaffID="", PropertyID=""):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM Job WHERE JobID=? OR Description=? OR Date=? OR Completed=? OR Cost=? OR StaffID=? OR PropertyID=?",(JobID, Description, Date, Completed, Cost, StaffID, PropertyID))
                rows = cur.fetchall()
                con.close()
                return rows

        def searchData1():
                for row in self.joblist.get_children():
                        self.joblist.delete(row)
                for row in searchData(JobID.get(), Description.get(), Date.get(), Completed.get(), Cost.get(), StaffID.get(), PropertyID.get()):
                        self.joblist.insert("", 'end', values= row)

        def Reset():
                self.txtJobID.delete(0, END)
                self.txtDescription.delete(0, END)
                self.txtDate.delete(0, END)
                self.txtCompleted.delete(0, END)
                self.txtCost.delete(0, END)
                self.txtStaffID.delete(0, END)
                self.txtPropertyID.delete(0, END)
                DisplayData()

        def updateJob(JobID, Description, Date, Completed, Cost, StaffID, PropertyID):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("UPDATE Job SET Description=?, Date=?, Completed=?, Cost=?, StaffID=?, PropertyID=? WHERE JobID = ?",(Description, Date, Completed, Cost, StaffID, PropertyID, JobID))
                con.commit()
                con.close()
                

        def addData():
                if JobID.get() =="" or Description.get() =="" or Date.get() =="" or Completed.get() =="" or Cost.get() =="" or StaffID.get() =="" or PropertyID.get() =="":
                        tkinter.messagebox.showinfo("Property Management App","Please Enter Valid Data")

                else:
                    addRecord(JobID.get(), Description.get(), Date.get(), Completed.get(), Cost.get(), StaffID.get(), PropertyID.get())
                    
                    super(self.joblist, self).delete()
                    
                    self.joblist.insert(END,(JobID.get(), Description.get(), Date.get(), Completed.get(), Cost.get(), StaffID.get(), PropertyID.get()))
                    DisplayData()

        def DisplayData():
                result = viewData()
                if len(result)!= 0:
                        self.joblist.delete(*self.joblist.get_children())
                        for row in result:
                                self.joblist.insert('',END,values =row)
                                
        def DeleteData():
                selectedRecord = self.joblist.focus()
                selectedRecord = self.joblist.item(selectedRecord)
                deleteRecord(selectedRecord["values"][0])
                DisplayData()
                tkinter.messagebox.showinfo("Property Management App","Record Successfully Deleted")
                DisplayData()
                Reset()

        def get_selected_row(event):
                try:
                        selectedRecord = self.joblist.focus()
                        selectedRecord=self.joblist.item(selectedRecord)
                        self.txtJobID.delete(0,END)
                        self.txtJobID.insert(END,selectedRecord["values"][0])
                        self.txtDescription.delete(0,END)
                        self.txtDescription.insert(END,selectedRecord["values"][1])
                        self.txtDate.delete(0,END)
                        self.txtDate.insert(END,selectedRecord["values"][2])
                        self.txtCompleted.delete(0,END)
                        self.txtCompleted.insert(END,selectedRecord["values"][3])
                        self.txtCost.delete(0,END)
                        self.txtCost.insert(END,selectedRecord["values"][4])
                        self.txtStaffID.delete(0,END)
                        self.txtStaffID.insert(END,selectedRecord["values"][5])
                        self.txtPropertyID.delete(0,END)
                        self.txtPropertyID.insert(END,selectedRecord["values"][6])
                except IndexError:
                        pass
                        
        def addRecord(JobID, Description, Date, Completed, Cost, StaffID, PropertyID):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("INSERT INTO Job VALUES (?,?,?,?,?,?,?)", \
                            (JobID, Description, Date, Completed, Cost, StaffID, PropertyID))
                con.commit()
                con.close()

        def viewData():
               con = sqlite3.connect("Landlord_App.db")
               cur = con.cursor()
               cur.execute("SELECT * FROM Job")
               rows = cur.fetchall()
               con.close()
               return rows

        def deleteRecord(Jobid):
                con = sqlite3.connect("Landlord_App.db")
                cur = con.cursor()
                cur.execute("DELETE FROM Job WHERE Jobid=?", (Jobid,))
                con.commit()
                con.close()

        def updateData():
                selectedRecord = self.joblist.focus()
                selectedRecord=self.joblist.item(selectedRecord)
                updateJob(selectedRecord["values"][0], Description.get(), Date.get(), Completed.get(), Cost.get(), StaffID.get(), PropertyID.get())
                viewData()
#-------------------------------------------------------------------------------------------Frames----------------------------------------------------------------------------------------------------------
        
        MainFrame = Frame(self.root, bd=25, width =1350, height =700, relief = RIDGE, bg = "dodgerblue")
        MainFrame.grid(row=0, column=0)
    
        TopFrame1 = Frame(MainFrame, bd=5, width =1340, height =50, relief = RIDGE)
        TopFrame1.grid(row = 2, column = 0, pady = 8)
        TitleFrame = Frame(MainFrame, bd=7, width =1340, height =100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)
        TopFrame3 = Frame(MainFrame, bd=5, width = 1340, height = 500, relief = RIDGE)
        TopFrame3.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame3, bd = 5, width = 1340, height = 400, padx = 2, bg="dodgerblue2", relief = RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd = 5, width = 600, height = 180, padx = 2, pady = 4, relief = RIDGE)
        LeftFrame1.pack(side=TOP, padx = 0, pady = 4)

        RightFrame1 = Frame(TopFrame3, bd = 5, width = 320, height = 400, padx = 2, pady = 2, relief =  RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd = 5, width = 310, height = 200, padx = 2, pady = 2)
        RightFrame1a.pack(side=TOP)

        


        self.lblTitle = Label(TitleFrame, font=("Arial", 56,"bold"), text ="Maintenance Hub", bd=7)
        self.lblTitle.grid(row=0, column=0, padx=132)

#----------------------------------------------------------------------------------Entry widgets-----------------------------------------------------------------------------------------------------

        self.lblJobID = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Job ID", bd=7, anchor = "w", justify=LEFT)
        self.lblJobID.grid(row=0, column=0, sticky = W, padx = 5)
        self.txtJobID = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable =   JobID)
        self.txtJobID.grid(row=0, column=1)

        self.lblDescription = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Description", bd=7, anchor = "w", justify=LEFT)
        self.lblDescription.grid(row=1, column=0, sticky = W, padx = 5)
        self.txtDescription = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Description)
        self.txtDescription.grid(row=1, column=1)

        self.lblDate = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Date", bd=7, anchor = "w", justify=LEFT)
        self.lblDate.grid(row=2, column=0, sticky = W, padx = 5)
        self.txtDate = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Date)
        self.txtDate.grid(row=2, column=1)

        self.lblCompleted = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Completed", bd=7, anchor = "w", justify=LEFT)
        self.lblCompleted.grid(row=3, column=0, sticky = W, padx = 5)
        self.txtCompleted = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Completed)
        self.txtCompleted.grid(row=3, column=1)

        self.lblCost = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Cost", bd=7, anchor = "w", justify=LEFT)
        self.lblCost.grid(row=4, column=0, sticky = W, padx = 5)
        self.txtCost = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = Cost)
        self.txtCost.grid(row=4, column=1)

        self.lblStaffID = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Staff ID", bd=7, anchor = "w", justify=LEFT)
        self.lblStaffID.grid(row=5, column=0, sticky = W, padx = 5)
        self.txtStaffID = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = StaffID)
        self.txtStaffID.grid(row=5, column=1)

        self.lblPropertyID = Label(LeftFrame1, font=("Arial", 12,"bold"), text ="Property ID", bd=7, anchor = "w", justify=LEFT)
        self.lblPropertyID.grid(row=6, column=0, sticky = W, padx = 5)
        self.txtPropertyID = Entry(LeftFrame1, font=("Arial", 12,"bold"), bd=5, width = 20, justify="left", textvariable = PropertyID)
        self.txtPropertyID.grid(row=6, column=1)

        
#-----------------------------------------------------------------------------------------Treeview-------------------------------------------------------------------------------------------------

        scroll_x = Scrollbar(RightFrame1a, orient = HORIZONTAL)
        scroll_y = Scrollbar(RightFrame1a, orient = VERTICAL)

        self.joblist = ttk.Treeview(RightFrame1a, height = 12, columns =("JobID", "Description", "Date", "Completed", "Cost", "StaffID", "PropertyID"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        self.joblist.heading("JobID",text="JobID")
        self.joblist.heading("Description",text="Description")
        self.joblist.heading("Date",text="Date")
        self.joblist.heading("Completed",text="Completed")
        self.joblist.heading("Cost",text="Cost")
        self.joblist.heading("StaffID",text="StaffID")
        self.joblist.heading("PropertyID",text="PropertyID")

        self.joblist["show"] = "headings"

        self.joblist.column("JobID", width = 110)
        self.joblist.column("Description", width = 150)
        self.joblist.column("Date", width = 130)
        self.joblist.column("Completed", width = 100)
        self.joblist.column("Cost", width = 80)
        self.joblist.column("StaffID", width = 80)
        self.joblist.column("PropertyID", width = 80)

        self.joblist.pack(fill = BOTH, expand = 1)
        self.joblist.bind('<ButtonRelease-1>', get_selected_row)
        DisplayData()

#---------------------------------------------------------------------------------------------Buttons--------------------------------------------------------------------------------------------------------

        self.btnAddNew = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Add new", padx = 24, width = 9, height = 2, relief = RAISED, command = addData).grid(row = 0,column = 0, padx = 1)

        self.btnDisplay = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Display", padx = 24, width = 9, height = 2, relief = RAISED, command = DisplayData).grid(row = 0,column = 1, padx = 1)

        self.btnDelete = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Delete", padx = 24, width = 9, height = 2, relief = RAISED, command = DeleteData).grid(row = 0,column = 2, padx = 1)

        self.btnReset = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Reset", padx = 24, width = 9, height = 2, relief = RAISED, command = Reset).grid(row = 0,column = 3, padx = 1)

        self.btnExit = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Update", padx = 24, width = 9, height = 2, relief = RAISED, command = updateData).grid(row = 0,column = 4, padx = 1)

        self.btnSearch = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Search", padx = 24, width = 9, height = 2, relief = RAISED, command = searchData1).grid(row = 0, column = 5, padx = 1)

        self.btnUpdate = Button(TopFrame1, pady = 1, bd = 4, font=("Arial",18, "bold"), text = "Exit", padx = 24, width = 9, height = 2, relief = RAISED, command = Exit).grid(row = 0, column = 6, padx = 1)

        self.btnBack = Button(MainFrame, pady = 1,bd = 4, font=("Arial",18, "bold"), text = "Back", padx = 24, width = 9, height = 2, relief = RIDGE, command=lambda:controller.show_frame(View3)).place(x=0,y=0)


 


app = tkinterApp()
app.mainloop()
