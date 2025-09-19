y=int(input("enter the year"))
for  i in range(2025,y):
    if (i % 400 == 0) or ((i % 4 == 0) and (i % 100 != 0)):
        print(i)