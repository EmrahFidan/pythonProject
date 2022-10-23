# geometrik cisim hesaplama işlemi

print("üçgen veya dörtgen girebilirsiniz")
işlem_tipi=input("istediğiniz şekili giriniz: ")

if(işlem_tipi=="dörtgen"):
    a=int(input("1.kenar:"))
    b=int(input("2.kenar:"))
    c=int(input("3.kenar:"))
    d=int(input("4.kenar:"))
    if(a==b and a==c and a==d):
        print("KARE")
    elif((a==b and d==c) or (a==c and b==d) or (a==d and b==c)):
        print("DİKDÖRTGEN")
    else:
        print("DÖRTGEN")
elif(işlem_tipi=="üçgen"):
    a=int(input("1.kenar:"))
    b=int(input("2.kenar:"))
    c=int(input("3.kenar:"))
    if(abs(a+b)>c and abs(a+c)>b and abs(b+c)>a):
        if(a==b and a==c):
            print("EŞKENAR ÜÇGEN")
        elif((a==b and a!=c) or (a==c and a!=b)):
            print("İKİZKENAR ÜÇGEN")
        else:
            print("ÜÇGEN")
    else:
        print("üçgen belirtmiyor....")
else:
    print("geçersiz şekil....")

