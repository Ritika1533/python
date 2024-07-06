#ABSTRACTION
class Car():
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.acc=True #abs hides this
        self.clutch=True  #abs hides this
        print("car started")  #veiwed essential thing
car1=Car()
car1.start()


class Student():
    def __init__(self,name):
        self.name=name
s1=Student("ritik")
print(s1.name)
#del keyword
del s1.name
del s1

#public private (__namevar)
class Account():
    def __init__(self,accNo,accPass):
        self.accNo=accNo
        self.__accPass=accPass
    def reset(self):
        print(self.__accPass)
a1=Account(56478,"vgy@34vg")
#print(a1.__accPass) can not acces vecause of private attribute
a1.reset()  #this can access

#INHERITANCE
class Car():
    @staticmethod
    def start():
        print("started")
    @staticmethod
    def stop():
        print("stop")
#single level
class Toyota(Car):
    def __init__(self,brand):
        self.brand=brand
        super().start()
#multi level
class Fortuner(Toyota):
    def __init__(self,color):
        self.color=color
t1=Toyota("mahindra")
t1.start()
t1.stop()
print(t1.brand)
t2=Fortuner("black")
t2.start()
print(t2.color)

#multiple inheritance
class Mummy():
    @staticmethod
    def cooking():
        print("delicious food")
class Papa():
    @staticmethod
    def teaching():
        print("good teacher")
class Child(Mummy,Papa):
    @staticmethod
    def singing():
        print("good singer")
child1=Child()
child1.cooking()
child1.teaching()
child1.singing()

#@property
class Test():
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"
stud1=Test(78,98,56) 
print(stud1.percentage)
stud1.math=77
print(stud1.percentage)

