def palin (x):
    y=''
    for i in range(len(x)-1,-1,-1):
        y=y+x[i]
        print(y)
    z=''
    for i in range(len(x)):
        z=z+x[i]
        print(z)
    for i in range(3):
        print(x[i])

x=input("Enter a word to check for the palindrom: ")
palin(x)
