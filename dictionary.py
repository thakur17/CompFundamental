#Dictionary is a collection where data are
#arranged in key value pair

d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d2 = {
  "brand": "Hyndai",
  "model": "i20",
  "year": 2020}

#print(d1)

f1 = {
  "child1" : {
    "name" : "Emil",
    "dob" : 2004,
    "car":"None"
  },
  "child2" : {
    "name" : "Tobias",
    "dob" : 2007,
    "car":d2
  },
  "child3" : {
    "name" : "Linus",
    "dob" : 2011,
    "car":d1
  }
}
#child1["name"]
for x in f1:
   print(f1[x]["name"]+" was born on "+str(f1[x]["dob"]))
   
  
  
