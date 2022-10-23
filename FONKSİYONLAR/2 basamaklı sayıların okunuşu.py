"""
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
"""

birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunuş(sayı):
    BİRİNCİ = sayı % 10
    İKİNCİ = sayı // 10

    a =onlar[İKİNCİ] + " " + birler[BİRİNCİ]
    return a

sayı = int(input("sayı: "))

print("okunuşu:",okunuş(sayı))
