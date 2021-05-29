s=["delhi","delhi","mumbai","mumbai","delhi","chennai","chennai"]
a=[]
i=0
while i<len(s):
    if s[i] not in a:
        a.append(s[i])
    i+=1
print(a)