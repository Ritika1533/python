#count occurrance of character in a string
string=input("enter the string : ")
character=input("enter tha character : ")
count=0
for i in string:
    if(string[i]==character):
        count=count+1
print("the count of character",character,"is",count)