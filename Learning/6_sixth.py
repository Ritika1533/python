#FUNCTION IN PYTHON

#function defination
def calSum(a,b) : #parameters
    sum=a+b
    return sum

#function call
print(calSum(2,10))  #arguments


def avg(a,b,c):
    return (a+b+c)/3

print(avg(5,7,9))


def greet():
    print("hello ritika")

print(greet())  #no return value so its printing none

#default parameter
def calSum(a=1,b=1) : 
    sum=a+b
    return sum

#function call
print(calSum())

#RECURSION
def show(n):
    if(n==0):
         return
    print(n)
    show(n-1)
    print("end",n)
show(5)


#factorial
def factorial(n):
    if(n==1 or n==0):
        return 1
    result=n*factorial(n-1)
    print("end",n)
    return result
print("factorial is",factorial(6))