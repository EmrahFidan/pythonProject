"""Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.
"""

YAZI = input("istediğiniz cümleyi kelime aralarında boşluk bırakmadan giriniz:")

frekans = dict()

for i in YAZI:
    if (i in frekans):
        frekans[i] += 1
    else:
        frekans[i] = 1
for i, j in frekans.items():
    print(i, ":", j)
