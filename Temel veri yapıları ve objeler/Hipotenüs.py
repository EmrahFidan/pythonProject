# Kullanıcıdan bir dik üçgenin dik olan iki kenarını alın ve hipotenüs uzunluğunu bulmaya çalışın

a=int(input("yatay kenar uzunluğu:"))
b=int(input("dikey kenar uzunluğu:"))

c=(a**2 + b**2)**(1/2)

print("Hipotenüs=",c)
