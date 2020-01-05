from time import time
from random import randint

from merge_sort import merge_sort
from bubble_sort import bubble_sort,bubble_sort_optimised
from bogo_sort import bogo_sort
from insertion_sort import insertion_sort

sorts=[merge_sort,bubble_sort,bubble_sort_optimised,insertion_sort]
inlist=[randint(0,10000) for i in range(0,randint(0,1000))]

for sort in sorts:
    temp=inlist[:] # Sorts work in place, so create a copy
    start=time()
    sort(temp)
    print(f'{sort.__name__} took {time()-start} seconds.')
