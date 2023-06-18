 #This is the source code to illustrate list data structure

thislist = ["apple", 3,2,2.5, [1,2,3,4],"banana", "cherry"]
print(len(thislist[4]))
thislist[5] = "coconut"
thislist.append(["orange","chocolate"])
thislist.append("banana")
thislist.remove("banana")
#print(thislist)
#print(len(thislist))
      
for i in range(len(thislist)):
    print(type(thislist[i]))
    if i==4:
        for b in thislist[i]:
           # print(b)
            x=type(b)
            if x==int:
                print(x)
    
        
    
