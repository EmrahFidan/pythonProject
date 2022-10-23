import requests

from bs4 import BeautifulSoup
# beatifulsoup sınıfımı dahil ediyorum.

url = "https://www.imdb.com/chart/top"

response = requests.get(url) # response değişkenimizin adı

html = response.content # web sayfamızın içeriğini aldık

soup = BeautifulSoup(html,"html.parser") # içeriğimizi parçalamak için bu staırı yazdık

"""
for i in soup.find_all("td",{"class":"titleColumn"}):
# td etiketlerinden classı titleColumn olanları alamk istediğimiz söylüyoruz.
    print(i.text)
# sadece film isimlerini almak için o etiket içindeki yazıları
# almak istediğimi söyleyeceğim. (i.text)
    print("****************************************")
"""

a = float(input("Rating giriniz: "))

# ratingColumn imdbRating (oyların bulunduğu kısım)

names = soup.find_all("td",{"class":"titleColumn"})
ratings = soup.find_all("td",{"class":"ratingColumn imdbRating"})

# print(len(names),len(ratings)) # iki listemizinde boyu 250
# yani sırasıyla birbirlerinin sırasına ve puanına denk geliyorlar.
# zip fonksiyonunu kullanarak buradaki 2 listeyi birleştirebiliriz.

for names,ratings in zip(names,ratings):
    # daha güzel görüntü için \n ve boşlukları kaldırabiliriz.
    names = names.text
    ratings = ratings.text
    # mantıklıı

    names = names.strip() # baştaki ve sondaki boşşlukları siler.
    names = names.replace("\n","") # \n lerin yerine boşluklları atadık.
# Aynı işlemleri rating için uyguluyoruz.
    ratings = ratings.strip()
    ratings = ratings.replace("\n", "")
    """
    print("FİlM ADI = ",names)
    print("RATİNG = ",ratings)
    """
# kullanıcıdın girdiği ratingten daha yüksek olanları göstermeyi çalışalım.
# en başa dönelim ve kullanıcıdan değer alalım.

    if(float(ratings) > a):
        print("FİLM İSMİ: ",names + "\n" + "FİLMİN RATİNGİ: ",ratings)

