# 1 ile 100 arası 3'e bölünebilen sayıları ekrana bastırın. Bu işlemi contunie ile yapmaya çalışın

for i in range(1,101):
    if(i % 3 != 0):
        continue
    print(i)
    