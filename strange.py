def strange(j):
    k=0
    while j > 0:
        k=10*k+j%10
        j=j//10
        return k
print(strange(1230))

foo=[1,2,3,'a',None,(),[],]
print(len(foo))        

word = "positive"
print(word[:2])