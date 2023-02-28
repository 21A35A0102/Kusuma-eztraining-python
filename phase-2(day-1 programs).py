#lambda function
l=[1,2,3]
r=(lambda x:x+x,l)
print(list(r))

#map
res=map(lambda n:pow(n,2),l)
print(list(res))
name="sam"
(lambda name:print(name))(name)

#write a program after creating a list with even numbers within the range 1 to 15
r=[2,4,6,8,10,12,14]
r=map(lambda x:x**(1/2),r)
print(list(r))

#
from abc import ABC,abstractmethod
class abstractdemo(ABC):
    @abstractmethod #called decorator to
    #make the method(function) abstract one
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
#changing abstract to concrete
class demo(abstractdemo):
    def display(self):
        print("Abstraction method")
    def show(self):
        print("2nd function")
obj=demo()
obj.display()
obj.show()

#one parent and one child class

class parent:      #BASE CLASS
    def display(self):
        print("parent class")

#DERIVED CLASS
class child(parent):
    def show(self):
        print("Child class")

c=child()
c.display()
c.show()

#single inheritance
class A:
    n=30
class B(A):
    def calc(self):
        c=self.n+70
        print(c)
obj=B()
obj.calc()

#Mutliple inheritance
#two classes-one child -like mom,dad---children
#inherits properties of mom and dad
class mom:     #BASE CLASS-1
    def mdisplay(self):
        print("mom class")
class dad:
    def ddisplay(self):
        print("dad class")
class child(mom,dad):
    def cdisplay(self):
        print("child class")

c1=child()
c1.cdisplay()
c1.mdisplay()
c1.ddisplay()

#multilevel inheritance
#one parent and one child class
class grandparent:
    def display(self):
        print("grand parent class")
class parent(grandparent):
    def show(self):
        print("parent class")
class child(parent):
    def printing(self):
        print("child class")
c=child()
c.display()
c.show()
c.printing()

#hierarchial inheritance
#one base class and multiple child class
#objects should be created for child class individual
class parent:
    def pdisplay(self):
        print("parent class")
class child1(parent):
    def c1show(self):
        print("child1 class")
class child2(parent):
    def c2show(self):
        print("child2 class")
c1=child1()
c1.c1show()
c1.pdisplay()
c2=child2()
c2.c2show()
c2.pdisplay()

#hybrid inheritance
class parent:
  def display(self):
    print("parent class")
class child1(parent):
  def c1show(self):
    print("child1 class")
class child2(parent):
  def c2show(self):
    print("child2 class")
class kid1(child1):
  def k1display(self):
    print("kid1 class")
class kid2(child1):
  def k2display(self):
    print("kid2 class")
class kidd1(child2):
  def k1show(self):
    print("kidd1 class")
class kidd2(child2):
  def k2show(self):
    print("kidd2 class")
c1=kid1()
c1.c1show()
c1.display()
c1.k1display()
c2=kid2()
c2.c1show()
c2.display()
c2.k2display()
c3=kidd1()
c3.c2show()    
c3.k1show()
c3.display()
c4=kidd2()
c4.c2show()
c4.display()
c4.k2show()  











