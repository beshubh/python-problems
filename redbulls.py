def func(redbulls,teas,n,c):
    redbulls.reverse()
    teas.reverse()
    redbulls=[0]+redbulls
    teas=[0]+teas
    res=redbulls_and_tea(redbulls,teas,n,c)
    return res
def redbulls_and_tea(redbulls,teas,n,c):
    if n is 0 or c is 0:
        return 0
    else:
        c=c-1
        t1=teas[n]+redbulls_and_tea(redbulls,teas,n-1,c)
        t2=redbulls_and_tea(redbulls,teas,n-1,(c+redbulls[n]))
        result=max(t1,t2)
    return result
res=[]
sample=int(input()) 
while sample is not 0:
    n,c=input().split()
    n=int(n)
    c=int(c)
    redbulls=[int(var) for var in input().split()]
    teas=[ int(var) for var in input().split()]
    res.append(func(redbulls,teas,n,c))
    sample-=1
for i in res:
    print(i)
