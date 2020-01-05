# def merge_sort(m):
#     return m if len(m)<=1 else merge(merge_sort(m[:len(m)//2]),merge_sort(m[len(m)//2:]))

# def merge(l,r):
#     return [(l.pop(0) if r[0]>=l[0] else r.pop(0)) if r and l else (l.pop(0) if l else r.pop(0)) for _ in range(len(l)+len(r))]

def merge_sort(m):
    if len(m)<=1:
        return m

    l=m[:len(m)//2]
    r=m[len(m)//2:]

    l=merge_sort(l)
    r=merge_sort(r)

    return merge(l,r)

def merge(l,r):
    m=[]

    while len(l)>0 and len(r)>0:
        steps += 1
        if l[0]<=r[0]:
            m.append(l.pop(0))
        else:
            m.append(r.pop(0))

    m.extend(l)
    m.extend(r)

    return m


print(merge_sort([1,4,5,2,3,6]), steps)