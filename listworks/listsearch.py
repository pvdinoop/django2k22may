lst=[12,13,14,15,16,17,18,19,20]
elmnt=15
for i in lst:
    if i==elmnt:
        print("elment found")
        break
    else:
        print("elment not found")

newlst=[5,7,6,4,78,12,54,33,64,23,1,98,73,5,5,5]
oddlst=[]
evenlst=[]
for i in newlst:
    if i%2!=0:
        oddlst.append(i)
print(oddlst)

for i in newlst:
    if i%2==0:
        evenlst.append(i)
        print(evenlst)
        evenlst.sort()



print(newlst.count(5))

lst1=[10,11,12,13,14,15,20]
lst2=[12,13,14,15,16,17,18]
flag=0
lst3=[]
for i in lst1:
    for j in lst2:
         if i==j:
             lst3.append(i)
print(lst3)







