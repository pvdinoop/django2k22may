expenses=[10000,20000,30000,50000,450000]
for i in expenses:
    print(i)

employees=["bheem,chutki,raju,jaggu"]
for name in employees:
    print(name)
for i in range(0,len(employees)):
    print(employees[i])

numbers=[12,15,23,44,45,64,54,79,38,80]
for i in numbers:
    if i<45:
        print(i-1)
    elif i>45:
        print(i+1)
    else :
        print(45)
num=0
for i in numbers:
    if i>=45 and i<=80:
        num+=1
print(num)
a=0
b=0
c=0
sum=0
numbrs=[-5,-4,-3,-1,0,1,0,2,0,3,0,4,0,5,6,7,8,9]
for i in numbrs:
    if i<0:
        a+=1
    elif i==0:
        b+=1
    elif i>0:
        c+=1
print(a,b,c)
sum=sum+i
print(sum)





