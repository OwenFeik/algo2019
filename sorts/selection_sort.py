def selection_sort(l):
    i = 0
    while i < len(l):
        m = min(l[i:])
        s = l[i:]
        s.remove(m)
        l = l[:i] + s
        l = l[:i] + [m] + l[i:]
        i += 1

    return l

from random import randint
print(selection_sort([randint(0, 20) for _ in range(10000)]))