def fun(data):
    l=0
    r=len(data)-1
    res=0
    while l<=r:
        m=(l+r)//2
        if data[m]==n:
            res=m
            r=m-1
        elif data[m]>n:
            r=m-1
        else:
            l=m+1
    return res
def fun1(data):
    l=0
    r=len(data)-1
    res1=-1
    while l<=r:
        m=(l+r)//2
        if data[m]==n:
            res1=m
            l=m+1
        elif data[m]>n:
            r=m-1
        else:
            l=m+1
    return res1
n=8
data=[5,7,8,8,8]
print(fun1(data)-fun(data)+1)
