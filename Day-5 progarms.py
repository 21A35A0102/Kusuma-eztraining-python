'''import random as r
x= "i love sweets "
print(r.sample(x,2))

#every time it gives different output
a=[1,2,3,4,5,6]

r.shuffle(a)
print(a)

a=[1,2,3,4,5]
print(r.choice(a))

b= "welcome back"
print(r.choice(b))

a=r.random()
print(r.choice(b))

a=r.random()
print(a)

#to
z=dir(r)
print

#Display whole year calendar

import calendar

print("full calendar")
print(calendar. calendar(2022))

print("particular month")
print(calendar. month(2021,3))

print("set first day of the week")
calendar.setfirstweekday(calendar.Friday)
print(calendar.month(2021,12))

#
import datetime

a=datetime.datetime.now()
print(a)

sv=a.strftime("%y") #lower case
fv=a.strftime("%y") #upper case

print("year short version",sv)
print("year full version",fv)

#
def sample(): #def or des
    print("great day")
    print("happy time")


sample() #call
print("today ")
sample()

#without argument,without return value

def multi():
    n1=int(input("Number"))
    n2=int(input("Number"))
    n3=int(input("Number"))
    prod=n1*n2*n3
    return prod
res=multi()
print(res)

#with argument,without return value
#static input
def multi (n1,n2,n3):
    prod=n1*n2*n3
    print(prod)

multi(3,4,5)

#user input
def multi1(a,b,c):
    prod=a*b*c
    print(prod)

n1=int(input("Enter 1:"))
n2=int(input("Enter 2:"))
n3=int(input("Enter 3:"))
multi1(n1,n2,n3)
#
def lemons():
    n=int(input("number of lemons"))
    if n>27:
         exess=n-21
         print("exess lemons",excess)
    else:
        less=21-n
        print("less lemons",less)
lemons()
#
def multi_table(n):
    for i in range(1,11):
        print(i,"x",n,"=",i*n)

n=int(input("which table? :"))
multi_table(n)

#
def digits(n):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
        return sum
n=int(input("enter the number"))
res=digits(n)
print(res)'''

#
def display():
    n=int(input("Enter a number"))
    if n==1:
        display()
    else:
        print("over")
        
display()
    

        
