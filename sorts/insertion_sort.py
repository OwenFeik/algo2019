def insertion_sort(m):
    for i in range(1,len(m)):
        j=i
        while j>0 and m[j-1]>m[j]:
            m[j-1],m[j]=m[j],m[j-1]
            j-=1
    return m
