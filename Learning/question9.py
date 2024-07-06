#QUESTION1:  create class of circle create method to cal area and perimeter
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
circle1=Circle(3)
print("Area f circle : ",circle1.area())
print("perimeter of circle : ",circle1.perimeter())



#QUESTION2 :  create employee class having attribute role,salary and department make a show
#  delail method create engineer class inherit property of employee and   have attribute name & age


class Employee():
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal
    def showDetail(self):
        print("Role : ",self.role)
        print("Department : ",self.dept)
        print("Salary : ",self.sal)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","IT",89000)
e1=Employee("mechanics","EE",67000)
e1.showDetail()
eng1=Engineer("Ram kumar",34)
eng1.showDetail()



#QUESTION3 :  create odere class having attribute item &price use dunder funvtion __gt__
# to convey that order1>order2 if price of  order1>order2
class Order():
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(ord1,ord2):
        return ord1.price > ord2.price

ord1=Order("chips",20)
ord2=Order("tea",15)
print(ord1>ord2)