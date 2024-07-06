#operator overloading
print(1+3) #add
print("ritika" + "keshri") #concat
print([6,5,3]+[7,9,0]) #merge

#complex number overloading : dunder function
class Complex():
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    def __add__(c1,c2):
        newReal=c1.real + c2.real
        newImg=c1.img + c2.img
        return Complex(newReal,newImg)
    def __sub__(c1,c2):
        newReal=c1.real - c2.real
        newImg=c1.img - c2.img
        return Complex(newReal,newImg)
c1=Complex(4,8)
c1.showNumber()
c2=Complex(6,9)
c2.showNumber()
c3=c1+c2
c3.showNumber()
c3=c1-c2
c3.showNumber()