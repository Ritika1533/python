#OOPS
#CLASS 
class Student:
    collage="techno india" #class attribute
    #default constructor
    def __init__(self):
        print("i am a default constructor")
    #parametrised constructor
    def __init__(self,fullName,marks):
        self.name=fullName  #object attribute>> class attribute
        self.marks=marks
        print("i am a parametrised constructor")
    #method
    def greet(self):
        print("hello",self.name)
    def getMarks(self):
        return self.marks
    @staticmethod
    def hello():
        print("hello everyone")
#OBJECT
#self : object that we created
s1=Student("ritika",89)
print(s1.name)
s2=Student("arjun",67)
print(s2.name)
print(s2.collage)
s2.greet()
print(s2.getMarks())
s2.hello()
"""
<__main__.Student object at 0x000001E0CAD05AF0> print(self)
i am a constructor
<__main__.Student object at 0x000001E0CAD05AF0> print(s1)
"""