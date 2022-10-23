def not_hesapla(satır):
    satır = satır.rstrip("\n")
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1 * 0.3 + not2 * 0.3 + not3 * 0.4

    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "DF"

    else:
        harf = "FF"

    return isim + "----------------->" + str(son_not) + "------------> "+  harf + "\n"


def kalanlar(satır2):
    satır2 = satır2.rstrip("\n")
    liste1 = satır2.split(",")
    isim = liste1[0]
    not11 = int(liste1[1])
    not22 = int(liste1[2])
    not33 = int(liste1[3])
    last = not11 * 0.3 + not22 * 0.3 + not33 * 0.4

    if (last <= 55):
        return isim + "----------------->" + str(last) +"\n"

def geçenler(satır3):
    satır3 = satır3.rstrip("\n")
    liste2 = satır3.split(",")
    isim = liste2[0]
    not111 = int(liste2[1])
    not222 = int(liste2[2])
    not333 = int(liste2[3])
    son_not = not111 * 0.3 + not222 * 0.3 + not333 * 0.4

    if (son_not >= 90):
        harf = "AA"
        return isim + "----------------->" + str(son_not) + "------------> " + harf + "\n"
    elif (son_not >= 85):
        harf = "BA"
        return isim + "----------------->" + str(son_not) + "------------> " + harf + "\n"
    elif (son_not >= 80):
        harf = "BB"
        return isim + "----------------->" + str(son_not) + "------------> " + harf + "\n"
    elif (son_not >= 75):
        harf = "CB"
        return isim + "----------------->" + str(son_not) + "------------> " + harf + "\n"
    elif (son_not >= 70):
        harf = "CC"
        return isim + "----------------->" + str(son_not) + "------------> " + harf + "\n"
    elif (son_not >= 65):
        harf = "DC"
        return isim + "----------------->" + str(son_not) + "------------> " + harf + "\n"
    elif (son_not >= 60):
        harf = "DD"
        return isim + "----------------->" + str(son_not) + "------------> " + harf + "\n"
    elif (son_not >= 55):
        harf = "DF"
        return isim + "----------------->" + str(son_not) + "------------> " + harf + "\n"


with open("dosya.txt", "r", encoding="utf-8") as file:
    eklenecekler_listesi = []

    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))

    with open("notlar.txt", "w", encoding="utf-8") as file2:

        for i in eklenecekler_listesi:
            file2.write(i)

with open("dosya.txt", "r", encoding="utf-8") as file3:
    kalanlar_listesi = []

    for i in file3:
        kalanlar_listesi.append(kalanlar(i))

    with open("kalanlar.txt", "w", encoding="utf-8") as file4:

        for i in kalanlar_listesi:
            try:
                file4.write(i)
            except:
                pass

with open("dosya.txt", "r", encoding="utf-8") as file5:
    geçenler_listesi = []

    for i in file5:
        geçenler_listesi.append(geçenler(i))

    with open("geçenler.txt", "w", encoding="utf-8") as file6:

        for i in geçenler_listesi:
            try:
                file6.write(i)
            except:
                pass
