def quick_sort(l):
    if len(l) in [0, 1]:
        return l

    p = l[0]
    smaller = []
    larger = []
    for e in l[1:]:
        if e < p:
            smaller.append(e)
        else:
            larger.append(e)

    return quicksort(smaller) + [p] + quicksort(larger)

def count_quick_sort(l):
    if len(l) in [0, 1]:
        return l, 1

    p = l[0]
    smaller = []
    larger = []

    steps = 0

    for e in l[1:]:
        steps += 1
        if e < p:
            smaller.append(e)
        else:
            larger.append(e)

    left, s = count_quick_sort(smaller)
    steps += s
    right, s = count_quick_sort(larger)
    steps += s

    return (left + [p] + right), steps

from random import randint
print(count_quick_sort([randint(0, 2000) for _ in range(100000)])[1])
