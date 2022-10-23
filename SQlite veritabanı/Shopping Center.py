from süpermarket import *
print("""

Processing: 
1- Show me to products
2- Search for Product
3- Add Product
4- Delete Product
5- Search for Mall
6- Raise
7- Sale
8- Create Box
9- Last consumption date check

Press "q" to exit
----------------------------------------------------------------

""")

avm = AVM()

while True:

    process = input("process you do: ")

    if (process == "q"):
        print("Checking OUT...")
        time.sleep(1)
        print("Come Again")
        break

    elif (process == "1"):

        avm.show_product()

    elif (process == "2"):

        name = input("which product do you want to search ")
        print("Searching for product...")
        time.sleep(1)

        avm.search_product(name)

    elif (process == "3"):

        name = input("Product Name: ")
        brand = input("Brand: ")
        expiration_date = input("Expiration Date (please write you /): ")
        sales_location = input("Sales Location: ")
        price = input("Price: ")
        stock_status = int(input("Stock Status: "))

        new_product = product(name,brand,expiration_date,sales_location,price,stock_status)
        print("Adding product")
        time.sleep(1)

        avm.add_product(new_product)
        print("Product added")

    elif (process == "4"):

        name = input("Which song do you want to delete the product ? ")
        print("Searching for product...")
        time.sleep(1)

        solution = input("Are you sure ? (Y/N)")
        if (solution == "Y"):
            print("Deleting Product...")
            time.sleep(1)

            avm.delete_product(name)
            print("Product Deleted")

    elif(process == "5"):

        sales_location = input("which sales location do you want to search ")
        print("Searching for sales location...")
        time.sleep(1)

        avm.search_mall(sales_location)

    elif(process == "6"):

        name = input("Name :")
        ratio = int(input("ratio: "))
        print("Calculating...")
        time.sleep(1)

        avm.Raise(name,ratio)



    elif(process == "7"):

        name = input("Name :")
        ratio = int(input("ratio: "))
        print("Calculating...")
        time.sleep(1)

        avm.sale(name, ratio)

    elif(process == "8"):

        print("Press 'q' to exit")

        a = 0
        while True:
            name = input("Name :")

            if (name == "q"):
                print("Calculating...")
                time.sleep(1)
                print("BOX PRİCE = ",a)
                break

            else:
                a = avm.create_box(name) + a

    elif(process == "9"):

        name = input("Please write you product name :")
        print("Calculating...")
        time.sleep(3)

        LCD = avm.expiration_date(name)

        a = int(LCD[0])
        b = int(LCD[1])
        c= int(LCD[2])


        guncel_tarih = datetime.datetime.now()  # bugünün tam tarihi
        guncel_yil = guncel_tarih.year
        guncel_ay = guncel_tarih.month
        guncel_gun = guncel_tarih.day

        year = c - guncel_yil
        month = b - guncel_ay
        day = a - guncel_gun

        if(year < 0):
            print("this product has expired")
        else:
            if(month < 0 and year == 0):
                print("this product has expired")

            elif(month < 0 and year > 0):
                year = year -1

                if(day < 0):
                    month = month -1

                    year = abs(year)
                    day = 30 - abs(day)
                    if (day > 29):
                        y = month // 30
                        day = day % 30
                        month = month +y
                    month = 12 - abs(month)
                    if (month > 11):
                        x = month // 12
                        month = month % 12
                        year = year + x
                    print("Son tüketim tarihi = {} yıl, {} ay, {} gün sonra ".format(year, month, day))

                elif(day >= 0):
                    year = abs(year)
                    day = 30 - abs(day)
                    if (day > 29):
                        y = month // 30
                        day = day % 30
                        month = month + y
                    month = 12 - abs(month)
                    month = 30 - abs(month)
                    if (month > 11):
                        x = month // 12
                        month = month % 12
                        year = year + x
                    print("Son tüketim tarihi = {} yıl, {} ay, {} gün sonra ".format(year, month, day))

            else:
                if(day < 0 and month == 0 and year == 0):
                    print("this product has expired")

                elif(day < 0 and month == 0):
                    year = year -1

                    year = abs(year)
                    month = abs(month)
                    day = abs(day)
                    print("Son tüketim tarihi = {} yıl, {} ay, {} gün sonra ".format(year, month, day))

                elif(day < 0 and month > 0):

                    month = month -1

                    year = abs(year)
                    day = 30 - abs(day)
                    if (day > 29):
                        y = month // 30
                        day = day % 30
                        month = month + y
                    month = 12 - abs(month)
                    month =12 - abs(month)
                    if (month > 11):
                        x = month // 12
                        month = month % 12
                        year = year + x
                    print("Son tüketim tarihi = {} yıl, {} ay, {} gün sonra ".format(year, month, day))

                else:
                    year = abs(year)
                    month = abs(month)
                    day = abs(day)
                    print("Son tüketim tarihi = {} yıl, {} ay, {} gün sonra ".format(year,month,day))

    else:

        print("illegal process")
