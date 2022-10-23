# Kullanıcıdan 2 tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

a=int(input("1.sayı:"))
b=int(input("2.sayı:"))

print("Değiştirilmeden önceki değerler: a={},  b={}".format(a,b))

a,b=b,a

print("Değiştirildikten sonraki değerler: a={},  b={}".format(a,b))
