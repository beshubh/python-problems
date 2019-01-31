def comp(a,b):
    result=0
    while(a>0) or (b>0):
        result+=int((a%2)) ^ int((b%2))
        a//=2
        b//=2
    return result

def diff(B):
    A=[0]*len(B)
    for i in range(len(A)):
        A[i]=B[i]
    temp=[]
    counter=0
    for i in range(len(A)):
        for j in range(len(A)):
            temp.append((A[i],A[j]))
    
    for i in temp:
        print(i)
        print(i[0])
        counter+=comp(i[0],i[1])
    return counter
diff((2,4,6))