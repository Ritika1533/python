string1=input("enter string1 : ")
string2=input("enter string2 : ")
string1=sorted(string1)
string2=sorted(string2)
if(len(string1)==len(string2)):
    if(string1==string2):
        print("Are anagram")
else:
    print("Not arargam")