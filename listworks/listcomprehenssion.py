lst=[
    [10,11],
    [12,13],
    [14,15],
    [16,17],
    [18,19],
]
fltn_lst=[num for slist in lst for num in slist]
print(fltn_lst)
# numbers greater than 16
grtrsxtn=[num for num in fltn_lst if num>16]
print(grtrsxtn)

oddlst=[num for num in fltn_lst if num%2!=0]
print(oddlst)

evnsum = sum([num for num in fltn_lst if num%2==0])
print(evnsum)
mapp=[ num+1 if num >15 else num-1 for num in fltn_lst ]
print(mapp)