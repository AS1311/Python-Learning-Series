def numbers(students):
    sub=[]
    num={}
    ns=len(students)
    for n in range(ns):
        for a in students[n]:
            if not a in sub:
                sub.append(a)            
    for s in sub:
        ct=0
        for n in range(ns):
            if s in students[n]:
                ct=ct+1
        num.update({s:ct})
    return(num) 
print("number of students")
n=int(input())
students=[]
li=[]
for i in range(n):
    print("enter no. of subjects for student",(i+1))
    st=int(input())
    print("enter the subjects")
    li=[]
    for j in range(st):
        ele=input()
        li.append(ele)
    students.append(li)
print(students)
num=numbers(students)
def popular(num):
    mx=0
    de=len(num)
    for key,value in num.items():
        if value>mx:
            mx=value
            popular_course=key
    print("most popular course=")        
    return(popular_course)
print(popular(num))   


