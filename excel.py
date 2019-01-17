def excel(s):
    res=0
    n=len(s) - 1
    var=0
    for i in s:
        var=ord(i)-ord('A')+1
        res+=var*26**n
        n-=1
    return res
print(excel('AB'))