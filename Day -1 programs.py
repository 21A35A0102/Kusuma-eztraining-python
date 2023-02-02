#Displaying name in mother tongue using unicode for letters
print(chr(3093)+chr(3137)+chr(3128)+chr(3137)+chr(3118)+chr(3110)+chr(3143)+chr(3125)+chr(3135)+chr(3093))
#Assignment
print(chr(3128)+chr(3137)+chr(3110)+chr(3120)+chr(3149)+chr(3126)+chr(3112)+chr(3149))

#Take 3integers,3float,2strings and 1complex number as input and print the same on the screen

num1=int(input("Enter first integer:"))
num2=int(input("Enter second integer:"))
num3=int(input("Enter third integer:"))
print()
fl1=float(input("Enter first float:"))
fl2=float(input("Enter second float:"))
fl3=float(input("Enter third float:"))
print()
string1=input("Enter first string:")
string2=input("Enter second string:")
print()
c1=complex(input("Enter first complex:"))
print()
print("OUTPUT")
print("------")
print("first integer:",num1)
print("second integer:",num2)
print("third integer:",num3)
print("first float:",fl1)
print("second float:",fl2)
print("third float:",fl3)
print("first string:",string1)
print("second string:",string2)
print("first complex:",c1)


#Kumar is buying 75kgs sugar candy and half of it he gives to his friend sam.sam returns to kumar half in what he got now how much candy kumar is having.

initial=int(input("enter initial sugar candy wt:"))
final=(0.75)*initial
print("amount of candy kumar got",final)
remain=initial-final
print("amount of candy sam got",remain)

#multiple inputs in single line

n1,n2=input("enter two integers").split(".")
print(n1)
print(n2)
print(n1+n2)

#swapping,area&perimeter
#swapping

n1=int(input())
n2=int(input())
temp=n1
n1=n2
n2=temp
print("n1=",n1)
print("n2=",n2)

#area
l=int(input("length="))
b=int(input("breadth="))
area=l*b
print("area of the rectangle=",area)

#perimeter
l=int(input("length="))
b=int(input("breadth="))
perimeter=2*(l+b)
print("perimeter of the rectangle=",perimeter)
      


