"""
kullanıcıdan aldığınız bir sayının armstrong sayısı olup olmadığını bulmaya çalışın.
örnek olarak eğer bu sayı 4 basamaklı ise ve oluşturulan rakamlardan her birinin 4. kuvvetinin toplamı
(3 basamaklı sayılar için 3.kuvveti) o sayıya eşitse bu sayıya armstorng sayısı denir.
örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    basamak = gecici_sayı % 10

    toplam += basamak ** basamak_sayisi
    gecici_sayı /= 10
    gecici_sayı = int(gecici_sayı)
    # or    gecici_sayı //= 10   (bölümü bulur)

if (toplam == sayı):
    print(sayı, "bir armstrong sayısıdır.")
else:
    print(sayı, "bir armstrong sayısı değildir.")

