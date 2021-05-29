list1=[1,5,10,12,16,20]
list2=[1,2,10,13,16]
i=0
while i<len(list2):
    m=list2[i]
    if m not in list1:
        list1.append(m)
    i+=1
print(sorted(list1))