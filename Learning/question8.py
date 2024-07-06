#QUESTION1:  create a class of student that take name and marks of 3 student as argument in a constructor 
#then create a method to print average
class Student():
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def getAverage(self):
        return (self.m1+self.m2+self.m3)/3
    
s1=Student("rahul",98,89,87)
print("average : ",s1.getAverage())