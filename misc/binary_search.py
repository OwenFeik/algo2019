def binary_search(l, target):
    lower = 0 # The lowest index target could have
    upper = len(l) - 1 # The highest index target could have

    while lower <= upper: # If lower > upper, target is not here
        mid = (lower + upper) // 2 # Choose the midpoint of lower and upper
    
        if l[mid] == target: # When we find the target
            return mid # Return the index
        elif target < l[mid]: # Target is below the middle, lower the range
            upper = mid - 1
        else:
            lower = mid + 1 # Otherwise, the upper range
    
    return -1 # If target isn't found, return -1

def binary_search(l, target):
    if len(l) == 1:
        if l[0] == target:
            return 0
        else:
            return -1
    if len(l) == 0:
        return -1

    lower = 0
    upper = len(l) - 1
    mid = upper // 2

    if l[mid] == target: # When we find the target
        return mid # Return the index
    elif target < l[mid]: # Target is below the middle, lower the range
        upper = mid - 1
    else:
        lower = mid + 1 # Otherwise, the upper range

    i = binary_search(l[lower:upper], target)
    if i == -1:
        return i
    else:
        return i + lower

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(l, 8))
