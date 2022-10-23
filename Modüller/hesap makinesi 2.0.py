# math metodunu kullanrak hesap makinesi 2.0 ı oluşturun.

import time
import math

print("""
1.işlem = sum                                                            
2.işlem = subtraction
3.işlem = multiplication
4.işlem = division
5.işlem = converts the given decimal number to a higher number
6.işlem = EBOB
7.işlem = absolute value
8.işlem = factorial
9.işlem = converts the given decimal point to a lower number
10.işlem = finds the remainder of the given first parameter in the second parameter
11.işlem = area od circular
12.işlem = circumference of the circle
13.işlem = calculates the logarithia of the given number at the base of 2
14.işlem = calculates the logarithia of the given number at the base of 10
15.işlem = takes the strength of the first number by the second number
16.işlem = calculates the outpost of the given number
17.işlem = converts the given number from grade to radar
18.işlem = calculates the sine of the given number
for exit = "q"
""")

while True:
    işlem = input("enter the operation you want to use:")
    if (işlem == "q"):
        time.sleep(0.5)
        print ("CHECKİNG OUT....")
        break
    else:
        işlem = int(işlem)

        if(işlem == 1):
            a = int(input("enter a number: "))
            b= int(input("enter a number: "))
            print("RESULT= ",a+b)
        elif(işlem == 2):
            a = int(input("enter a number: "))
            b = int(input("enter a number: "))
            print("RESULT= ",a-b)
        elif(işlem == 3):
            a = int(input("enter a number: "))
            b = int(input("enter a number: "))
            print("RESULT= ", a*b)
        elif (işlem == 4):
            a = int(input("enter a number: "))
            b = int(input("enter a number: "))
            print("RESULT= ", a/b)
        elif (işlem == 5):
            a = float(input("enter a number: "))
            print("RESULT= ",math.ceil(a))
        elif (işlem == 6):
            a = int(input("enter a number: "))
            b = int(input("enter a number: "))
            print("RESULT= ",math.gcd(a,b))
        elif (işlem == 7):
            a = int(input("enter a number: "))
            print("RESULT= ",math.fabs(a))
        elif (işlem == 8):
            a = int(input("enter a number: "))
            print("RESULT= ",math.factorial(a))
        elif (işlem == 9):
            a = float(input("enter a number: "))
            print("RESULT= ",math.floor(a))
        elif (işlem == 10):
            a = int(input("enter a number: "))
            b = int(input("enter a number: "))
            print("RESULT= ",math.fmod(a,b))
        elif (işlem == 11):
            a = int(input("enter a radius: "))
            print("RESULT= ",(a*a)*(math.pi))
        elif (işlem == 12):
            a = int(input("enter a radius: "))
            print("RESULT= ",a*(math.tau))
        elif (işlem == 13):
            a = int(input("enter a number: "))
            print("RESULT= ",math.log2(a))
        elif (işlem == 14):
            a = int(input("enter a number: "))
            print("RESULT= ",math.log10(a))
        elif (işlem == 15):
            a = int(input("enter a number: "))
            b = int(input("enter a number: "))
            print("RESULT= ",math.pow(a,b))
        elif (işlem == 16):
            a = int(input("enter a number: "))
            print("RESULT= ",math.sqrt(a))
        elif (işlem == 17):
            a = int(input("enter a number: "))
            print("RESULT= ",math.radians(a))
        elif (işlem == 18):
            a = int(input("enter a number: "))
            print("RESULT= ",math.sin(a))
        else:
            print("İNVALİD OPERATİON.....")

