from random import shuffle

def bogo_sort(m):
    target=sorted(m)
    while not m==target:
        shuffle(m)
    return m
