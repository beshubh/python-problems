def msqrt(a):
    low=1
    high=a
    ans=0
    while(low<high):
        mid=(low+high)//2
        print(low,high)
        print(mid)
        if mid*mid is a:
            return mid
        print("high before if "+str(high))
        if mid*mid > a:
            high=mid-1
            print("high after mid *mid > a "+str(high))
        else:
            low=mid+1
    return int(high)
print(msqrt(36))