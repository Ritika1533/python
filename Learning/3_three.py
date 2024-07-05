"""
marks=[56,90,35,78,45,24,68]
print(marks)
print(type(marks))
#strng and list are similar here
print(marks[0])
print(marks[4])
print(len(marks))
#we can store any type of variable in list same as in javascript 
studentInfo=["ritika",98,20,"deoghar"]
print(studentInfo)
print(type(studentInfo))
# there is a major diffeerene between string and list that is string is immutable but list is mutables
studentInfo[1]=23
print(studentInfo)
#we can acess the value in range only 
#print(studentInfo[6]) this will give you error 

#SLICING : similar to string
print(marks[1:3])
print(marks[1:])
#similar to marks[1:] ==marks[1:len(marks)]
print(marks[:4])
#similar to marks[:4] ==marks[0:4]

#LIST METHOD : append  sort  insert  remove  pop
marks.append(100)
marks.sort()
print(marks)
#print(marks.append(100)) thisappend will not return anyhing it will add the value in original list same 
#as sort it will not return anything
marks.sort(reverse=True)
print(marks)
fruits=["apple","mango","banana"]
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

fruits.insert(1,"pinapple")
#insert(ind,el)
print(fruits)

fruits.remove("apple")
#it will remove the element found in the first occurrance
fruits.pop(2)
#it will remove element from the particular index 
print(fruits)
"""
"""
TUPLES : 
diff btw tuples and list : list is mutable but tuples is immutable
"""

tup=(56,89,45,32,45)
print(type(tup))
print(tup[1])
#can not assign value it's immutable tup[1]=6
tupp=(1,)
#for assigning single value in tuple use this 
#SLICING
print(tup[1:3])

#tupple method : index  count
print(tup.index(32)) # will give the first occurrance of that element
print(tup.count(45)) # will count the occurrance of that element
