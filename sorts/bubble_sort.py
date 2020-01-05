def bubble_sort(m):
    while True:
        swapped=False
        for i in range(1,len(m)):
            if m[i-1]>m[i]:
                m[i-1],m[i]=m[i],m[i-1]
                swapped=True
        if not swapped:
            break
    return m

def bubble_sort_optimised(m):
    n=len(m)
    while n>1:
        newn=0
        for i in range(1,n):
            if m[i-1]>m[i]:
                m[i-1],m[i]=m[i],m[i-1]
                newn=i
        n=newn
    return m
