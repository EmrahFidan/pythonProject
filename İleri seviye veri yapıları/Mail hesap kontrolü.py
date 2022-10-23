"""
Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun.
Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.
"""

# endswith(x): String x ile bitiyorsa True, bitmiyorsa False değeri döndürür.
# find(x): x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür.
# Bulamazsa "-1" değerini verir.


with open("mailler.txt","r",encoding= "utf-8") as file:
    dosya_icerigi = file.read()
    kelimeler = dosya_icerigi.split("\n")
    mailler = list()

    for i in kelimeler:
        mailler.append(i)

for i in mailler:
    if (i.endswith(".com") and i.find("@") != -1):
        print(i)


# 2. çözüm
"""
with open("mailler.txt","r",encoding= "utf-8") as file:
    mailler = file.readlines()
    mailler2 = list()

    for i in mailler:
        i = i.strip("\n")
        mailler2.append(i)


for i in mailler2:
    if (i.endswith(".com") and i.find("@") != -1):
        print(i)

"""