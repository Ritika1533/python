#escape sequence character : \n \t
str1="This is a string. We are written it in python."
print(str1)

#concatination
str2="hello"
str3="world"
print(str2+str3)

#length of string
print(len(str2))

#indexing
print(str1[0])
#can not assign value in python str1[3]='b' : not allowed

#slicing format ==> str[starting_indx : ending_indx] (ending index no included)
str4=str1[5:23]
print(str4)
#str[:5] ==> str[0:5] 
#str[5:] ==> str[5:len(str)]
str5=str1[-7:-1]
print(str5)

#string function
str6="i am a coder."
print(str6.endswith("er."))
print(str6.capitalize()) # dosen't chnge in orignial string
print(str6.find('am')) #return index first time occurrance
print(str6.count('coder')) # count the occurrance

#condition
age=21
if(age>=18):
    print("can apply for licance")
else:
    print("can not apply")
