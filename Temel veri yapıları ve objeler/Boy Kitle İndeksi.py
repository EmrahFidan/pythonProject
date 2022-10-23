# kullanıcıdan aldığınız boy ve kitle değerlerine göre kullanıcının beden kitle indeksini oluşturun.
# Beden kitle indeksi = kilo/ boy(m)*boy(m)

kilo=int(input("kilonuzu giriniz:"))
boy=float(input("boyunuzu giriniz: "))

BKİ= kilo/(boy**2)

print("Beden KÜtle İndeksi: ",BKİ)