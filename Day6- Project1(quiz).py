q1="""who is your Bestie?
a.Ruchitha
b.Sathvika
c.Bindhu
d.Modha"""

q2="""who is cheif minister?
a.N.chadra babu
b.YS jagan mohan reddy
c.Sanjana
d.Pikuu"""

q3="""who likes you more?
a.Neelima
b.Aparna
c.Harika
d.Priyanka"""

q4="""Who is the best?
a.Aparna
b.Kusuma
c.Neelima
d.sanju"""

q5="""who are beautiful?
a.Aparna
b.Kusuma
c.Neelima
d.sanju"""

questions={q1:"a",q2:"b",q3:"d",q4:"b",q5:"d"}

name=input("Hi Whats ur name")
print("Helo",name,"Welcome to the Quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this ques (yesorno)")
    if flag1=="yes":
        continue
    ans=input("enter your answer")
    if ans== questions[i]:
        print("Wow!you got one point")
        score=score+1
        print("your current score is :",score)
    else:
        print("Wrong answer,u lost 1 mark")
        score=score-1
        print("ur current score is",score)
    flag2=input("Do you want to Quit?")
    if flag2=="yes":
        break
    print("your total score",score)








        
        



        
              





    
        
    
