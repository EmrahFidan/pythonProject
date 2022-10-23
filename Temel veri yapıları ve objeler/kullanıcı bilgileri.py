# Kulllanıcıdan ad,soyad ve numara bilgilerini  alarak bunları alt alta yazdırın

ad=input("adınızı giriniz: ")
soyad=input("soyadınızı giriniz: ")
NO=input("numaranızı giriniz: ")

bilgiler=[ad,soyad,NO]

print("\nBilgiler....\n")
print("Adı: {}\nSoyadı: {}\nNumarası: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))
