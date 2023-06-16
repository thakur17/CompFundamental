def palin (x):
    y=''
    for i in range(len(x)-1,-1,-1):
        y=y+x[i]
        print(y + " the value of i "+str(i))
    if x==y:
        print("The "+x+" string is a palindrom")
    else:
        print("The "+x+" string is not a palindrom")

x=input("Enter a word to check for the palindrom: ")
print(len(x))
palin(x)
