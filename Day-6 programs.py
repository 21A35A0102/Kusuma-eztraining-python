'''a=100
b=0

try:#u r telling  this may hv error, u try
    print(a/b)

#except Exception:#u saying if error thr i handle
#print("cant divide any number by zero")

except Exception as e:
    print("please note, number cant be divided by zero",e)
    #this will print error also

#to check your prg execution goes till end or get
    print("bye")


a=10
try:
    b=int(input("Enter the number"))
    print("resource open")
    print(a/b)
except zeroDivisionError as e:
    print("please note, number cant be divided by zero",e)
except valueError as e:
    print("Invalid Input",e)
except Exception as e:#if not any above errors
    print("others error",e)
finally:
    print("Resource closed")

class computer:    #class definition
    def config(self):  #config is a function
        print("Yes")
lenova=computer() #object1
lenova.config()

dell=computer()  #object2
dell.config()'''

#
class computer():
    a=10
    b=20
    print("class variable inside class",a)

    def config(self): # config is a function
        c=100
        print("Yes")
        print("Instance access",self.b)

lenova=computer() # object1
print(lenova.a)
print(lenova.a+lenova.b)
dell=computer()   #object 2
print("dell" ,dell.a)
lenova.config()

    
    
    
    
