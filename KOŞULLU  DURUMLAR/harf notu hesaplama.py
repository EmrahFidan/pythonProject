# öğrencinin vize1, vize2 ve final notlarına göre harf notunu hesaplama
"""
vize1 =%30
vize2=%30
final=%40
"""

vize1=int(input("VİZE 1:"))
vize2 =int(input("VİZE2:"))
final = int(input("FİNAL:"))

a= vize1 * (3/10)
b= vize2 * (3/10)
c= final *(4/10)

grade = a+b+c

if(grade>=90):
    print("AA")
elif(grade>=85):
    print("BA")
elif(grade>=80):
    print("BB")
elif(grade>=75):
    print("CB")
elif(grade>=70):
    print("CC")
elif(grade>=65):
    print("DC")
elif(grade>=60):
    print("DD")
elif(grade>=55):
    print("FD")
else:
    print("FF")
