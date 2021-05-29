list1=[1,342,75,23,98]
list2=[75,23,98,12,78,10,1]
i=0
list3=[]
while i<len(list2):
    m=list2[i]
    if m in list1:
        list3.append(m)
    i+=1
print(sorted(list3))