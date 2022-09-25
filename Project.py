import mysql.connector as mysql
import datetime
import tkinter as tk

# SHOP OWNER

class login():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.minsize(300,150)
        self.window.configure(background="#ADFF2F") #lime lel
        self.userlabel = tk.Label(self.window, text="Username").pack()
        self.userinput = tk.Entry(self.window)
        self.userinput.pack()
        self.pwlabel = tk.Label(self.window, text="Password").pack()
        self.userpw = tk.Entry(self.window)
        self.userpw.pack()
        self.submitbutton = tk.Button(text="Login", command=self.check).pack()
        self.window.mainloop()

    def check(self):
        self.username = self.userinput.get()
        self.password = self.userpw.get()
        if self.username == 'marvel' and self.password == '1234':
            self.GD_USER = tk.Label(self.window, text="Correct user name and password").pack()
            self.window.destroy()
        else:
            self.BD_USER = tk.Label(self.window, text="Incorrect username or password").pack()

def createdb():
    global mycon
    global mycur
    mycon=mysql.connect(host="localhost",user="root",password="dbase")
    mycur=mycon.cursor()
    mycur.execute("Create database if not exists medical")
    mycur.execute("Use medical")
    if mycon.is_connected():
        print("\n>>> Connected to Inventory Database Server <<<")
    cmd1="Create table if not exists _medicalproject(ProductCode integer primary key,name char(50) not null,Packing char(50),Expirydate date,"\
    "Company char(50),Batch integer,Quantity integer,Rate integer)"
    mycur.execute(cmd1)

def add_medicine():
    ProductCode=int(input("Enter the product code:"))
    name=input("Enter name of the medicine:")
    Packing=input("Enter the packing details:")       
    ExpiryDate=input("Enter expiry date of medicine(yyyy/mm/dd):")
    Company=input("Enter name of the company:")
    Batch=int(input("Enter batch number of medicine:"))
    Quantity=int(input("Enter quantity of medicine:"))
    Rate=int(input("Enter rate of medicine:"))
    cmd3 = "insert into _medicalproject values ("+str(ProductCode)+",'"+name+"','"+Packing+"','"+str(ExpiryDate)+"',\
        '"+Company+"',"+str(Batch)+","+str(Quantity)+","+str(Rate)+")"
    mycur.execute(cmd3)
    print("Record has been added successfully")

def display_medicine():
    cmd4 = "select * from _medicalproject"
    mycur.execute(cmd4)
    r1 = mycur.fetchall()
    print("================================================================================================================")
    print("| PRODUCT CODE   MEDICINE NAME   PACKING DETAILS   EXPIRY DATE   COMPANY NAME    BATCH NUMBER  QUANTITY   RATE |")
    print("================================================================================================================")
    for i in range(len(r1)):
        print("| ",end="")
        print(str(r1[i][0]).ljust(15," "),end="")
        print(r1[i][1].ljust(16," "),end="")
        print(r1[i][2].ljust(18," "),end="")
        print(str(r1[i][3]).ljust(14," "),end="")
        print(r1[i][4].ljust(16," "),end="")
        print(str(r1[i][5]).ljust(14," "),end="")
        print(str(r1[i][6]).ljust(11," "),end="")
        print(str(r1[i][7]).ljust(5," "),end="|")
        print()
    print("================================================================================================================")

def search_medicine():
    med_name= input("Enter medicine name for search: ")
    cmd5 = "select * from _medicalproject where name like '%"+med_name+"%'"
    mycur.execute(cmd5)
    r2 = mycur.fetchall()
    print("================================================================================================================")
    print("| PRODUCT CODE   MEDICINE NAME   PACKING DETAILS   EXPIRY DATE   COMPANY NAME    BATCH NUMBER  QUANTITY   RATE |")
    print("================================================================================================================")
    for i in range(len(r2)):
        print("| ",end="")
        print(str(r2[i][0]).ljust(15," "),end="")
        print(r2[i][1].ljust(16," "),end="")
        print(r2[i][2].ljust(18," "),end="")
        print(str(r2[i][3]).ljust(14," "),end="")
        print(r2[i][4].ljust(16," "),end="")
        print(str(r2[i][5]).ljust(14," "),end="")
        print(str(r2[i][6]).ljust(11," "),end="")
        print(str(r2[i][7]).ljust(5," "),end="|")
        print()
    print("================================================================================================================")

def expiry_stock():
    expdate=datetime.date.today()
    y1=expdate.year
    cmd6 ="select ProductCode,name,Expirydate,Batch from _medicalproject where Expirydate <='"+str(expdate)+"'"
    mycur.execute(cmd6)
    r3 = mycur.fetchall()
    print("========================================================")
    print("| PRODUCT CODE   NAME             EXPIRY DATE   BATCH  |")  
    print("========================================================")
    for i in range(len(r3)):
        print("| ",end="")
        print(str(r3[i][0]).ljust(15," "),end="")
        print((r3[i][1]).ljust(17," "),end="")
        print(str(r3[i][2]).ljust(14," "),end="")
        print(str(r3[i][3]).ljust(7," "),end="|")
        print()
    print("========================================================")

def display_companywise():
    company_name= input("Enter the company name you want to display:")
    cmd7=" select * from _medicalproject where Company = '"+company_name+"'"
    mycur.execute(cmd7)
    r4 = mycur.fetchall()
    print("================================================================================================================")
    print("| PRODUCT CODE   MEDICINE NAME   PACKING DETAILS   EXPIRY DATE   COMPANY NAME    BATCH NUMBER  QUANTITY   RATE |")
    print("================================================================================================================")
    for i in range(len(r4)):
        print("| ",end="")
        print(str(r4[i][0]).ljust(15," "),end="")
        print(r4[i][1].ljust(16," "),end="")
        print(r4[i][2].ljust(18," "),end="")
        print(str(r4[i][3]).ljust(14," "),end="")
        print(r4[i][4].ljust(16," "),end="")
        print(str(r4[i][5]).ljust(14," "),end="")
        print(str(r4[i][6]).ljust(11," "),end="")
        print(str(r4[i][7]).ljust(5," "),end="|")
        print()
    print("================================================================================================================")

def delete_medicine():
    delete_medicine=int(input("Enter the medicine product code that you want to delete:"))
    cmd8="delete from _medicalproject where ProductCode="+str(delete_medicine)+""
    mycur.execute(cmd8)
    print("Record has been deleted")
 
# Main Menu
print("\n>>> Marvel Medical Store <<<")
createdb()
while True:
    print("\n-------------MAIN MENU--------------------")
    print("(1)Shop owner(Admin)  (2)Exit")
    choice=int(input("Please enter your choice:"))
    if(choice==1):
        login()
        while True:
            print("\n\n----SHOP OWNER----\n")
            print("(1)ADD MEDICINE                  (2)DISPLAY ALL MEDICINE  (3)SEARCH MEDICINE")
            print("(4)DISPLAY MEDICINES COMPANYWISE (5)CHECK EXPIRY STOCK    (6)DELETE MEDICINE")
            print("(7)EXIT") 
            choice1=int(input("Please enter your choice:"))
            if(choice1==1):
                add_medicine()
            elif(choice1==2):
                display_medicine()
            elif(choice1==3):
                search_medicine()
            elif(choice1==4):
                display_companywise()
            elif (choice1==5):
                expiry_stock()
            elif(choice1==6):
                delete_medicine()
            elif(choice1==7):
                break
                

    if(choice==2):
        mycon.commit()
        break
