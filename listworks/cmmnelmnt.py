lst1=[10,11,12,13,14,15,16]
lst2=[12,13,14,15,16,17,18]
p1=0
p2=0
lst1.sort()
lst2.sort()
while(p1<len(lst1) and p2<len(lst2)):
    if lst1[p1]==lst2[p2]:
        print(f"common elements is {lst1[p1]} ")
        p1+=1
        p2+=1
    elif lst1[p1]>lst2[p2]:
        p2+=1
    elif lst1[p1]<lst2[p2]:
        p1+=1
