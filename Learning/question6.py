#QUESTION1 :  print the length of list
cities=["munbai","chennai","hydrabad","kolkata"]
states=["jharkhand","west bangal"]
def calLength(list):
    print(len(list))
calLength(cities)
calLength(states)

#QUESTION2: print element in single line
def printSingle(list):
    for el in list:
        print(el)
printSingle(states)
printSingle(cities)

#QUESTION3:  cal factorial of n
def factorial(n):
    fact=1
    i=1
    while(i<=n):
        fact=fact*i
        i+=1
    print("factoroial of ",n,"is",fact)
    return fact  
output=factorial(5) 
print(output)  
    
#QUESTION4: USD TO INR
def usdTOinr(dollar):
    return dollar*83
print(usdTOinr(67))


#QUESTION5: recursive function to print sum of n natural number
def sumN(n):
    if(n==0):
        return 0
    return n+sumN(n-1)  
print(sumN(5))


#QUESTION6 :  print the emement of list
city=["munbai","chennai","hydrabad","kolkata"]
def printL(list,idx):
    if(idx>=len(list)):
        return
    print(list[idx])
    printL(list,idx+1)
printL(city,0)