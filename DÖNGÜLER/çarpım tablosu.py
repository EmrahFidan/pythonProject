# 1 den 10'a kadar olan sayıların çarpım tablosunu oluşturunuz.

for i in range(1,11):
    print("***************************************")
    for j in range(1,11):
        print("{} * {} = {}".format(i,j,i*j))
