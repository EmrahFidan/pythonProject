# beden kitle indeksi 2
"""
BKİ= kilo / (boy(m)**2
BKİ < 18.5 == Zayıf
18.5 < BKİ < 25 == Normal
25 < BKİ < 30 == Kilolu
BKİ > 30 == Obez
"""
boy = float(input("Boyunuzu Giriniz:"))
kilo = int(input("Kilonuzu Giriniz:"))

bki = kilo / (boy ** 2)
print("Beden KÜtle İndeksi: ",bki)
print("\n")
if (bki < 18.5):
    print("Zayıf")
elif (bki >= 18.5 and bki < 25):
    print("Normal")
elif (bki >= 25 and bki < 30):
    print("Kilolu")
else:
    print("Obez")