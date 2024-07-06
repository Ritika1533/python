#QUESTION1: print 1 to 10
i=1
while i<=10 : 
    print(i)
    i+=1

#QUESTION2 : print 10 to 1
j=10
while j>=0 :
    print(j)
    j-=1


#QUESTION3 : print multiplication table
# number=int(input("enter the number for multiplication table"))
# k=1
# while k<=10 :
#     print(number*k)
#     k+=1

#QUESTION4 : PRINT [1,4,9,16,25,36,49,64,81,100]
num=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(num) :
    print(num[i])
    i+=1

#QUESTION5 : search x in tupple  (1,4,9,16,25,36,49,64,81,100)
tup= (1,4,9,16,25,36,49,64,81,100)
find=64
i=0
while i<len(tup) :
    if(tup[i]==find):
        print("found")
        break
    i+=1

#QUESTION6 :  PRINT [1,4,9,16,25,36,49,64,81,100] using for loop
listFor=[1,4,9,16,25,36,49,64,81,100]
find2=49
for el in listFor :
    print(el)
   
for el in listFor:
    if(el==find2):
        print("found")


#QUESTION7 : print sum of n numbers
term=int(input("enter the number"))
i=1
sum=0
while i<=term :
    sum=sum+i
    i+=1
print(sum) 



#QUESTION7 : finf factorial of n
j=1
fact=1
while(j<=term):
    fact=fact*j
    j+=1
print(fact)