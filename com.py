def convert_to_binary(a):
    ret=[]
    while a>0:
        rem=int(a%2)
        ret.append(str(rem))
        a=int(a/2)
    s= ''.join(ret)
    s=s[::-1]
    return int(s)
def diff(A):
    for i in range(len(A)):
        A[i]=convert_to_binary(A[i])
    temp=[]
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            temp.append((A[i],A[j]))
    print(A)
    print(temp)
# def result(a,b):
#     x=[int(m) for m in str(a)]
#     y=[int(n) for n in str(b)]
#     res=0
#     for i in range(max(len(x),len(y))):
        
#     return res
def result(a,b):
    x=bin(a)
    y=bin(b)
    s=0
    for i in range(len(x)-1,0-1):
        if x[i] is not y[i]:
            s+=1
    return s
diff([2,3,4,7])
# print(result(4,7))
# print(result(10,11))
a=[1,1]
b=[1,0,0]
s=0
for i,j in zip(a,b):
    print(i,j)
print(bin(3,4))