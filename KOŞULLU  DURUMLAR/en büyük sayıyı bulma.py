# kullanıcının girdiği 3 sayı arasında en büyüğünü bulma

a=int(input("please enter a number:"))
b=int(input("please enter a number:"))
c=int(input("please enter a number:"))

if(a>=b and a>= c):
    print("en büyük sayı: {}".format(a))
elif(b>=a and b>=c):
    print("en büyük sayı: {}".format(b))
elif(c>=a and c>=b):
    print("en büyük sayı: {}".format(c))
