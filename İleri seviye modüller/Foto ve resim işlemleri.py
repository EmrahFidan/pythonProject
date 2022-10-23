from PIL import Image,ImageFilter
# ımage filter 'ı blur işlemi için dahil ettik.

image = Image.open("kuş.jpg") # resmimiz açılmış oluyor.
"""
image.show() # resmimizi göstermek için kullandığımız fonksiyon.
# unutma bu resim dosyaları çalıştığın proje dosyasının içinde olmalı.
"""

image.save("kuş2.jpg") # farklı bir isimle bu dosyanın içine kopyalamak için.

# resmi döndürmek için
image.rotate(180).save("kuş3.jpg") # hem döndürdük hem de kaydettik

# resmin sadece siyah beyaz halini almak için
image.convert(mode = "L").save("kuş4.jpg")

# boyutlarını düşürelim.
degistir = (960,360)
image.thumbnail(degistir)
image.save("kuş5.jpg")

# resmi bulurlaştırmak için
image.filter(ImageFilter.GaussianBlur(5)).save("kuş6.jpg") # istediğin değeri girebilirsin

# bir resmi kırpmamız için koordinat bilmemiz gerekiyor.
# PhotoScape üzerinden düzenleyiciyi aç kesim yapacağın dosyayı bul ve sürükle.
# kırp 'a bas kırpacağın alanı ayarla.
# resimin altında kordinatlar yazar.
# fareniz konumda olsun altta yuazar.
# (1129,1052) ve (427,35)
# bunu da 4'lü bir demet şeklinde oluşturacağız.
# önce üst kısımın köşegenini yaz.

kırpılacak_alan = (427,35,1129,1052)
image2 = Image.open("Atatürk.jpg")
image2.crop(kırpılacak_alan).save("ATAM.jpg")
