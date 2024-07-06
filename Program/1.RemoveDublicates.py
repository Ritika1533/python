#REMOVE DUBLICATE ELEMENT FROM LIST
list=[6,8,9,4,5,5,6]
list.sort()
print(list)
i=0
j=i+1
while(j<len(list)):
    if(list[j]==list[i]):
        del list[i]
        i+=1
        j+=1
    else:
        i+=1
        j+=1
print(list)
    