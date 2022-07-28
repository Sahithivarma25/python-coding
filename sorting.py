"""Selection Sort
   --------------
l=[56,3,2,78,6,0]
for i in range(len(l)):
    m=min(l[i:])
    a=l.index(m,i)
    l[i],l[a]=l[a],l[i]
print(l)

"""
""" Bubble sort
    ------------
l=[10,15,4,23,0]
for j in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l)

"""
"""Quick Sort
   --------------
def pivot(data,first,last):
    p=data[first]#56
    left=first+1#1
    right=last#5
    while True:
        while left<=right and data[left]<=p:#5<=5 and 93<=56
            left=left+1#5
        while left<=right and data[right]>=p:#5<=5 and 93>=56
            right=right-1#4
        if right<left:#4>5
            break
        else:
            data[left],data[right]=data[right],data[left]#44-93
    data[first],data[right]=data[right],data[first]
    return right#4
def quick(data,first,last):
    if first<last:
        a=pivot(data,first,last)#4
        quick(data,first,a-1)#0,3
        quick(data,a+1,last)#4,5
data=[54,26,93,17,77,31]
n=len(data)#
quick(data,0,n-1)#0,5
print(data)

 Merge Sort
    -----------"""
def merge(l):
    if len(l)>1:
        mid=len(l)//2
        a=l[:mid]
        b=l[mid:]
        merge(a)
        merge(b)
        i=0
        j=0
        k=0
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                l[k]=a[i]
                i+=1
                k+=1
            else:
                l[k]=b[j]
                j+=1
                k+=1
        while i<len(a):
            l[k]=a[i]
            i+=1
            k+=1
        while j<len(b):
            l[k]=b[j]
            j+=1
            k+=1"""
l=[int(input()) for i in range(5)]
print(merge(l))
print(l)
    

""" Sieve
    ------
n=int(input())
prime=[]
for i in range(n+1):
    prime.append(i)
prime[0]=0
prime[1]=0
p=2
while p*p<=n:
    if p!=0:
        for i in range(p*2,n+1,p):
            prime[i]=0
    p+=1
for i in range(len(prime)):
    if prime[i]!=0:
        print(prime[i],end=" ")
"""
"""  Sliding Window
     --------------
def fun(arr,k):
    n=len(arr)#9
    if n<k:
        return -1
    a=sum(arr[:k])
    b=a
    for i in range(n-k):
        a=a-arr[i]+arr[i+k]
        b=max(a,b)#27
    return b
arr=[1,4,2,5,8,3,9,7,6]
k=4
print(fun(arr,k))
"""
""" Two Pointers
    -------------
def fun(arr,n,k):
    i=0
    j=n-1
    while i<j:
        if arr[i]+arr[j]==k:
            return arr[i],arr[j]
        elif arr[i]+arr[j]<k:
            i+=1
        else:
            j-=1
    return -1

arr = [2, 3, 5, 8, 9, 13, 11]
k = 17
n=len(arr)
print(fun(arr,n,k))
"""
