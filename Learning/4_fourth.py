#dictonary : store key value pair nat it is unordered mutable & don't allow dublicate key

stud={
    "name" : "ritika",
    "collage" : "techno india",
    "year" : 4,
    "isAdult" : True,
    "marks" : [56,89,67,34]
}
print(stud)
print(type(stud))
print(stud["collage"])
stud["name"]="Ritika keshri"
stud["middleName"]="kumari"
print(stud)

#null dictonary
null_dict={}  #empty dictnory
null_dict["name"]="ritik"
print(null_dict)

#nested dictonary
student={
    "name": {
        "first" : "golu",
        "middle" : "prasad",
        "last" : "keshri"
    },
    "number" : 7865
}
print(student)
print(student["number"])      #return the key value
print(student["name"]["middle"])
#dictonary methods

print(student.keys())         #will print all the keys
print(list(student.keys()))   #will typecast this into list
print(len(student))           #will print total number of keys
print(student.values())       #will print all the value of key
print(list(student.values())) # will typecast this into list
print(student.items())        #will print all the items with key
pairs=list(student.items())
print(pairs[0])
print(student.get("number"))  #return the key value

#why need of two function to get the value
#print(student["number2"])     #if not found will give ERROR
print(student.get("number2")) #if not found will give NO ERROR will give NONE

new_dict={"name" : "rahul" ,"age" : 18}
student.update(new_dict) #will update the old one will new key value pair
print(student)


#SET in python is collection of unordered items where each item in the set is unique and immutable 
#we can not store list and dictonary in set because item of set are mutable but remember set is 
#mutable we can add or remove element so SET MUTABLE IT'S ELEMENT IMMUTABLE

setCollection={1,7,5,9,9,"hello","world"}
print(setCollection)
print(type(setCollection))
print(len(setCollection))

null_set=set()  #empty set

#methods of set : add remove clear pop union intersection
null_set.add(1)
null_set.add(2)
null_set.add(2)
null_set.add("apple")
null_set.add((2,6,8)) #tupple
#null_set.add([78,9]) can't add this
print(null_set)
print(null_set.pop()) #pop random value
null_set.clear()
print(len(null_set))

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))