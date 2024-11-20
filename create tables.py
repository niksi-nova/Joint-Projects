# Anika & Sanjana Project Create Tables & Admin
import mysql.connector
cnx=mysql.connector.connect(user="root",password="sql123",host="localhost")
cursor=cnx.cursor()
query="drop database if exists project_anika_sanjana"
cursor.execute(query)
cnx.commit()
query="create database project_anika_sanjana"

cursor.execute(query)
print("Database created")
query="use project_anika_sanjana"
cursor.execute(query)
print("Using project_anika_sanjana")
query="create table user(username varchar(25) primary key, password varchar(15));"
cursor.execute(query)
cursor.execute("create table customer(Cust_name varchar(30), phno integer primary key, num_orders integer,discount_percent integer);")
cursor.execute("create table vegetables(slno integer primary key,veg_name varchar(20),stock integer);")
cursor.execute("create table sauce(slno integer primary key,sauce_name varchar(20),stock integer);")
cursor.execute("create table meat(slno integer primary key,meat_name varchar(20),stock integer);")
cursor.execute("create table sales(ph_s int primary key,total integer);")
cursor.execute("create table menu(Slno integer primary key,dish varchar(30), price integer, availability varchar(20));")
cursor.execute("create table cart(slno integer, dish_name varchar(30),details varchar(50), quantity integer, price integer)")
print("Tables created!")

query='insert into menu values(1,"Taco",200,"Available")'
cursor.execute(query)

query='insert into menu values(2,"Burrito",210,"Available")'
cursor.execute(query)

query='insert into menu values(3,"Loaded Nacho",200,"Available")'
cursor.execute(query)

query='insert into menu values(4," Quesedilla",200,"Available")'
cursor.execute(query)
query='insert into menu values(5,"Chocolate Churros",150,"Available")'
cursor.execute(query)
cnx.commit()
print("Items inserted in menu")

query='insert into vegetables values(1,"Lettuce",50)'
cursor.execute(query)

query='insert into vegetables values(2,"Onion",50)'
cursor.execute(query)

query='insert into vegetables values(3,"Tomato",50)'
cursor.execute(query)

query='insert into vegetables values(4,"Jalapeno",50)'
cursor.execute(query)

query='insert into vegetables values(5,"Olive",50)'
cursor.execute(query)
cnx.commit()
print("Items inserted in vegetables")

query='insert into meat values(1,"Chicken",50)'
cursor.execute(query)

query='insert into meat values(2,"Fish",50)'
cursor.execute(query)

query='insert into meat values(3,"Shrimp",50)'
cursor.execute(query)
cnx.commit()
print('Items inserted in meat')

query='insert into sauce values(1,"Mayo",50)'
cursor.execute(query)

query='insert into sauce values(2,"Southwest",50)'
cursor.execute(query)

query='insert into sauce values(3,"Thousand Island",50)'
cursor.execute(query)

query='insert into sauce values(4,"Sweet Onion",50)'
cursor.execute(query)

query='insert into sauce values(5,"Honey Mustard",50)'
cursor.execute(query)
cnx.commit()
print("Items inserted in sauce")
print()
#to input username details for admins
def useradmin():
    n=int(input("Enter number of admins "))
    print()
    for i in range(n):
        username=input("Enter username ")
        passwd=input("Enter password ")
        query="insert into user values ('{}','{}')".format(username,passwd)
        cursor.execute(query)
        cnx.commit()
        print()

useradmin()



