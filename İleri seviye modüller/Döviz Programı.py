# biz bunun için bilgilerimizi Json objesi olarak alıp bu bilgileri doları türk lirasını çevirmek için falan kullanacağız.
"""
Json objesi
-> sözlük objesine benzer.
"""

import requests
import sys

url = "http://data.fixer.io/api/latest?access_key=23a38fb98b0b297edb241f8e4a80119c&format=1"

firstValue = input("birinci döviz: ")
secondValue = input("ikinci döviz: ") # çevirmek istediğimiz döviz
amount = float(input("Çevirmek istediğiniz miktar ne: "))

response = requests.get(url + firstValue)

# bunu json objesine döndürerek try ye dönüştüreceğiz.

jsonData = response.json()

# artık secondValue yi jsonData içerisinde aramam gerkiyor.
# ama ilk başta jsonData içerisindeki rates anahtar kelimesini aramam gerekiyor.

# print(jsonData["rates"])
# artık değerlerin yazılı olduğu objeye sahibiz.
# şimdi bunun üzerinde secondValue yi arıyacağız.
# print(jsonData["rates"][secondValue])

# bu değeri belli bir miktarla çarpıp kullanıcıya sunabiliriz. Yani kullanıcı bir dolar fazlasını merak ederse mesela 5 dolar kaç tl ?
try:
    print(jsonData["rates"][secondValue] * amount)
except KeyError:
    sys.stderr.write("Lütfen para birimlerini doğru girin.")
    sys.stderr.flush()
# bu döviz uygulamamızın daha güvenli bir şekilde kullanmamızı sağlar.


#  bu kod sadece euro yu istediğiniz para birimine dönüştürüyor.