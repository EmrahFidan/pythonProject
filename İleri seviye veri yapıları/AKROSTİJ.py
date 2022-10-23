"""
Problem 2
"şiir.txt"
Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek
bir string oluşturun ve bu string'i ekrana yazdırın.
"""
akrostij = ""

with open("şiir.txt","r",encoding= "utf-8") as file:
    for satır in file:
        akrostij+= satır[0]
print(akrostij)