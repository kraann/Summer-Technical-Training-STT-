t=int(input())

n,p,q,r=list(map(int,input().split()))


def func(n,t):
    te=t
    
    l=[]   
    i=1
    while te<=n:
        l.append(i*t)
        
        i+=1
        te=i*t
    return l
m={}
t=func(n,p)

for i in t:
    if i in m:
        m[i]+=1
    else:
        m[i]=1
t=func(n,q)

for i in t:
    if i in m:
        m[i]+=1
    else:
        m[i]=1
t=func(n,r)

for i in t:
    if i in m:
        m[i]+=1
    else:
        m[i]=1

c=0
for i in m:
    if m[i]==1:
        c+=1
print(c)