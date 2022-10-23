# kullanıcının girdiği sayıları toplayacağım
print("""
 "q" tuşuna basarak girdiğiniz tüm sayıların toplamını görebilirsiniz.
""")
toplam =0

while True:
    x=input("enter a number:")

    if(x == "q"):
        break
    x = int(x)
    toplam += x

print("girdiğiniz sayıların toplamı = ",toplam)