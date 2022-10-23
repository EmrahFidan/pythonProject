"""
Kullanıcıdan 2 tane sayı alarak
bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
EN BÜYÜK ORTAK BÖLEN
"""

def ebob(sayı1,sayı2):
    ebobb = 1
    if(sayı1 >= sayı2):
        for i in range(1,sayı1):
            if((sayı1 % i == 0) and (sayı2 % i == 0)):
                ebobb = i
    else:
            for i in range(1, sayı2):
                if((sayı1 % i == 0) and (sayı2 % i == 0)):
                     ebobb = i
    return ebobb

sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("\n""Ebob:",ebob(sayı1,sayı2))









