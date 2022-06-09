lst=[10,11,12,13,14,15,16]
flag=0
elmnt=15
lst.sort()
low=0
up=len(lst)-1
while(low<up):
    mid=(low+up)//2
    if elmnt==lst[mid]:
        flag=1
        break
    elif elmnt>lst[mid]:
        low=mid+1
    elif elmnt<lst[mid]:
        up=mid-1
print(f"found"if flag>0 else Notfound)

