#Anika & Sanjana Project Main code
import mysql.connector
import tabulate
from tkinter import *
from tkinter import messagebox
cnx=mysql.connector.connect(user="root",password="sql123",host="localhost")
query="use project_anika_sanjana"
cursor=cnx.cursor()
cursor.execute(query)

ww=0
def menu():
    if cnx.is_connected():
        c=cnx.cursor()
        q="select * from menu"
        c.execute(q)
        a=c.fetchall()
        
        root1 = Tk() 
        root1.geometry("900x610") 
        bg = PhotoImage(file = "bg1.png") 
        label1 = Label( root1, image = bg) 
        label1.place(x = 0, y = 0) 
        frame1 = Frame(root1) 
        frame1.pack(pady = 20 )
        root1.title("Menu")
        y=Label(root1,text="Menu", font= ('Broadway 20'))
        y.pack(pady=25)
        p=Label(root1,text="Sl no         Item Name         Price(₹)         Availability",font=('Broadway 20'))
        p.pack(pady=10)
        for i in a:
            o,w,e,r=i
            q=str(o)+" "*(25-len(str(o)))+str(w)+" "*(25-len(str(w)))+str(e)+" "*(25-len(str(e)))+str(r)
            z=Label(root1,text=q, font=('Broadway 20'))
            z.pack(pady=10)
    
    
        root1.mainloop()

        return len(a)
    

def order():
    if cnx.is_connected():
        c=cnx.cursor()
        while True:
            number_of_items=menu()
            
            ch=int(input('Enter sl no of the dish you want to order '))
            if ch in range(number_of_items+1):
                q=int(input('Enter quantity '))
                break
            else:
                print('Invalid slno....Please enter valid slno')
        if ch==1 or ch==2 or ch==4:
            choice_veg=veg(ch)
            choice_veg_sauce=sauces(choice_veg)
            m=input('Do you want meat? (Yes/No) ').lower()
            
            if m=='yes':
                choice_veg_sauce_meat=meat(choice_veg_sauce)
                
            cart(choice_veg_sauce,q)
        if ch==3:
            cart(ch,q)
        if ch==5:
            cart(ch,q)
        if ch==0:
            bill()
        return ch,q


def cart(ch,q):
    
    if cnx.is_connected():
        c=cnx.cursor()
        c.execute('select * from menu ;')
        data=c.fetchall()
        a=str(type(ch))
        if a=="<class 'list'>":
            if ch[0] in (1,2,4):
                l=len(ch)
                st=''
                for i in range(1,l):
                    st+=ch[i]+' '
            
                count=0
                for i in data:
                    if i[0]==ch[0]:
                        if count==0:
                            count+=1
                            query="select count(*) from cart"
                            c.execute(query)
                            d=c.fetchone()
                            
                            qu="insert into cart values({},'{}','{}',{},{})".format(d[0]+1,i[1],st,q,q*i[2])
                            cursor.execute(qu)
                            cnx.commit()
                            break
        else:
            
            for i in data:
                if i[0]==ch:
                    query="select count(*) from cart"
                    c.execute(query)
                    d=c.fetchone()
                    qu="insert into cart values({},'{}','{}',{},{})".format(d[0]+1,i[1],"N/A",q,q*i[2])
                    cursor.execute(qu)
                    cnx.commit()
                    break
def admintk():                
    def adminchk():
        userid=username_entry.get()
        global ww
        count=0
        if cnx.is_connected():
            c=cnx.cursor()
            c.execute('select * from user ;')
            data=c.fetchall()
            check=0
            v=0
            w=0
            password_correct = False
        while count<3 or password_correct == True :
                for j in data:
                    
                    if j[0]==userid:
                        i=j
                        w=1
                        if v==0:
                            password=password_entry.get()
                            count+=1
                            v=1
                        break
                if w==0:
                    messagebox.showerror("Username does not exist!")
                    break
                
                if i[1]!=password:
                    messagebox.showerror("Password Incorrect!")
                    password=password_entry.get()
                    count+=1

                if i[1]==password:
                    
                    password_correct = True
                    messagebox.showinfo("Login Successful","Welcome, Admin!")
                    ww=1
                    break
    
    root = Tk() 
    root.geometry("900x610") 
    bg = PhotoImage(file = "bg2.png") 
    label1 = Label( root, image = bg) 
    label1.place(x = 0, y = 0) 
    frame1 = Frame(root) 
    frame1.pack(pady = 20 )
    root.title("Aztec Fiesta ")
    y=Label(root,text="Aztec Fiesta ", font= ('Broadway 20'))
    y.pack(pady=25)
    username_label = Label(root, text="Username:", font= ('Broadway 20'))
    username_label.pack(pady=20)
    username_entry = Entry(root)
    username_entry.pack(pady=20)
    password_label = Label(root, text="Password:", font= ('Broadway 20'))
    password_label.pack(pady=20)
    password_entry = Entry(root, show="*")  
    password_entry.pack(pady=20)
    login_button = Button(root, text="Login", command=adminchk, font= ('Broadway 21'))
    login_button.pack(pady=20)
    root.mainloop()
    admin()

    

def admin():
    global ww
    print()
    print('Welcome please select which action you want to perform ')               
    if ww==1:
        while True:
            print()
            print("1. To View Sales")
            print("2. To restock supplies when stock is less than 10")
            print("3. To View Stock")
            print("4. To Add a dish to the menu")
            print("5. To Delete a dish from the menu")
            print("6. To Exit")
            print()
            a=int(input('Enter choice '))
            print()
            if a==1:
                salesview()
            if a==2:
                restock()
            if a==3:
                view_stock()
            if a==4:
                add_ing()
            if a==5:
                delete_ingredente()
                            
            if a==6:
                break
         
                    
def view_stock():
    print()
    print("1. View vegetables stock")
    print("2. View meats stock")
    print("3. View sauces stock")
    print()
    vh=int(input("Enter choice"))
    if vh==1:
        query="select * from vegetables"
        cursor.execute(query)
        d=cursor.fetchall()
        heading=["Slno","Item","Stock"]
        print(tabulate.tabulate(d,headers=heading))
    if vh==2:
        query="select * from meat"
        cursor.execute(query)
        d=cursor.fetchall()
        heading=["Slno","Item","Stock"]
        print(tabulate.tabulate(d,headers=heading))
    if vh==3:
        query="select * from sauce"
        cursor.execute(query)
        d=cursor.fetchall()
        heading=["Slno","Item","Stock"]
        print(tabulate.tabulate(d,headers=heading))

def add_ing():
    print()
    print("1. Add to vegetables")
    print("2. Add to meat")
    print("3. Add to sauce")
    print()
    vh=int(input("Enter choice"))
    if vh==1:
        v=input("Enter vegetable to add ")
        st=int(input("Enter stock "))
        query="select * from vegetables;"
        cursor.execute(query)
        d=cursor.fetchall()
        sln=(d[(len(d)-1)][0]) +1
        query="insert into vegetables values({},'{}',{})".format(sln,v,st)
        cursor.execute(query)
        cnx.commit()
    if vh==2:
        v=input("Enter meat to add ")
        st=int(input("Enter stock "))
        query="select * from meat;"
        cursor.execute(query)
        d=cursor.fetchall()
        sln=(d[(len(d)-1)][0]) +1
        query="insert into meat values({},'{}',{})".format(sln,v,st)
        cursor.execute(query)
        cnx.commit()
    if vh==3:
        v=input("Enter sauce to add ")
        st=int(input("Enter stock "))
        query="select * from sauce;"
        cursor.execute(query)
        d=cursor.fetchall()
        sln=(d[(len(d)-1)][0]) +1
        query="insert into sauce values({},'{}',{})".format(sln,v,st)
        cursor.execute(query)
        cnx.commit()
    



def delete_ingredente():
    print()
    print('1. To delete from vegetables')
    print('2. To delete from meats')
    print('3. To felete from sauces')
    print()
    
    ch=int(input('enter choice '))
    if ch==1:
        c=cnx.cursor()
        q="select * from vegetables;"
        c.execute(q)
        b=c.fetchall()
        heading=['Sl no','Vegetables','Stock']
        print(tabulate.tabulate(b,headers = heading))
        option=int(input('Enter the slno of the ingredente you want to delete '))
        tot=len(b)
            
        for i in range(tot):
            if b[i][0]==option:
                    
                q="delete from vegetables where slno={}".format(option)
                c.execute(q)
                cnx.commit()
                break
            
        for j in range (option,tot+1):
            q='update vegetables set slno={} where slno={}'.format(j-1,j)
            c.execute(q)
            cnx.commit()
                
    if ch==2:
        c=cnx.cursor()
        q="select * from meat;"
        c.execute(q)
        b=c.fetchall()
        heading=['Sl no','Meat','Stock']
        print(tabulate.tabulate(b,headers = heading))
        option=int(input('Enter the slno of the ingredente you want to delete '))
        tot=len(b)
            
        for i in range(tot):
            if b[i][0]==option:
                    
                q="delete from meat where slno={}".format(option)
                c.execute(q)
                cnx.commit()
                break
            
        for j in range (option,tot+1):
            q='update meat set slno={} where slno={}'.format(j-1,j)
            c.execute(q)
            cnx.commit()
    if ch==3:
            c=cnx.cursor()
            q="select * from sauce;"
            c.execute(q)
            b=c.fetchall()
            heading=['Sl no','Sauce','Stock']
            print(tabulate.tabulate(b,headers = heading))
            option=int(input('Enter the slno of the ingredente you want to delete '))
            tot=len(b)
            
            for i in range(tot):
                if b[i][0]==option:
                    
                    q="delete from sauce where slno={}".format(option)
                    c.execute(q)
                    cnx.commit()
                    break
            
            for j in range (option,tot+1):
                q='update sauce set slno={} where slno={}'.format(j-1,j)
                c.execute(q)
                cnx.commit()
    else:
        print('Invalid value entered')

    
        
def restock():
    if cnx.is_connected():
        c=cnx.cursor()
        while True:
            print()
            print("1. To retock vegetables where stock less than 10")
            print("2. To restock meat where stock less than 10")
            print("3. To restock sauce where stock less than 10")
            print("4. To exit")
            print()
            ch=int(input("Please enter your choice "))
            
            if ch==1:
                c.execute('update vegetables set stock=50 where stock<10 ;')
                cnx.commit()
            elif ch==2:
                c.execute('update meat set stock=50 where stock<10 ;')
                cnx.commit()
            elif ch==3:
                c.execute('update sauce set stock=50 where stock<10 ;')
                cnx.commit()
            elif ch==4:
                break


                


def veg(item):
    if cnx.is_connected():
        l=[item]
        c=cnx.cursor()
        
        q="select slno, veg_name from vegetables;"
        c.execute(q)
        a=c.fetchall()
        heading=['Sl no','Vegetables']
        print(tabulate.tabulate(a,headers = heading))
        print()
        print("Please Select the SlNo of the vegetable you want to add and enter 0 to finish")
        
        while True:
            print()
            ch=int(input('Enter choice please '))
            
            if ch==0:
                    break
            if ch in range(len(a)+1):
                q="select stock from vegetables where slno={}".format(ch)
                c.execute(q)
                d=c.fetchone()
               
                if str(d[0])=="0":
                    print("OUT OF STOCK")
                    continue
                else:
                    
                    l+=[a[ch-1][1]]
                    c.execute("update vegetables set stock=stock-1 where veg_name='{}'".format(a[ch-1][1]))
            else:
                print('Invalid slno....please enter valid slno')
        return l

def meat(choice_veg_sauce):
    if cnx.is_connected():
        l=choice_veg_sauce
        c=cnx.cursor()
        q="select slno, meat_name from meat;"
        c.execute(q)
        a=c.fetchall()
        heading=['Sl no','Meats']
        print(tabulate.tabulate(a,headers = heading))
        print()
        print("Please Select the SlNo of the meat you want to add and enter 0 to finish")
        
        while True:
            print()
            ch=int(input('Enter number please '))
            if ch==0:
                    break
            if ch in range(len(a)+1):
                q="select stock from meat where slno={}".format(ch)
                c.execute(q)
                d=c.fetchone()
                
                if str(d[0])=="0":
                    print("OUT OF STOCK")
                    continue
                else:
                    
                    l+=[a[ch-1][1]]
                    c.execute("update meat set stock=stock-1 where meat_name='{}'".format(a[ch-1][1]))
            else:
                print('Invalid slno....please enter valid slno')
        return l

def sauces(choice_veg):
    if cnx.is_connected():
        l=choice_veg
        c=cnx.cursor()
        q="select slno, sauce_name from sauce;"
        c.execute(q)
        a=c.fetchall()
        heading=['Sl no','Sauces']
        print(tabulate.tabulate(a,headers = heading))
        print()
        print("Please Select the SlNo of the sauce you want to add and enter 0 to finish")
        while True:
            print()
            ch=int(input('Enter number please '))
            if ch==0:
                    break
            if ch in range(len(a)+1):
                q="select stock from sauce where slno={}".format(ch)
                c.execute(q)
                d=c.fetchone()
                
                if str(d[0])=="0":
                    print("OUT OF STOCK")
                    continue
                else:
                    
                    l+=[a[ch-1][1]]
                    c.execute("update sauce set stock=stock-1 where sauce_name='{}'".format(a[ch-1][1]))
            else:
                print('Invalid slno....please enter valid slno')
        return l
        
def discount():
    query="update customer set discount_percent = 5 where num_orders>5;"
    cursor.execute(query)
    cnx.commit()
    query="update customer set discount_percent = 10 where num_orders>10;"
    cursor.execute(query)
    cnx.commit()
def bill(ph):
    if cnx.is_connected():
        discount()
        cursor.execute("select * from cart")
        totals=0
        data=cursor.fetchall()
        
        if data==[]:
            print()
            print("CART IS EMPTY")
            gg=0
        else:
            print()
            print(" "*25,'AZTEC FIESTA')
            print()
            
            heading=["Sl.no","Dish name","Details","Quantity","Price"]
            for i in range(len(data)):
                totals+=data[i][4]
            print(tabulate.tabulate(data,headers=heading, tablefmt='grid'))
            print()
            print("TOTAL:   ",totals)
            query='select discount_percent from customer where phno={}'.format(phno)
            cursor.execute(query)
            d=cursor.fetchall()
            discount_percent=d[0][0]
            totals-=totals*(discount_percent)/100
            print("DISCOUNT:    ",discount_percent,"%")
            print("GRAND TOTAL:   ",totals)
            query="select phno from customer;"
            cursor.execute(query)
            data=cursor.fetchall()
            c=0
            for i in data:
                if i[0]==ph:
                    c=1
                    break
            if c==1:
                customer_table(ph)
            query="update customer set num_orders=num_orders+1 where phno={}".format(ph)
            cursor.execute(query)
            cnx.commit()
            query="drop table cart;"
            cursor.execute(query)
            cnx.commit()
            query="create table cart(slno integer, dish_name varchar(30),details varchar(200) default'None' ,quantity integer, price integer);"
            cursor.execute(query)
            cnx.commit()
            print("Thank You for ordering!")
            gg=1
            
def salesview():
    if cnx.is_connected():
        cursor.execute("select * from customer;")
        data=cursor.fetchall()
        heading=["Customer Name","Phone Number","Number of Orders","Discount %"]
        print(tabulate.tabulate(data,headers=heading))
        
def customer_table(ph):
    if cnx.is_connected():
        c=0
        query="select phno from customer;"
        cursor.execute(query)
        data=cursor.fetchall()
        for i in data:
            if i[0]==ph:
                c=1
                break
        if c==0:
            name=input("Enter name")
            query="insert into customer values('{}',{},{},{})".format(name,ph,0,0)
            cursor.execute(query)
            cnx.commit()
        query="update customer set discount_percent=10 where num_orders>=5;"
        cursor.execute(query)
        cnx.commit()
def func():
    customer_table(phno)
    print()
    print("Welcome!")
    while True:
        print()
        print("Enter 1. To view menu")
        print("2. To place an order")
        print("3. To view cart")
        print("4. To generate the bill")
        print()
        chs=int(input("Enter choice please "))
        print()
        if chs==1:
            menu()
        elif chs==2:
            order()
            
        elif chs==3:
            query="select * from cart;"
            cursor.execute(query)
            d=cursor.fetchall()
            if d==[]:
                print("CART IS EMPTY")
            else:
                heading=['Slno','Dish Name','Details','Quantity','Price']
                print(tabulate.tabulate(d,headers=heading,tablefmt='grid'))
        elif chs==4:
            bill(phno)
            break



print()
print("_"*80)
print()
print(" "*30,"Aztec Fiesta  ")
print("_"*80)
print()
print("1. Admin")
print("2. Customer")
counter=1
print()
ch=int(input("Please enter choice "))
if ch==1:
    admintk()
elif ch==2:
    print()
    phno=int(input("Please enter your phone number "))
    q="select * from customer;"
    cursor.execute(q)
    d=cursor.fetchall()
    if d==[]:
        func()
    else:
        for i in d:
            if phno in i:
                print("Welcome ",i[0])
                
                while True:
                    
                    print()
                    print("Enter 1. To view menu")
                    print("2. To place an order")
                    print("3. To view cart")
                    print("4. To generate the bill")
                    print()
                    chs=int(input("Enter choice please "))
                    print()
                    if chs==1:
                        menu()
                    elif chs==2:
                        order()
            
                    elif chs==3:
                        query="select * from cart;"
                        cursor.execute(query)
                        d=cursor.fetchall()
                        if d==[]:
                            print("CART IS EMPTY")
                        else:
                            heading=['Slno','Dish Name','Details','Quantity','Price']
                            print(tabulate.tabulate(d,headers=heading))
                    elif chs==4:
                        
                        bill(phno)
                        counter=4
                        
                        break
                    else:
                        print('Invalid slno')
                
           
            elif counter!=4:
                func()
                break
else:
    print('INVALID VALUE ENTERED')

      
#END
    
