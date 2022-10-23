import sqlite3

import time

import datetime

class product():

    def __init__(self,name,brand,expiration_date,sales_location,price,stock_status):
        self.name = name
        self.brand = brand
        self.expiration_date = expiration_date
        self.sales_location = sales_location
        self.price = price
        self.stock_status = stock_status


    def __str__(self):
        return "Product Name = {}\nProduct Brand = {}\nExpiration Date = {}\nSales Location = {}\nThe Price of the Product = {}\nStock Status = {}".format(self.name,self.brand,self.expiration_date,self.sales_location,self.price,self.stock_status)

class AVM():

    def __init__(self):

        self.create_link()

    def create_link(self):

        self.link = sqlite3.connect("shopping_center.db")
        self.cursor = self.link.cursor()

        code = "Create table if not exists AVM (name TEXT,brand TEXT,expiration_date TEXT,sales_location TEXT,price FLOAT,stock_status INT)"

        self.cursor.execute(code)
        self.link.commit()

    def disconnect(self):

        self.link.close()

    def show_product(self):

        code = "Select * From AVM"
        self.cursor.execute(code)

        liste = self.cursor.fetchall()

        if(len(liste) == 0):
            print("Product Don't exists")
        else:
            for i in liste:
                data = product(i[0],i[1],i[2],i[3],i[4],i[5])
                print(data)

    def search_product(self,name):

        code = "Select * From AVM where name = ?"
        self.cursor.execute(code, (name,))

        liste = self.cursor.fetchall()

        if (len(liste) == 0):
            print("This product doesn't exist")
        else:
            for i in liste:
                data = product(i[0], i[1], i[2], i[3], i[4], i[5])
                print(data)
                time.sleep(1)
                if(i[5] == 0):
                    print("The product is out of stock")
                elif(i[5] == 1):
                    print("The last 1 product remain")
                elif(i[5] == 2):
                    print("The last 2 product remain")
                elif (i[5] == 3):
                    print("The last 3 product remain")
                elif (i[5] == 4):
                    print("The last 4 product remain")
                elif (i[5] == 5):
                    print("The last 5 product remain")
                else:
                    print("Get it before it runs out of stock")

    def add_product(self,product):

        code = "INSERT INTO AVM VALUES(?,?,?,?,?,?)"
        self.cursor.execute(code,(product.name,product.brand,product.expiration_date,product.sales_location,product.price,product.stock_status))

        self.link.commit()

    def delete_product(self,name):

        code = "Delete From AVM where name = ?"
        self.cursor.execute(code, (name,))

        self.link.commit()

    def search_mall(self,sales_location):

        code = "Select * From AVM where sales_location = ?"
        self.cursor.execute(code, (sales_location,))

        liste = self.cursor.fetchall()

        if (len(liste) == 0):
            print("This sales location doesn't exist")
        else:
            for i in liste:
                data = product(i[0], i[1], i[2], i[3], i[4], i[5])
                print(data)


    def Raise(self,name,ratio):

        code = "Select * From AVM where name = ?"
        self.cursor.execute(code, (name,))

        liste = self.cursor.fetchall()

        if (len(liste) == 0):
            print("This product don't exist")
        else:
            price = liste[0][4]
            price += ((price * ratio) // 100)


            code2 = "Update AVM set price = ? where name = ?"
            self.cursor.execute(code2, (price, name))

            self.link.commit()

            return price

    def sale(self,name,ratio):

        code = "Select * From AVM where name = ?"
        self.cursor.execute(code, (name,))

        liste = self.cursor.fetchall()

        if (len(liste) == 0):
            print("This product don't exist")
        else:
            price = liste[0][4]
            price -= ((price * ratio) // 100)


            code2 = "Update AVM set price = ? where name = ?"
            self.cursor.execute(code2, (price, name))

            self.link.commit()

            return price

    def create_box(self,name):

        code = "Select * From AVM where name = ?"
        self.cursor.execute(code, (name,))

        liste = self.cursor.fetchall()

        if (len(liste) == 0):
            print("This product don't exist")
        else:
            price = liste[0][4]
            return price

    def expiration_date(self,name,):

        code = "Select * From AVM where name = ?"
        self.cursor.execute(code, (name,))

        liste = self.cursor.fetchall()

        if (len(liste) == 0):
            print("This product don't exist")
        else:
            LCD = liste[0][2].split("/")
            return LCD
