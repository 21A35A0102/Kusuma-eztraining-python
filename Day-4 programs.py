
d={n:n*n for n in range(1,5)}
print(d)
   

#calculating product price for 5 units
old={'rice':60,'dhaal':120,'oil':150}
new={product:price*5 for(product,price)in old.items()}
print(new)

#with checks
real={'sam':24,'angel':18,'kumar':35}
now={name:age for(name,age) in real.items()
     if age>20}
print(now)

#
import random
cust=["kusu","ruchi","sathi","bindhu","modha","apuu","neelu"]

cust_dict={names:random.randint(1,100) for names in cust}

print(cust_dict)
           
#
L1=['a','b','c']
L2=[1,2,3]

d={a:b for (a,b) in zip (L1,L2)}

print(d)

#
m='hi i\'am'

#
L=("i am kusuma")
L.upper()
type(L)
#
L=("kusuma","ruchi","sathvi")
L.count("ruchi")
type(L)
#
s=("sam","jam","kusu")
print(max(s))
#
r=[200]
id(r)
#
r=[200]
r=r+r
id(r)
#
L=[1,2,3]
id(L)
#
L=[4,5,6]
id(L)
#character present or not
s=input("string:")
ch=input("chrt:")
if ch in s:
    print("present")
else:
    print("not present")
#
st=input("Enter the string:")
char=input("Enter req char:")
a="yes" if char in st else no
print(a)
#
s=input("enter a string:")
count=0
for i in s:
    if i==" ":
        count+=1
print(count)
#
L1= input("Enter list of vowels:")
L2=input("Enter req string:")
if L2 in L1:
    print("req string")
else:
    type(L)

