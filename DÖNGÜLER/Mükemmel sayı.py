"""
kullanıcıdan alınan sayının mükemmeliğini bulun
bir sayımım kendisi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
"""
print("""
***************
MÜKEMMEL SAYI BULMA
***************
""")

x= int(input("please enter a numbeer:"))

bölenleri = 0

for i in range(1,x):
    if(x % i == 0):
        bölenleri +=i
if(x == bölenleri):
    print("{} mükemmel sayıdır.".format(x))
else:
    print("{} mükemmel sayı değildir.".format(x))

