
lst1=[10,11,11,12,13,14,14,14,15,15]
reclst=[]
for i in range(0,len(lst1)):
    for j in range(i+1,len(lst1)):
        if lst1[i]==lst1[j]:
            reclst.append(lst1[i])
print(reclst)

lst2=[2,3,4,6]
sum=8
for i in range(len(lst2)):
    for j in range(i+1,len(lst2)):
        cursum=lst2[i]+lst2[j]
        if cursum==sum:
            print(f" pairs are {lst2[i],lst2[j]}")
            break

lst=[2,3,4,6]
elmnt=7
lst.sort()
low=0
up=len(lst)-1
while(low<up):
    curtsum=lst[low]+lst[up]
    if curtsum==elmnt:
        print(f"Pairs are {lst[low]}and {lst[up]}")
        break
    elif curtsum<elmnt:
        low+=1
    elif curtsum>elmnt:
        up-=1


