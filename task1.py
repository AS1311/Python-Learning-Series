import random
n=random.randrange(1000,9999)
print("generated code=",n)
l1=list(int(d) for d in str(n))
for i in range(10):
    l2=[]
    print("enter your 4 digit code")
    num=int(input())
    l2=list(int(j) for j in str(num))
    c=0
    s=""
    for j in range(4):
        if l2[c]==l1[c]:
            s=s+"R"
        elif l2[c] in l1:
            s=s+"A" 
        else:
            s=s+"W"
        c=c+1
    print(s)
    if s=="RRRR":
        print("congratulations you guessed the right code")
        break      
if (s!="RRRR"):
    print("Sorry, your chances are over")


